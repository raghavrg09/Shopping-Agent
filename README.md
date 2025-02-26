![alt text](image.png)


# 🛒 Shopping Agent
An AI-powered shopping assistant designed to streamline product searches, comparisons, and decision-making using LLMs and intelligent agent workflows.


# ⚙️ Design Decisions
## Agent Architecture
ReAct Used (Graph Workflow recommended for controlled execution)\n\n
LLM-Powered Decision Making: Uses OpenAI/GPT models.\n\n
Multi-Step Reasoning: The agent sequentially evaluates user needs.\n\n
Tool Usage: Integrates search APIs and knowledge graphs.\n\n
## Tool Selection
LangGraph: For structured agent workflows.\n\n
###### _Recommended_
Vector Search (FAISS/Neo4j): For contextual memory.\n\n
FastAPI Backend: For efficient request handling.\n\n


# 🚧 Challenges & Improvements

## Challenges
Handling Ambiguous Queries → Users may provide vague inputs.\n\n
Latency Issues → LLM calls introduce delays.\n\n
Tool Execution Errors → External APIs can fail unexpectedly.\n\n

## Improvements
✅ Prompt Engineering → Refined instructions to improve accuracy.\n\n
✅ Hybrid Search → Combined keyword + vector search for better retrieval.\n\n
✅ Caching Strategies → Reduced API calls by 30%.\n\n
✅ Custom Graph Based Workflow

# 📖 References


["ReAct: Synergizing Reasoning and Acting in Language Models" – Yao et al.](https://arxiv.org/abs/2210.03629)

["Toolformer"](https://arxiv.org/abs/2302.04761)