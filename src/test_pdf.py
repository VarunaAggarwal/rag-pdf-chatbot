from pdf_loader import load_pdf


pdf_path = "../data/documents/flood_modelling.pdf"

text = load_pdf(pdf_path)

print("=" * 60)
print("PDF TEXT EXTRACTION")
print("=" * 60)

print(f"Total characters: {len(text)}")

print("\nFirst 3000 characters:\n")

print(text[:3000])