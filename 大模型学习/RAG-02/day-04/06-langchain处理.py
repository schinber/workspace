from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(r"财务管理文档.pdf")
pages = loader.load_and_split()

print(f"第0页：\n{pages[0]}")  ## 也可通过 pages[0].page_content只获取本页内容