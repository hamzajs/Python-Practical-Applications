# Simple Word to PDF conversion script.
# It sets the source file path, converts the document, and saves a PDF output.

from docx2pdf import convert
from pathlib import Path

# Define the source Word document and destination PDF file paths
input_file = Path.home() / 'Desktop' / 'xx.docx'
output_file = Path.home() / 'Desktop' / 'xx_pdf.pdf'

# Convert the Word document to PDF using docx2pdf
convert(str(input_file), str(output_file))

# Example: convert a single file in the current folder
# convert('my_file.docx')

# Example: convert all Word files in a folder to PDF
# convert('my_documents_folder/')