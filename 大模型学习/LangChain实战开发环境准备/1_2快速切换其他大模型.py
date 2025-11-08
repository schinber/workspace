import os

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from langchain_deepseek import ChatDeepSeek

api_key = os.environ.get("OPENAI_API_KEY")
base_url = "https://api.openai-hk.com/v1"
# llm = ChatOpenAI(model="gpt-3.5-turbo", base_url=base_url)
llm = ChatDeepSeek(model="deepseek-chat")

messages = [
    SystemMessage(content="Translate the following from English into Chinese"),
    HumanMessage(content="Hello, how are you"),
]

print(llm.invoke(messages))


