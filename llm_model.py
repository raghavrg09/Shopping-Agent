from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
from pydantic import SecretStr

load_dotenv()


model = ChatOpenAI(
    model=str(os.getenv("OPENAI_MODEL")),  # type : ignore[arg-type]
    base_url=os.getenv("BASE_URL"),
    temperature=0.0,
    api_key=SecretStr(str(os.getenv("OPENAI_API_KEY"))),  # type : ignore[arg-type]
)
