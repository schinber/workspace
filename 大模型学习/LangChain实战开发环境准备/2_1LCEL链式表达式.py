from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

api_key = os.environ.get("OPENAI_API_KEY")

# 提示词
prompt_template = ChatPromptTemplate.from_messages([
    ("system", "Translate the following from English into {language}"),
    ("user", "{text}")
])

#