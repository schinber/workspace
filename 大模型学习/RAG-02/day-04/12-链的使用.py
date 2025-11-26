# 导入LangChain中的提示模板
import os

from dotenv import load_dotenv
from langchain.chains.llm import LLMChain
from langchain_core.prompts import PromptTemplate
# 导入LangChain中的OpenAI模型接口
from langchain_openai import ChatOpenAI

load_dotenv(dotenv_path=r"F:\Python\llm.env")

# 原始字符串模板
template = "桌上有{number}个苹果，四个桃子和 3 本书，一共有几个水果?"

# 创建LangChain模板
prompt_temp = PromptTemplate.from_template(template)

# 根据模板创建提示
prompt = prompt_temp.format(number=2)

model = ChatOpenAI(api_key=os.getenv("DASHSCOPE_API_KEY"),
                   base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
                   model='qwen-plus',
                   temperature=0)
# 不使用chain传入提示，调用模型返回结果
# result = model.invoke(prompt)
# print(result)


# 使用chain
# 创建LLMChain
# llm_chain = LLMChain(
#     llm=model,
#     prompt=PromptTemplate.from_template(template)
# )

# # 调用LLMChain，返回结果
# result = llm_chain.invoke({"number": 2})
# print(type(result))
# print(result['text'])


# LCEL
prompt = PromptTemplate.from_template(template)
chain = prompt | model
result = chain.invoke({"number": 2})
print(result)
