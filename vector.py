from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import pandas as pd
import os



df=pd.read_csv("BangaloreZomatoData.csv")
embeddings = OllamaEmbeddings(model="nomic-embed-text")

db_location = "./chrome_langchain_db"
add_documents=not os.path.exists(db_location)

if add_documents:
    documents=[]
    ids=[]


    for i,row in df.iterrows():
        document=Document(
            page_content=str(row["Cuisines"]) + " " + str(row["PeopleKnownFor"]),
            metadata={"rating": row["Dinner Ratings"]},
            id=str(i)
        )

        ids.append(str(i))
        documents.append(document)
vector_store=Chroma(
    embedding_function=embeddings,
    collection_name="zomato_bangalore",
    persist_directory=db_location
)
if add_documents:
    vector_store.add_documents(documents=documents,ids=ids)

retriever=vector_store.as_retriever(
    search_kwargs={"k":5}
)




    
    



    