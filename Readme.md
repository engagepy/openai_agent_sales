# Enterprise AI Sales Agent Platform

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-green.svg)](https://fastapi.tiangolo.com/)
[![Next.js](https://img.shields.io/badge/Next.js-14-black.svg)](https://nextjs.org/)
[![OpenAI](https://img.shields.io/badge/Powered_by-OpenAI-orange)](https://openai.com)

An intelligent, industry-specialized AI sales agent platform that generates personalized enterprise sales strategies with real-time streaming responses. Built with OpenAI's Agents SDK, FastAPI, and Next.js.

## 🎯 What It Does

This platform provides AI-powered sales strategists specialized across 25+ industries, each capable of:
- **Analyzing target enterprise clients** with real-time web research
- **Generating customized sales strategies** tailored to specific regions and industries
- **Providing ROI projections** and competitive analysis
- **Validating inputs** with intelligent guardrails
- **Streaming responses** for real-time feedback

## ✨ Key Features

### 🤖 Multi-Industry AI Agents
Specialized sales strategists for:
- **Technology**: Healthcare, Biotech, Pharmaceutical, Cybersecurity, Telecommunications
- **Finance**: Banking, FS, Insurance
- **Industrial**: Aerospace, Aeronautics, Defence, Manufacturing, Automotive, Energy, Oil & Gas
- **Commercial**: Retail, E-commerce, Logistics, Hospitality, Construction
- **Professional**: Education, Legal, Media, Entertainment, AgriTech

### 🛡️ Intelligent Input Validation
- AI-powered guardrails that verify industry-region-client relevance
- Real-time web search validation
- Prevents hallucinations and invalid queries

### 📊 Comprehensive Sales Intelligence
Each generated strategy includes:
- Client-specific research and business model analysis
- Competitor landscape and differentiation strategies
- Regional regulations and compliance requirements (GDPR, HIPAA, etc.)
- Economic and technological climate assessment
- 3-5 actionable sales campaign ideas
- ROI projections with tangible KPIs
- Reference links and latest news

### 🎨 Modern UI/UX
- Dark futuristic theme with gradient effects
- Real-time streaming with status updates
- Glass-morphism design elements
- Fully responsive interface
- Markdown rendering for formatted results

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Node.js 18+
- OpenAI API Key ([Get one here](https://platform.openai.com/api-keys))

### One-Command Setup

```bash
# Clone and navigate to the repository
git clone <repository-url>
cd agent-sales

# Start both backend and frontend
./start.sh
```

This will open two terminal tabs:
- **Backend**: http://localhost:8000 (FastAPI)
- **Frontend**: http://localhost:3000 (Next.js)

### Manual Setup

#### Backend Setup

```bash
# Install Python dependencies
pip install -r requirements.txt

# Configure environment
cd agent
cp .env.example .env
# Add your OPENAI_API_KEY to .env

# Run the agent server
python main.py
```

#### Frontend Setup

```bash
# Install Node dependencies
cd web
npm install

# Start development server
npm run dev
```

## 📁 Project Structure

```
agent-sales/
├── agent/                      # Backend (FastAPI + OpenAI Agents)
│   ├── main.py                # API endpoints and streaming logic
│   ├── custom_agents.py       # Agent factory and guardrails
│   ├── instruction_templates.py # Industry-specific prompts
│   └── .env                   # Environment variables
├── web/                       # Frontend (Next.js + TypeScript)
│   ├── app/
│   │   ├── components/       # React components
│   │   │   ├── Header.tsx
│   │   │   ├── InfoCards.tsx
│   │   │   ├── StrategyForm.tsx
│   │   │   ├── ResultDisplay.tsx
│   │   │   └── Footer.tsx
│   │   ├── page.tsx          # Main page
│   │   └── layout.tsx        # App layout
│   └── package.json
├── requirements.txt           # Python dependencies
└── start.sh                   # Launch script
```

## 🔧 Configuration

### Environment Variables

Create `agent/.env`:

```bash
OPENAI_API_KEY=sk-...your-key-here
```

### Customizing Industries

Edit `agent/custom_agents.py` to add/remove industries:

```python
_industries = [
    "Your Custom Industry",
    # ... other industries
]
```

### Customizing Strategy Templates

Modify `agent/instruction_templates.py` to adjust the strategy format:

```python
def COMMON_INSTRUCTIONS_TEMPLATE(industry, client, region):
    return f"""Your custom template..."""
```

## 🔌 API Endpoints

### Get Available Industries
```bash
GET http://localhost:8000/api/industries
```

### Generate Strategy (Streaming)
```bash
POST http://localhost:8000/api/strategy
Content-Type: application/json

{
  "industry": "AI Sales Strategist for Healthcare",
  "client": "Mayo Clinic",
  "region": "North America"
}
```

### Generate Strategy (Non-Streaming)
```bash
POST http://localhost:8000/api/generate-strategy
```

## 🧠 How It Works

1. **User Input**: Select industry, enter client name and region
2. **Validation**: AI guardrail agent validates the input using web search
3. **Agent Selection**: Appropriate industry-specialized agent is selected
4. **Research**: Agent performs real-time web research on the client
5. **Strategy Generation**: GPT-4 generates comprehensive sales strategy
6. **Streaming**: Results are streamed back in real-time
7. **Display**: Markdown-formatted strategy is rendered in the UI

## 🛠️ Tech Stack

### Backend
- **FastAPI**: High-performance async web framework
- **OpenAI Agents SDK**: Agentic framework with tools and guardrails
- **Pydantic**: Data validation and settings management
- **uvicorn**: ASGI server
- **WebSearchTool**: Real-time web research capabilities

### Frontend
- **Next.js 14**: React framework with App Router
- **TypeScript**: Type-safe development
- **Tailwind CSS**: Utility-first styling
- **Framer Motion**: Smooth animations
- **Heroicons**: Beautiful icons
- **Server-Sent Events**: Real-time streaming

## 🌐 Alternative Model Providers

While this platform uses OpenAI by default, you can integrate alternative providers using [LiteLLM](https://github.com/BerriAI/litellm):

- **Anthropic Claude**: Advanced reasoning capabilities
- **Google Vertex AI**: Enterprise-grade ML platform
- **AWS Bedrock**: Foundation models on AWS
- **Azure OpenAI**: Microsoft's AI services
- **Mistral**: High-performance open models
- **Cohere**: Enterprise NLP solutions
- **Hugging Face**: Open-source model hub

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open-source and available under the MIT License.

## 💬 Support

For issues, questions, or contributions:
- Open an issue on GitHub
- Contact: [it@m37labs.com](mailto:it@m37labs.com)

## 🎓 Educational Use

This platform is perfect for:
- Learning agentic AI development
- Understanding multi-agent systems
- Building industry-specific AI applications
- Exploring OpenAI's Agents SDK
- Sales strategy automation research

---

**Built with ❤️ using OpenAI Agents SDK**

