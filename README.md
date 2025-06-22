# FreeSearch - AI-Powered Legal Research Tool

**Note:** This repository is named "FreeSearch" but contains a specialized legal research application called "Deep Research Legal".

This project is a comprehensive legal research application built with a React frontend and a LangGraph-powered backend agent. The agent performs sophisticated legal research by dynamically generating targeted legal search queries, gathering information from authoritative legal sources, analyzing results to identify knowledge gaps, and iteratively refining searches until it can provide well-supported legal analysis with proper citations. This flexible, multi-provider application supports both Google Gemini and OpenAI-compatible endpoints, serving as a powerful tool for legal professionals, students, and researchers conducting thorough legal research.

![FreeSearch Legal Research Tool](./app.png)

## Features

- ⚖️ **Specialized Legal Research**: React frontend with LangGraph backend specifically designed for legal research and analysis
- 🧠 **AI-Powered Research Agent**: LangGraph agent that conducts sophisticated legal research workflows
- 🔀 **Multi-Provider LLM Support**: Flexible provider switching between Google Gemini and OpenAI-compatible endpoints (OpenAI, Ollama, Together AI, etc.)
- 🔍 **Intelligent Query Generation**: Dynamic legal query generation with configurable LLM providers and legal terminology
- 🌐 **Enhanced Search Integration**: Advanced legal research via Google's native Search API with grounding metadata and improved citation system
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
  - Multi-provider LLM support (Google Gemini and OpenAI-compatible)
  - Enhanced Google Search API integration with grounding metadata
  - FastAPI server with streaming capabilities
  - Provider testing infrastructure

## Getting Started: Development and Local Testing

Follow these steps to get the application running locally for development and testing.

**Prerequisites:**

- Node.js 18+ and npm (or yarn/pnpm)
- Python 3.11+
- **LLM Provider API Key**: Choose one of the following:
  - **Google Gemini** (default): Set `GEMINI_API_KEY="YOUR_ACTUAL_API_KEY"`
  - **OpenAI or Compatible**: Set `LLM_PROVIDER=openai` and `OPENAI_API_KEY="YOUR_ACTUAL_API_KEY"`
    - For custom endpoints (Ollama, Together AI, etc.): Also set `OPENAI_API_BASE="YOUR_ENDPOINT_URL"`
  1. Navigate to the `backend/` directory
  2. Copy `backend/.env.example` to `backend/.env`
  3. Configure your preferred LLM provider (see Environment Configuration section below)
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

**Environment Configuration:**

Configure your preferred LLM provider by editing `backend/.env`:

**For Google Gemini (default):**
```bash
GEMINI_API_KEY=your_gemini_api_key_here
```

**For OpenAI:**
```bash
LLM_PROVIDER=openai
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_API_BASE=https://api.openai.com/v1
QUERY_GENERATOR_MODEL=gpt-4o-mini
REFLECTION_MODEL=gpt-4o
ANSWER_MODEL=gpt-4o
```

**For OpenAI-Compatible Providers (Ollama, Together AI, etc.):**
```bash
LLM_PROVIDER=openai
OPENAI_API_KEY=your_api_key_here
OPENAI_API_BASE=http://localhost:11434/v1  # Example for Ollama
QUERY_GENERATOR_MODEL=llama3.2
REFLECTION_MODEL=llama3.2
ANSWER_MODEL=llama3.2
```

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
- LLM Provider API Key (Google Gemini or OpenAI-compatible)
- LangSmith API Key (optional, for monitoring and debugging)

**Build and Deploy:**

1. **Pull Docker Image from GitHub Container Registry:**
   ```bash
   docker pull ghcr.io/robert/freesearch:latest
   ```

2. **Build Docker Image (Alternative):**
   ```bash
   docker build -t ghcr.io/robert/freesearch:latest -f Dockerfile .
   ```

