# FreeSearch - AI-Powered Legal Research Tool

**Note:** This repository is named "FreeSearch" but contains a specialized legal research application called "Deep Research Legal".

This project is a comprehensive legal research application built with a React frontend and a LangGraph-powered backend agent. The agent performs sophisticated legal research by dynamically generating targeted legal search queries, gathering information from authoritative legal sources, analyzing results to identify knowledge gaps, and iteratively refining searches until it can provide well-supported legal analysis with proper citations. This application serves as a powerful tool for legal professionals, students, and researchers conducting thorough legal research using LangGraph and Google's Gemini models.

![FreeSearch Legal Research Tool](./app.png)

## Features

- ⚖️ **Specialized Legal Research**: React frontend with LangGraph backend specifically designed for legal research and analysis
- 🧠 **AI-Powered Research Agent**: LangGraph agent that conducts sophisticated legal research workflows
- 🔍 **Intelligent Query Generation**: Dynamic legal query generation using Google Gemini models with legal terminology
- 🌐 **Authoritative Source Integration**: Legal research via Google Search API targeting case law, statutes, regulations, and legal databases
- 🤔 **Knowledge Gap Analysis**: Reflective reasoning to identify missing legal information and refine searches
- 📄 **Comprehensive Legal Analysis**: Generates detailed legal analysis with proper citations and precedent references
- 🔄 **Development Hot-Reloading**: Live reload for both frontend and backend during development
- ⚖️ **Legal-Focused Interface**: Specialized UI with research depth options (Basic, Comprehensive, Deep Analysis)
- 📚 **Multi-Source Research**: Covers case law, statutes, regulations, legal precedent, and secondary sources

## Project Structure

The project consists of two main components:

- **`frontend/`**: React application built with Vite, TypeScript, and Tailwind CSS
  - Modern React 19 with TypeScript
  - Shadcn UI components for consistent design
  - LangGraph SDK integration for real-time streaming
  - Responsive design optimized for legal research workflows

- **`backend/`**: LangGraph/FastAPI application with specialized legal research agent
  - Python-based LangGraph agent for legal research workflows
  - Google Gemini integration for AI-powered analysis
  - Google Search API integration for legal source gathering
  - FastAPI server with streaming capabilities

## Getting Started: Development and Local Testing

Follow these steps to get the application running locally for development and testing.

**Prerequisites:**

- Node.js 18+ and npm (or yarn/pnpm)
- Python 3.11+
- **Google Gemini API Key**: Required for the backend AI agent
  1. Navigate to the `backend/` directory
  2. Copy `backend/.env.example` to `backend/.env`
  3. Add your Gemini API key: `GEMINI_API_KEY="YOUR_ACTUAL_API_KEY"`
- **Optional**: Google Search API credentials for enhanced web research capabilities

**Install Dependencies:**

**Backend Dependencies:**
```bash
cd backend
pip install .
```

**Frontend Dependencies:**
```bash
cd frontend
npm install
```

**Run Development Servers:**

**Start Both Frontend and Backend:**
```bash
make dev
```
This command starts both servers concurrently. Access the application at `http://localhost:5173/app`.

**Run Servers Separately (Alternative):**
- **Backend**: `cd backend && langgraph dev` (available at `http://127.0.0.1:2024`)
- **Frontend**: `cd frontend && npm run dev` (available at `http://localhost:5173`)

The backend also provides access to the LangGraph UI for debugging and monitoring agent workflows.

## How the Legal Research Agent Works

The backend features a sophisticated LangGraph agent (defined in `backend/src/agent/graph.py`) that specializes in legal research workflows:

![Legal Research Agent Workflow](./agent.png)

**Research Workflow:**

1. **Legal Query Generation**: Analyzes your legal question and generates targeted search queries using Google Gemini with legal-specific terminology and context
2. **Authoritative Source Research**: Executes searches using Google Search API, focusing on case law, statutes, regulations, and legal commentary from authoritative sources
3. **Legal Analysis & Knowledge Assessment**: Evaluates research results for completeness, identifying gaps in legal precedent, jurisdictional variations, or conflicting authorities
4. **Iterative Research Refinement**: Generates follow-up queries to address knowledge gaps, targeting specific legal authorities, jurisdictions, or recent developments (configurable loop limit)
5. **Comprehensive Legal Analysis**: Synthesizes gathered information into detailed legal analysis with proper citations, case references, and statutory authority

## Production Deployment

The application is designed for production deployment with Docker. The backend requires Redis (for pub-sub messaging and real-time streaming) and PostgreSQL (for data persistence, thread management, and task queue with exactly-once semantics).

**Requirements:**
- Docker and Docker Compose
- Google Gemini API Key
- LangSmith API Key (optional, for monitoring and debugging)

**Build and Deploy:**

1. **Build Docker Image:**
   ```bash
   docker build -t freesearch-legal -f Dockerfile .
   ```

2. **Run with Docker Compose:**
   ```bash
   GEMINI_API_KEY=<your_gemini_api_key> LANGSMITH_API_KEY=<your_langsmith_api_key> docker-compose up
   ```

**Access the Application:**
- Frontend: `http://localhost:8123/app/`
- API: `http://localhost:8123`

**Configuration Notes:**
- For custom deployments, update the `apiUrl` in `frontend/src/App.tsx`
- Default URLs: `http://localhost:8123` (production) or `http://localhost:2024` (development)
- See [LangGraph Documentation](https://langchain-ai.github.io/langgraph/concepts/deployment_options/) for advanced deployment options

## Technologies Used

**Frontend:**
- [React 19](https://reactjs.org/) with [TypeScript](https://www.typescriptlang.org/) - Modern React application with type safety
- [Vite](https://vitejs.dev/) - Fast build tool and development server  
- [Tailwind CSS](https://tailwindcss.com/) - Utility-first CSS framework
- [Shadcn UI](https://ui.shadcn.com/) - Reusable component library
- [LangGraph SDK](https://github.com/langchain-ai/langgraph) - Real-time streaming integration

**Backend:**
- [LangGraph](https://github.com/langchain-ai/langgraph) - Agent workflow orchestration and management
- [Google Gemini](https://ai.google.dev/models/gemini) - Large language model for legal analysis and query generation
- [FastAPI](https://fastapi.tiangolo.com/) - High-performance Python web framework
- [Google Search API](https://developers.google.com/custom-search/v1/overview) - Web search integration for legal sources
- [Redis](https://redis.io/) - Pub-sub messaging and caching (production)
- [PostgreSQL](https://www.postgresql.org/) - Data persistence and state management (production)

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details.

**Note**: The backend component (`backend/`) contains an MIT license from its original development. The overall project follows the Apache License 2.0. 