from langchain_openai import ChatOpenAI
from langchain_classic.memory import ConversationBufferMemory
from langchain_classic.chains import ConversationChain
from decouple import config

api_key = config("OPENAI_API_KEY")

llm = ChatOpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1",
    model="deepseek/deepseek-chat"
)

memory = ConversationBufferMemory()

conversation = ConversationChain(
    llm=llm,
    memory=memory
)

def ask_llm(question):
    response = conversation.predict(input=question)
    return response