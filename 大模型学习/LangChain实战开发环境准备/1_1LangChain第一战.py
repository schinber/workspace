import os
from langchain_core.messages import HumanMessage, SystemMessage
from langchain.chat_models import init_chat_model

api_key = os.environ.get("OPENAI_API_KEY")

# gpt-4o-mini
model = init_chat_model("gpt-4o-mini", model_provider="openai", base_url="https://api.openai-hk.com/v1")


messages = [
    SystemMessage(content="Translate the following from English into Chinese"),
    HumanMessage(content="Hello, how are you"),
]

print(model.invoke(messages))
