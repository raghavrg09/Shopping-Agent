from langchain_core.tools import tool
from llm_model import model
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent
import tools


# creating the tools for tool calling
api_tools = [getattr(tools,i) for i in dir(tools) if i.startswith('tool')]
api_tools = [tool(i) for i in api_tools]

# setting core system prompt
system_message = """You are an agent developed by Shoppin to help customer purchase and place orders online.
Use the given tools to answer question and nothing else
"""
memory = MemorySaver()

# react agent app to call tools according to LLM understanding
app = create_react_agent(
    model, api_tools, state_modifier=system_message,
    checkpointer=memory
)
