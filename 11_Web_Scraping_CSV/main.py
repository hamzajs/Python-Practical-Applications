"""
Scrape a specific Wikipedia table and export it to CSV.

This script loads the Wikipedia page that lists languages by number of native speakers,
locates the table whose caption contains 'CIA', extracts its columns and rows, and
stores the data in a CSV file on the desktop.
"""

import csv
from pathlib import Path

import bs4
import requests

# Target webpage containing the language statistics table.
URL = "https://en.wikipedia.org/wiki/List_of_languages_by_number_of_native_speakers"

# Use a custom User-Agent header to reduce the chance of being blocked while scraping.
HEADER = {
    "User-Agent": "MyScraperBot/1.0 (your_email@gmail.com)"
}

# Send an HTTP GET request to the target page.
response = requests.get(URL, headers=HEADER)

# Parse the HTML content using BeautifulSoup for structured data extraction.
soup = bs4.BeautifulSoup(response.text, "html.parser")

# Inspect all tables on the page and select the one whose caption mentions "CIA".
tables = soup.find_all("table")
required_table = None

for table in tables:
    caption = table.find("caption")

    if caption is not None:
        if "CIA" in caption.get_text():
            required_table = table
            break

# If the target table is not found, stop the script and notify the user.
if required_table is None:
    print("The table you were looking for could not be found on this page.")
    exit()

# Extract the rows from the selected table.
rows = required_table.find_all("tr")

# Read the header cells and clean the text for use as CSV column names.
columns = rows[0].find_all("th")
headers = [column.get_text(separator=' ', strip=True) for column in columns]

# Store each data row in a list after removing extra whitespace and line breaks.
data = []
for row in rows[1:]:
    td_cells = row.find_all("td")
    cells = [cell.get_text(separator=' ', strip=True) for cell in td_cells]
    data.append(cells)

# Save the extracted records to a CSV file on the Desktop.
with open(Path.home() / Path('Desktop', 'Table_wikipedia.csv'), 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(data)
