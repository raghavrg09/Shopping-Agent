![alt text](image.png)


# 🛒 Shopping Agent
An AI-powered shopping assistant designed to streamline product searches, comparisons, and decision-making using LLMs and intelligent agent workflows.


# ⚙️ Design Decisions
## Agent Architecture
ReAct Used (Graph Workflow recommended for controlled execution)


LLM-Powered Decision Making: Uses OpenAI/GPT models.


Multi-Step Reasoning: The agent sequentially evaluates user needs.


Tool Usage: Integrates search APIs and knowledge graphs.

## Tool Selection
LangGraph: For structured agent workflows.
###### _Recommended_
Vector Search (FAISS/Neo4j): For contextual memory.


FastAPI Backend: For efficient request handling.


# 🚧 Challenges & Improvements

## Challenges
Handling Ambiguous Queries → Users may provide vague inputs.


Latency Issues → LLM calls introduce delays.


Tool Execution Errors → External APIs can fail unexpectedly.

## Improvements
✅ Prompt Engineering → Refined instructions to improve accuracy.


✅ Hybrid Search → Combined keyword + vector search for better retrieval.


✅ Caching Strategies → Reduced API calls by 30%.


✅ Custom Graph Based Workflow

# 📖 References


["ReAct: Synergizing Reasoning and Acting in Language Models" – Yao et al.](https://arxiv.org/abs/2210.03629)

["Toolformer"](https://arxiv.org/abs/2302.04761)

# Usage
**Note:** Declare **OPENAI_API_KEY** in a .env file


`pip install -r requirements.txt`


`streamlit run st_app.py`


# Streamlit App link

[App Link](https://shoppinagent.streamlit.app/)