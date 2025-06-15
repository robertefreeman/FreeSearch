# Deep Research Legal - AI-Powered Legal Research Tool

This project demonstrates a specialized legal research application using a React frontend and a LangGraph-powered backend agent. The agent is designed to perform comprehensive legal research on legal queries by dynamically generating legal search terms, querying authoritative legal sources, reflecting on the results to identify knowledge gaps, and iteratively refining its search until it can provide a well-supported legal analysis with proper citations. This application serves as a powerful tool for legal professionals, students, and researchers conducting thorough legal research using LangGraph and Google's Gemini models.

![Deep Research Legal](./app.png)

## Features

- ⚖️ Specialized legal research application with React frontend and LangGraph backend.
- 🧠 Powered by a LangGraph agent for advanced legal research and analysis.
- 🔍 Dynamic legal query generation using Google Gemini models with legal terminology.
- 🌐 Integrated legal research via Google Search API targeting authoritative legal sources.
- 🤔 Reflective reasoning to identify legal knowledge gaps and refine legal searches.
- 📄 Generates comprehensive legal analysis with proper legal citations.
- 🔄 Hot-reloading for both frontend and backend development during development.
- ⚖️ Legal-specific interface with research depth options (Basic, Comprehensive, Deep Analysis).
- 📚 Focuses on case law, statutes, regulations, and legal precedent research.

## Project Structure

The project is divided into two main directories:

-   `frontend/`: Contains the React application built with Vite.
-   `backend/`: Contains the LangGraph/FastAPI application, including the research agent logic.

## Getting Started: Development and Local Testing

Follow these steps to get the application running locally for development and testing.

**1. Prerequisites:**

-   Node.js and npm (or yarn/pnpm)
-   Python 3.8+
-   **`GEMINI_API_KEY`**: The backend agent requires a Google Gemini API key.
    1.  Navigate to the `backend/` directory.
    2.  Create a file named `.env` by copying the `backend/.env.example` file.
    3.  Open the `.env` file and add your Gemini API key: `GEMINI_API_KEY="YOUR_ACTUAL_API_KEY"`

**2. Install Dependencies:**

**Backend:**

```bash
cd backend
pip install .
```

**Frontend:**

```bash
cd frontend
npm install
```

**3. Run Development Servers:**

**Backend & Frontend:**

```bash
make dev
```
This will run the backend and frontend development servers.    Open your browser and navigate to the frontend development server URL (e.g., `http://localhost:5173/app`).

_Alternatively, you can run the backend and frontend development servers separately. For the backend, open a terminal in the `backend/` directory and run `langgraph dev`. The backend API will be available at `http://127.0.0.1:2024`. It will also open a browser window to the LangGraph UI. For the frontend, open a terminal in the `frontend/` directory and run `npm run dev`. The frontend will be available at `http://localhost:5173`._

## How the Backend Legal Research Agent Works (High-Level)

The core of the backend is a LangGraph agent defined in `backend/src/agent/graph.py` specialized for legal research. It follows these steps:

![Agent Flow](./agent.png)

1.  **Generate Legal Research Queries:** Based on your legal question, it generates a set of targeted legal research queries using a Gemini model with legal-specific terminology and context.
2.  **Legal Research:** For each query, it uses the Gemini model with the Google Search API to find relevant legal sources including case law, statutes, regulations, and legal commentary.
3.  **Legal Analysis & Knowledge Gap Assessment:** The agent analyzes the legal research results to determine if the information is sufficient for comprehensive legal analysis or if there are knowledge gaps. It uses a Gemini model for this legal reflection process, focusing on missing precedents, jurisdictional variations, or conflicting authorities.
4.  **Iterative Legal Research Refinement:** If gaps are found or the legal analysis is insufficient, it generates follow-up legal research queries targeting specific legal authorities, jurisdictions, or recent developments and repeats the research and reflection steps (up to a configured maximum number of loops).
5.  **Finalize Legal Analysis:** Once the legal research is deemed sufficient, the agent synthesizes the gathered legal information into a comprehensive legal analysis with proper legal citations, including case law, statutory authority, and relevant legal commentary using a Gemini model.

## Deployment

In production, the backend server serves the optimized static frontend build. LangGraph requires a Redis instance and a Postgres database. Redis is used as a pub-sub broker to enable streaming real time output from background runs. Postgres is used to store assistants, threads, runs, persist thread state and long term memory, and to manage the state of the background task queue with 'exactly once' semantics. For more details on how to deploy the backend server, take a look at the [LangGraph Documentation](https://langchain-ai.github.io/langgraph/concepts/deployment_options/). Below is an example of how to build a Docker image that includes the optimized frontend build and the backend server and run it via `docker-compose`.

_Note: For the docker-compose.yml example you need a LangSmith API key, you can get one from [LangSmith](https://smith.langchain.com/settings)._

_Note: If you are not running the docker-compose.yml example or exposing the backend server to the public internet, you update the `apiUrl` in the `frontend/src/App.tsx` file your host. Currently the `apiUrl` is set to `http://localhost:8123` for docker-compose or `http://localhost:2024` for development._

**1. Build the Docker Image:**

   Run the following command from the **project root directory**:
   ```bash
   docker build -t gemini-fullstack-langgraph -f Dockerfile .
   ```
**2. Run the Production Server:**

   ```bash
   GEMINI_API_KEY=<your_gemini_api_key> LANGSMITH_API_KEY=<your_langsmith_api_key> docker-compose up
   ```

Open your browser and navigate to `http://localhost:8123/app/` to see the application. The API will be available at `http://localhost:8123`.

## Technologies Used

- [React](https://reactjs.org/) (with [Vite](https://vitejs.dev/)) - For the legal research frontend interface.
- [Tailwind CSS](https://tailwindcss.com/) - For styling.
- [Shadcn UI](https://ui.shadcn.com/) - For components.
- [LangGraph](https://github.com/langchain-ai/langgraph) - For building the backend legal research agent.
- [Google Gemini](https://ai.google.dev/models/gemini) - LLM for legal query generation, reflection, and legal analysis synthesis.

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details. 