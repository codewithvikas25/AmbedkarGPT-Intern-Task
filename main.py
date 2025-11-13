from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.llms import Ollama
from langchain.chains import RetrievalQA

def main():
    print("🚀 AmbedkarGPT Q&A System")
    print("-----------------------------")

    loader = TextLoader("speech.txt")
    documents = loader.load()

    text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = text_splitter.split_documents(documents)

    print("Creating local embeddings...")
    embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectordb = Chroma.from_documents(docs, embedding, persist_directory="db")
    vectordb.persist()
    print("✅ Embeddings stored locally.")

    llm = Ollama(model="mistral")

    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectordb.as_retriever(search_kwargs={"k": 2}),
        return_source_documents=True
    )

    print("\n💬 Ask questions about Dr. B.R. Ambedkar's speech. Type 'exit' to quit.\n")
    while True:
        query = input("You: ")
        if query.lower() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break
        result = qa({"query": query})
        print(f"\nAmbedkarGPT: {result['result']}\n")

if __name__ == "__main__":
    main()
