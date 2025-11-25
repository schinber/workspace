from langchain_openai import ChatOpenAI

from langchain_core.prompts import PromptTemplate
import os

# 创建模型实例
# 创建 LLM 连接（继续使用阿里云 qwen-plus）
llm = ChatOpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),  # 确保环境变量名为 DASHSCOPE_API_KEY
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    model="qwen-plus"
)

prompt = PromptTemplate(
    template="您是一位专业的程序员。\n对于信息 {text} 进行简短描述"
)

# 输入提示
input = prompt.format(text="大模型langchain")

# 得到模型的输出
output = llm.invoke(input)
# output = llm.invoke("您是一位专业的程序员。对于信息 langchain 进行简短描述")

# 打印输出内容
print(output.content)
