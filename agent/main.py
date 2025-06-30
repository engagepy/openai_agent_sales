import os
import asyncio
from typing import Dict, Any, Optional
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
import sys
import time

# Add parent directory to path to import existing modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents import Runner, InputGuardrailTripwireTriggered
from custom_agents import industry_agent_map

# Load environment variables
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY", "")

# FastAPI app
app = FastAPI(
    title="Enterprise AI Sales Agents API",
    description="AI-powered sales strategy generation for enterprise clients",
    version="1.0.0"
)

# CORS middleware for Next.js frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request/Response models
class SalesStrategyRequest(BaseModel):
    industry: str
    client: str
    region: str

class SalesStrategyResponse(BaseModel):
    success: bool
    strategy: Optional[str] = None
    error: Optional[str] = None
    elapsed_time: float

class IndustriesResponse(BaseModel):
    industries: Dict[str, str]

# Agent response function (converted from Streamlit version)
async def get_agent_response(industry: str, client: str, region: str):
    """Generate sales strategy using the appropriate industry agent"""
    try:
        agent_function = industry_agent_map[industry]
        agent = agent_function(client, region)

        query = f"Client: {client}, Industry: {industry}, Region: {region}. Generate a strategic sales plan with RoI insights."

        result = await Runner.run(
            agent, 
            query, 
            context=None
        )
        return result.final_output, None
    except InputGuardrailTripwireTriggered as e:
        output_info = getattr(e, "output_info", None)
        if output_info and hasattr(output_info, "reasoning"):
            reason = output_info.reasoning
        elif output_info and hasattr(output_info, "reason"):
            reason = output_info.reason
        else:
            reason = "⚠️ Input rejected by AI validation agent."
        return None, reason
    except KeyError:
        return None, f"Industry '{industry}' not found"
    except Exception as e:
        return None, f"An error occurred: {str(e)}"

@app.get("/")
async def root():
    """Health check endpoint"""
    return {"message": "Enterprise AI Sales Agents API", "status": "running"}

@app.get("/api/industries", response_model=IndustriesResponse)
async def get_industries():
    """Get available industries"""
    display_map = {
        desc.split()[-1]: desc for desc in industry_agent_map.keys()
    }
    return IndustriesResponse(industries=display_map)

@app.post("/api/generate-strategy", response_model=SalesStrategyResponse)
async def generate_strategy(request: SalesStrategyRequest):
    """Generate sales strategy for given industry, client, and region"""
    
    if not request.client.strip() or not request.region.strip():
        raise HTTPException(
            status_code=400, 
            detail="Both client and region must be provided"
        )
    
    start_time = time.time()
    
    try:
        result, error = await get_agent_response(
            request.industry, 
            request.client, 
            request.region
        )
        
        elapsed_time = round(time.time() - start_time, 2)
        
        if error:
            return SalesStrategyResponse(
                success=False,
                error=error,
                elapsed_time=elapsed_time
            )
        else:
            return SalesStrategyResponse(
                success=True,
                strategy=result,
                elapsed_time=elapsed_time
            )
            
    except Exception as e:
        elapsed_time = round(time.time() - start_time, 2)
        return SalesStrategyResponse(
            success=False,
            error=f"Internal server error: {str(e)}",
            elapsed_time=elapsed_time
        )

# Streaming endpoint for AI SDK compatibility
@app.post("/api/chat")
async def chat_stream(request: SalesStrategyRequest):
    """Streaming endpoint compatible with AI SDK"""
    try:
        result, error = await get_agent_response(
            request.industry, 
            request.client, 
            request.region
        )
        
        if error:
            return {"error": error}
        
        return {"content": result}
        
    except Exception as e:
        return {"error": f"Internal server error: {str(e)}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 