from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

model= OllamaLLM(model="llama3:latest")
template="""
You are an expert in answering questions about restaurents in bangalore
here are relevant reviews: {reviews}

here are some questions: {questions}

"""

prompt = ChatPromptTemplate.from_template(template)
chain=prompt|model
while True:
    print("\n---------------------------------------")
    question=input("Ask a question and press q to quit :  ")
    if question== "q":
        break
    print("\n---------------------------------------")
    reviews=retriever.invoke(question)
    result=chain.invoke({"reviews":reviews,"questions":question})
    print(result)
