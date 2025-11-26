from langchain_community.embeddings import DashScopeEmbeddings
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path="F:\Python\llm.env")

# embeddings_model = DashScopeEmbeddings(dashscope_api_key=os.getenv('DASHSCOPE_API_KEY'))
# embeddings = embeddings_model.embed_documents(
#     [
#         "Hi there!",
#         "Oh, hello!",
#         "What's your name?",
#         "My friends call me World",
#         "Hello World!"
#     ]
# )
# print(len(embeddings), len(embeddings[0]), len(embeddings[1]))
# ##运行结果 (5, 1536)


#  句子向量 embed_query


embeddings_model = DashScopeEmbeddings(dashscope_api_key=os.getenv('DASHSCOPE_API_KEY'))

embedded_query = embeddings_model.embed_query("What was the name mentioned in the conversation?")
print(embedded_query[:5])