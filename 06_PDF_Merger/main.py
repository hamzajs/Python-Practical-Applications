# ==================== PDF MERGER CONFIGURATION ====================
# Configuration variables to modify for different usage:
# - folder_path: Change 'articles' to your PDF folder name
# - output_filename: Change 'article.pdf' to your desired output filename
# - page_skip: Currently skips first page (reader.pages[1:]), modify as needed

from pathlib import Path
import PyPDF2, os

# ==================== COLLECT PDF FILES ====================
# Get list of PDF files from the specified folder
pdf_files = []
folder_path = Path.home() / 'Desktop' / 'articles'  # Modify folder path here

for file in os.listdir(folder_path):
    full_file_path = folder_path / file
    if full_file_path.is_file() and file.endswith(".pdf"):
        pdf_files.append(file)
        print(f"A PDF file has been found: {file}")

# ==================== SORT AND PREPARE ====================
# Sort PDF files alphabetically
pdf_files.sort(key=str.lower)

# Create PDF writer object
writer = PyPDF2.PdfWriter()

# ==================== MERGE PDF PAGES ====================
# Read each PDF and merge pages (skip first page of each)
for file in pdf_files:
    with open(folder_path / file, 'rb') as file_read:
        reader = PyPDF2.PdfReader(file_read)
        total_page = len(reader.pages)

        if total_page > 1:
            for page in reader.pages[1:]:  # Skip first page
                writer.add_page(page)

# ==================== SAVE MERGED PDF ====================
# Write merged PDF to output file
with open(folder_path / 'article.pdf', "wb") as file:
    writer.write(file)

print(f"The new file has been successfully created and saved under the name: article.pdf")