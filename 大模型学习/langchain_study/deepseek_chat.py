import os

from langchain_deepseek import ChatDeepSeek

llm = ChatDeepSeek(
    model="deepseek-chat",
)

llm.invoke("What is the meaning of life?")