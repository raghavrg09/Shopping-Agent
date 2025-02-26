from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
from pydantic import SecretStr

load_dotenv()


# model = ChatOpenAI(
#     model=str(os.getenv("OPENAI_MODEL")),  # type : ignore[arg-type]
#     base_url=os.getenv("BASE_URL"),
#     temperature=0.0,
#     api_key=SecretStr(str(os.environ.get("OPENAI_API_KEY"))),  # type : ignore[arg-type]
# )

# initialising langchain chat model for tool calling
model = ChatOpenAI(
    model="gpt-4o",
    temperature=0.0,
    api_key=SecretStr(str(os.environ.get("OPENAI_API_KEY")))
)
