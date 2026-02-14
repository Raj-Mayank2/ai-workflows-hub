from ingestion.pdf_loader import load_pdf

text = load_pdf("data/uploads/sample.pdf")
print(text[:500])
