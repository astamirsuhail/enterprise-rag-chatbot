from src.ingestion.pdf_loader import load_pdf
from src.ingestion.chunker import split_documents
from src.embeddings.embedder import create_embeddings
from src.database.vector_store import create_vector_store

# Load PDF
docs = load_pdf(
    "data/input/Business Travel Policy-report-2025-volkswagen-group.pdf"
)

# Split into chunks
chunks = split_documents(docs)

# Create embedding model
embeddings = create_embeddings()

# Create vector database
db = create_vector_store(chunks, embeddings)