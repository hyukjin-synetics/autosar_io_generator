from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# OPENAI API KEY Load
load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o-mini",
)

print(llm.invoke("지구의 자전 주기는?").content)