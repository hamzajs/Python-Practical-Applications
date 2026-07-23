# Simple converter: turn a PDF file into a Word document
# This script loads the PDF, converts the selected pages, and saves the result.

from pathlib import Path
from pdf2docx import Converter

# Set the input PDF file path
pdf_file = Path.home() / 'Desktop' / 'articles' / 'article.pdf'
# Set the output Word file path
word_file = Path.home() / 'Desktop' / 'articles' / 'article_converted.docx'

# Load the PDF file into the converter
conv = Converter(pdf_file)
# Convert the PDF pages to a Word document
conv.convert(word_file, start=0, end=6)
# Close the converter to release resources
conv.close()