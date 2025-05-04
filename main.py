from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

model = OllamaLLM(model="llama3.2")

template = """
You are an Expert in answering questions about a Pizza restaurant.
Here are some relevant reviews: {reviews}
Here is a question: {question}
"""
prompt = ChatPromptTemplate.from_template(template)
# ? A chain of actions : we feed the prompt the reviews and question, get's passed to the model, and the model returns an answer.
chain = prompt | model

while True:
    print("-" * 20)
    question = input("Enter a question(q to quit): ")
    print("-" * 20)
    if question == "q":
        break    
    reviews = retriever.invoke(question)
    result = chain.invoke({"reviews" :[],"question" : question })

    print(result)
    
