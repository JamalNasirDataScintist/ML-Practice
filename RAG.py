import os

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_core.runnables import RunnablePassthrough
from langchain.prompts import PromptTemplate


# 1. Load PDF
loader = PyPDFLoader("myfile.pdf")
docs = loader.load()

# 2. Split PDF
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
chunks = splitter.split_documents(docs)

# 3. Embeddings (new LangChain package)
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# 4. Build FAISS vectorstore
vector_store = FAISS.from_documents(chunks, embeddings)
retriever = vector_store.as_retriever(search_kwargs={"k": 3})

# 5. Groq LLM
llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model="llama-3.1-8b-instant"
)

# 6. Prompt template
prompt = PromptTemplate(
    input_variables=["context", "question"],
    template="""
You are a helpful AI assistant. Answer the question strictly using the provided context.

Context:
{context}

Question:
{question}

Answer:
"""
)

# 7. Build RAG Chain (LCEL replaces RetrievalQA)
rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
)

print("Your PDF was loaded successfully!")

# 8. Chat loop
while True:
    query = input("you: ")

    if query.lower() in ["exit", "quit"]:
        break

    answer = rag_chain.invoke(query)

    print("\nAnswer:\n")
    print(answer)
