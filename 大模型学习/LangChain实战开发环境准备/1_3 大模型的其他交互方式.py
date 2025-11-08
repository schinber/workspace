import os

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

api_key = os.environ.get("OPENAI_API_KEY")
base_url = "https://api.openai-hk.com/v1"
llm = ChatOpenAI(model="gpt-3.5-turbo", base_url=base_url)


def stream_func():
    messages = [
        SystemMessage(content="Translate the following from English into Chinese"),
        HumanMessage(content="Hello, how are you"),
    ]

    stream = llm.stream(messages)
    for chunk in stream:
        print(chunk.content, end="\n")


def template_func():
    """
    先生成提示词
    """
    from langchain_core.prompts import ChatPromptTemplate
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", "Translate the following from English into {language}"),
        ("user", "{text}")

    ])
    prompt = prompt_template.invoke({"language": "Chinese", "text": "Hello, how are you"})
    print(prompt)

    llm = ChatOpenAI(model="gpt-3.5-turbo", base_url=base_url)
    response = llm.invoke(prompt)
    print(response.content)


if __name__ == '__main__':
    # stream_func()
    template_func()


