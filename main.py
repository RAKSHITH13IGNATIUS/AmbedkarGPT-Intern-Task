import sys

# Import necessary LangChain components [cite: 48-55]
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA

def main():
    # 1. Load the provided text file (speech.txt) [cite: 8]
    try:
        loader = TextLoader("./speech.txt")
        documents = loader.load()
        print("✅ Text loaded successfully.")
    except Exception as e:
        print(f"Error loading file: {e}")
        sys.exit()

    # 2. Split the text into manageable chunks [cite: 9]
    # Using chunk_size=500 to ensure small paragraphs are captured
    text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    texts = text_splitter.split_documents(documents)
    print(f"✅ Text split into {len(texts)} chunks.")

    # 3. Create Embeddings and store them in a local vector store [cite: 10, 16]
    # Using sentence-transformers/all-MiniLM-L6-v2 as requested 
    print("⏳ Creating embeddings and vector store (this may take a moment)...")
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    
    # Create Chroma vector store from documents
    db = Chroma.from_documents(texts, embeddings)
    print("✅ Vector store created.")

    # 4. Initialize the LLM (Ollama with Mistral) [cite: 18, 54]
    llm = Ollama(model="mistral")

    # 5. Create the Retrieval Chain [cite: 15, 55]
    # This automatically retrieves relevant chunks and feeds them to the LLM
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=db.as_retriever(search_kwargs={"k": 2}) # Retrieve top 2 relevant chunks
    )

    print("\n--- AmbedkarGPT Initialized ---")
    print("Type 'exit' to quit.\n")

    # Interactive Loop
    while True:
        user_query = input("Ask a question about the speech: ")
        
        if user_query.lower() in ['exit', 'quit']:
            break

        # 5. Generate answer [cite: 12]
        try:
            response = qa_chain.invoke(user_query)
            print(f"\nAnswer: {response['result']}\n")
        except Exception as e:
            print(f"Error generating response: {e}")

if __name__ == "__main__":
    main()