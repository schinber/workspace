from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os

load_dotenv(dotenv_path="F:\Python\llm.env")
llm = ChatOpenAI(api_key=os.getenv("DASHSCOPE_API_KEY"),
                 base_url=os.getenv("DASHSCOPE_BASE_URL"),
                 model_name="qwen-plus")

# 直接提供问题，并调用llm
response = llm.invoke("什么是大模型？")
print(response)
print("=" * 50)
print(response.content)