3. **Run with Docker Compose:**

   **Option 1: Google Gemini (Default):**
   ```bash
   GEMINI_API_KEY=<your_gemini_api_key> LANGSMITH_API_KEY=<your_langsmith_api_key> docker-compose up
   ```

   **Option 2: OpenAI:**
   ```bash
   # Set environment variables and run
   export LLM_PROVIDER=openai
   export OPENAI_API_KEY=<your_openai_api_key>
   export OPENAI_API_BASE=https://api.openai.com/v1
   export QUERY_GENERATOR_MODEL=gpt-4o-mini
   export REFLECTION_MODEL=gpt-4o
   export ANSWER_MODEL=gpt-4o
   export LANGSMITH_API_KEY=<your_langsmith_api_key>
   docker-compose up
   ```

   **Option 3: Ollama (Local OpenAI-Compatible):**
   ```bash
   # Set environment variables and run
   export LLM_PROVIDER=openai
   export OPENAI_API_KEY=your_key_here
   export OPENAI_API_BASE=http://host.docker.internal:11434/v1
   export QUERY_GENERATOR_MODEL=llama3.2
   export REFLECTION_MODEL=llama3.2
   export ANSWER_MODEL=llama3.2
   export LANGSMITH_API_KEY=<your_langsmith_api_key>
   docker-compose up
   ```

   **Option 4: Together AI:**
   ```bash
   # Set environment variables and run
   export LLM_PROVIDER=openai
   export OPENAI_API_KEY=<your_together_api_key>
   export OPENAI_API_BASE=https://api.together.xyz/v1
   export QUERY_GENERATOR_MODEL=meta-llama/Llama-3.2-3B-Instruct-Turbo
   export REFLECTION_MODEL=meta-llama/Llama-3.2-3B-Instruct-Turbo
   export ANSWER_MODEL=meta-llama/Llama-3.2-3B-Instruct-Turbo
   export LANGSMITH_API_KEY=<your_langsmith_api_key>
   docker-compose up
   ```

   **Option 5: Using Environment File (Recommended):**
   Create a `.env` file in the project root with your configuration:
   ```bash
   # Copy backend/.env.example to .env and configure your preferred provider
   cp backend/.env.example .env
   # Edit .env with your configuration, then run:
   docker-compose up
   ```

   **Option 6: Using --env-file Flag:**
   ```bash
   # Use a custom environment file
   docker-compose --env-file backend/.env up
   ```

**Access the Application:**
- Frontend: `http://localhost:8123/app/`
- API: `http://localhost:8123`

**Configuration Notes:**
- The Docker Compose configuration uses the GitHub Container Registry image: `ghcr.io/robert/freesearch:latest`
- The image is automatically built and pushed by GitHub Actions on every commit to the main branch
- Multi-provider environment variable support is included - all variables from [`backend/.env.example`](backend/.env.example) are available
- For custom deployments, update the `apiUrl` in [`frontend/src/App.tsx`](frontend/src/App.tsx)
- Default URLs: `http://localhost:8123` (production) or `http://localhost:2024` (development)
- When using Ollama with Docker, use `host.docker.internal` instead of `localhost` to access the host machine
- For other OpenAI-compatible providers, adjust the `OPENAI_API_BASE` URL accordingly
- All configuration options are documented in [`backend/.env.example`](backend/.env.example)
- See [LangGraph Documentation](https://langchain-ai.github.io/langgraph/concepts/deployment_options/) for advanced deployment options

## Provider Testing

The application includes a comprehensive testing script to verify LLM provider configurations. Use [`backend/test_llm_providers.py`](backend/test_llm_providers.py) to test different provider setups:

**Test Gemini Provider:**
```bash
cd backend
GEMINI_API_KEY=your_key python test_llm_providers.py
```

**Test OpenAI Provider:**
```bash
cd backend
LLM_PROVIDER=openai OPENAI_API_KEY=your_key python test_llm_providers.py
```

**Test OpenAI-Compatible Provider (e.g., Ollama):**
```bash
cd backend
LLM_PROVIDER=openai OPENAI_API_KEY=your_key OPENAI_API_BASE=http://localhost:11434/v1 python test_llm_providers.py
```

The test script validates:
- Provider configuration and authentication
- Model instantiation and basic functionality
- Factory function [`create_llm()`](backend/src/agent/graph.py#L44-L85) operation
- Configuration parameter handling

This ensures your chosen LLM provider is properly configured before running the full application.

## Technologies Used

**Frontend:**
- [React 19](https://reactjs.org/) with [TypeScript](https://www.typescriptlang.org/) - Modern React application with type safety
- [Vite](https://vitejs.dev/) - Fast build tool and development server  
- [Tailwind CSS](https://tailwindcss.com/) - Utility-first CSS framework
- [Shadcn UI](https://ui.shadcn.com/) - Reusable component library
- [LangGraph SDK](https://github.com/langchain-ai/langgraph) - Real-time streaming integration

**Backend:**
- [LangGraph](https://github.com/langchain-ai/langgraph) - Agent workflow orchestration and management
- **Multi-Provider LLM Support**:
  - [Google Gemini](https://ai.google.dev/models/gemini) - Advanced language models for legal analysis
  - [OpenAI](https://openai.com/api/) - GPT models and OpenAI-compatible endpoints
  - [LangChain OpenAI](https://python.langchain.com/docs/integrations/llms/openai) - OpenAI integration with support for custom endpoints
- [FastAPI](https://fastapi.tiangolo.com/) - High-performance Python web framework
- [Google Search API](https://developers.google.com/custom-search/v1/overview) - Enhanced web search with grounding metadata and advanced citations
- [Redis](https://redis.io/) - Pub-sub messaging and caching (production)
- [PostgreSQL](https://www.postgresql.org/) - Data persistence and state management (production)

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details.

**Note**: The backend component (`backend/`) contains an MIT license from its original development. The overall project follows the Apache License 2.0. 