import streamlit as st
from src.retrieval.retriever import Retriever
from src.llm.model_config import Model

st.title("Senegal Policy Bot")

query = st.text_input("Posez une question sur les politiques publiques sénégalaises")

if query:
    retriever = Retriever(db_path="data/vector_store/chroma_db")
    documents = retriever.retrieve_documents(query)
    context = "\n".join(documents)
    
    response = Model.generate_response(f"Contexte : {context}\n Question : {query}")
    
    st.write(response)
