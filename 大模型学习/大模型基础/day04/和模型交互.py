import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
client = OpenAI(api_key=os.getenv("DASHSCOPE_API_KEY"), base_url=base_url)
user_prompt = input('请输入你的问题：')
response = client.chat.completions.create(
    model="qwen-plus",
    messages=[{
        'role': 'system',  # 设置模型初始化内容
        'content': '我是你的小助手，我的名字叫小智，我能够帮助您解决各种各样的问题!'},
        {'role': 'user',  # 用户提问
         'content': user_prompt}
    ],
)
print(response.choices[0].message.content)
