import os

from dotenv import load_dotenv
from langchain_community.document_loaders import WebBaseLoader
import bs4
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.vectorstores import FAISS

load_dotenv(dotenv_path="F:\Python\llm.env")
# 初始化 WebBaseLoader

loader = WebBaseLoader(
    "https://www.gov.cn/zhengce/content/202510/content_7043916.htm",
    bs_kwargs=dict(parse_only=bs4.SoupStrainer(id='UCAP-CONTENT'))
)
docs = loader.load()
# print(docs)

# 文档分割
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)

documents = text_splitter.split_documents(docs)
# print(documents)

# 初始化 DashScope 嵌入模型
embeddings = DashScopeEmbeddings(
    dashscope_api_key=os.getenv("DASHSCOPE_API_KEY"),
    model="text-embedding-v4")

# 分批处理文档
vector = None
batch_size = 10
for i in range(0, len(documents), batch_size):
    batch_docs = documents[i:i + batch_size]
    # 第一批：创建新的 FAISS 索引
    if i == 0:
        vector = FAISS.from_documents(batch_docs, embeddings)
    else:
        new_vector = FAISS.from_documents(batch_docs, embeddings)
        # 后续批次：将新文档添加到现有索引
        vector.merge_from(new_vector)
vector.save_local("faiss_index")
print("FAISS 索引已保存到 faiss_index 文件夹")