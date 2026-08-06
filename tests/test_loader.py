from src.ingestion.pdf_loader import load_pdf
from src.ingestion.chunker import split_documents


docs = load_pdf(
    "data/input/Business Travel Policy-report-2025-volkswagen-group.pdf"
)

chunks = split_documents(docs)

print("\n")

print(chunks[0].page_content)