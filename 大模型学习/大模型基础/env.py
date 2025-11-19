import os

from dotenv import load_dotenv
from openai import OpenAI

client = OpenAI(api_key=os.getenv("DASHSCOPE_API_KEY"),
                base_url=os.getenv("DASHSCOPE_BASE_URL"))


def run_env():
    load_dotenv(dotenv_path="F:\Python\llm.env")


run_env()
