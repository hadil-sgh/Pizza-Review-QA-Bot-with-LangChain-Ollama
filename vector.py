from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import pandas as pd

df = pd.read_csv("realistic_restaurant_reviews.csv")
embeddings = OllamaEmbeddings(model="mxbai-embed-large")

# ? A place to store the vector database
db_location = "chroma_langchain_db"
add_documents =  not os.path.exists(db_location) # to granite that we don't overwrite the database if it already exists

if add_documents: 
    Documents = []
    ids = []
    for i, row in df.iterrows():
        # ?Create a Document object for each review
        doc = Document(
            page_content=row["Title"] +"²" + row["Review"],
            metadata={"rating": row["Rating"], "date": row["Date"]},
            id = str(i)
        )
        ids.append(str(i))
        Documents.append(doc)
        
        
vector_store = Chroma(
    collection_name="restaurant_reviews",
    persist_directory=db_location,
    embedding_function=embeddings,
)       
        
        
if add_documents:
    #? Add the documents to the vector store
    vector_store.add_documents(documents= Documents, ids=ids)
    # Persist the database to disk
  
        
  
# ? Load the vector store from disk      
retriever = vector_store.as_retriever(
    search_kwargs={"k": 10} # Number of documents / reviews to retrieve 
    )        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        