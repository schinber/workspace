import os

from dotenv import load_dotenv
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv(dotenv_path="F:\Python\llm.env")

embeddings = DashScopeEmbeddings(
    dashscope_api_key=os.getenv("DASHSCOPE_API_KEY"),
    model="text-embedding-v4")

# 加载本地FAISS
save_path = "faiss_index"

vector_store = FAISS.load_local(
    folder_path=save_path,
    embeddings=embeddings,
    allow_dangerous_deserialization=True  # 允许加载 pickle 文件（仅限可信文件）
)

# 创建提示词模板

prompt = ChatPromptTemplate.from_template("""仅根据提供的上下文回答以下问题:

<context>
{context}
</context>

问题: {input}""")

# 创建 LLM 连接（继续使用阿里云 qwen-plus）
llm = ChatOpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),  # 确保环境变量名为 DASHSCOPE_API_KEY
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    model="qwen-plus"
)

# 创建文档组合链
document_chain = create_stuff_documents_chain(llm, prompt)

# 创建检索器
retriever = vector_store.as_retriever(search_kwargs={"k": 3})

# 创建检索链
# 在langchain_community\vectorstores\faiss.py 可以查看向量检索的实现
retriever_chain = create_retrieval_chain(retriever, document_chain)

# 调用检索链并获取回答
# openai\resources\chat\completions\completions.py
# create方法中 self._post()  调用模型请求的api

response = retriever_chain.invoke({"input": "建设用地使用权是什么？"})

print("\n回答:", response["answer"])
