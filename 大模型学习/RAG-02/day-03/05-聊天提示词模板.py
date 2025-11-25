import os

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

template = "你是一个数学家，你可以计算任何算式"
# template = "你是一个翻译专家,擅长将 {input_language} 语言翻译成 {output_language}语言."
human_template = "{text}"

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", template),
    ("human", human_template),
])
# print(chat_prompt)


# 创建模型实例
# 创建 LLM 连接（继续使用阿里云 qwen-plus）
llm = ChatOpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),  # 确保环境变量名为 DASHSCOPE_API_KEY
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    model="qwen-plus"
)
# 输入提示
messages = chat_prompt.format_messages(text="我今年18岁，我的舅舅今年38岁，我的爷爷今年72岁，我和舅舅一共多少岁了？")
# print(messages)
# messages = chat_prompt.format_messages(input_language="英文", output_language="中文", text="I love Large Language Model.")
print(messages)
# 得到模型的输出
output = llm.invoke(messages)
# 打印输出内容
print(output.content)
