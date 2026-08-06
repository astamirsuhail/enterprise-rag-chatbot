from src.knowledge.document_manager import DocumentManager
from src.ingestion.pdf_loader import load_pdf
from src.ingestion.chunker import split_documents
from src.embeddings.embedder import create_embeddings
from src.database.vector_store import create_vector_store

all_chunks = []

manager = DocumentManager()

pdf_files = manager.get_all_documents()

print(f"Found {len(pdf_files)} PDF(s).")

for pdf in pdf_files:

    documents = load_pdf(str(pdf))

    chunks = split_documents(documents)

    # Add metadata to every chunk
    for chunk in chunks:
        chunk.metadata["source"] = pdf.name

    all_chunks.extend(chunks)

print(f"Total chunks: {len(all_chunks)}")

embeddings = create_embeddings()

create_vector_store(
    all_chunks,
    embeddings
)

print("Knowledge Base Ready.")