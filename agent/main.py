import os
import asyncio
import json
from typing import Dict, Any, Optional
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
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

# NEW: Real OpenAI streaming function
async def get_agent_response_streaming(industry: str, client: str, region: str):
    """Generate sales strategy using streaming with real OpenAI responses"""
    try:
        from openai import AsyncOpenAI
        
        # Initialize OpenAI client
        openai_client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        
        # Get the agent configuration (but use OpenAI directly for streaming)
        agent_function = industry_agent_map[industry]
        agent = agent_function(client, region)
        
        # Extract the system prompt from the agent
        system_prompt = f"""You are an expert {industry} sales strategist. 
        Create a detailed sales strategy for {client} in the {region} region.
        
        Include:
        - Market analysis and opportunity assessment
        - Competitive positioning
        - ROI projections and key metrics
        - Implementation timeline
        - Risk mitigation strategies
        - Success measurement criteria
        
        Format the response in markdown with clear sections and bullet points."""
        
        query = f"Client: {client}, Industry: {industry}, Region: {region}. Generate a comprehensive strategic sales plan with detailed RoI insights and actionable recommendations."

        # Create streaming response
        stream = await openai_client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": query}
            ],
            stream=True,
            temperature=0.7,
            max_tokens=2000
        )
        
        return stream, None
        
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

# Real OpenAI Streaming endpoint 
@app.post("/api/strategy")
async def strategy_stream(request: SalesStrategyRequest):
    """Real OpenAI streaming endpoint"""
    
    if not request.client.strip() or not request.region.strip():
        async def error_stream():
            yield f"data: {json.dumps({'error': 'Both client and region must be provided'})}\n\n"
            yield f"data: [DONE]\n\n"
        return StreamingResponse(error_stream(), media_type="text/event-stream")
    
    async def generate_real_stream():
        try:
            # Send initial status
            yield f"data: {json.dumps({'status': 'Initializing AI agent...', 'isComplete': False})}\n\n"
            await asyncio.sleep(0.5)
            
            yield f"data: {json.dumps({'status': 'Analyzing industry requirements...', 'isComplete': False})}\n\n"
            await asyncio.sleep(0.5)
            
            yield f"data: {json.dumps({'status': 'Researching client background...', 'isComplete': False})}\n\n"
            await asyncio.sleep(0.5)
            
            yield f"data: {json.dumps({'status': 'Generating strategic insights...', 'isComplete': False})}\n\n"
            
            # Get real OpenAI streaming response
            stream, error = await get_agent_response_streaming(
                request.industry, 
                request.client, 
                request.region
            )
            
            if error:
                yield f"data: {json.dumps({'error': error})}\n\n"
                yield f"data: [DONE]\n\n"
                return
            
            # Stream the real OpenAI response
            if stream:
                yield f"data: {json.dumps({'status': 'Streaming results...', 'isComplete': False})}\n\n"
                await asyncio.sleep(0.5)
                
                full_content = ""
                
                # Start with empty content
                yield f"data: {json.dumps({'content': '', 'isComplete': False})}\n\n"
                await asyncio.sleep(0.1)
                
                # Stream real OpenAI chunks
                async for chunk in stream:
                    if chunk.choices[0].delta.content:
                        content = chunk.choices[0].delta.content
                        full_content += content
                        
                        # Send the accumulated content
                        yield f"data: {json.dumps({'content': full_content, 'isComplete': False})}\n\n"
                        await asyncio.sleep(0.01)  # Small delay for smooth display
                
                # Send completion signal
                yield f"data: {json.dumps({'content': full_content, 'isComplete': True, 'type': 'complete'})}\n\n"
                yield f"data: [DONE]\n\n"
            
        except Exception as e:
            yield f"data: {json.dumps({'error': f'Internal server error: {str(e)}'})}\n\n"
            yield f"data: [DONE]\n\n"
    
    return StreamingResponse(generate_real_stream(), media_type="text/event-stream")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 