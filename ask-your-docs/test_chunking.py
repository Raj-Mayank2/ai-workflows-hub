from ingestion.pdf_loader import load_pdf
from ingestion.chunker import chunk_text

text = load_pdf("data/uploads/sample.pdf")
chunks = chunk_text(text)

print(f"Total chunks: {len(chunks)}\n")
print("First chunk:\n", chunks[0][:300])
