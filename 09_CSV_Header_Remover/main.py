# CSV Header Remover: Removes the first row (header) from all CSV files in a folder.
# This script iterates through CSV files, reads the data, removes the header row, and saves the updated file.

import csv, os
from pathlib import Path

# Define the folder containing CSV files to process
folder_path = Path.home() / 'Desktop' / 'employees'

try:
    # Loop through all files in the specified folder
    for file in os.listdir(folder_path):
        full_file_path = folder_path / file
        # Check if the file is a CSV file
        if full_file_path.is_file() and file.endswith(".csv"):
            print(f"A CSV file has been found: {file}")
            # Read the CSV file
            with open(full_file_path, 'r') as file1:
                reader = csv.reader(file1)
                data = list(reader)
                # Remove the first row (header)
                data.pop(0)
            # Write the data back to the file without the header
            with open(full_file_path, 'w', newline='') as file2:
                writer = csv.writer(file2)
                for row in data:
                    writer.writerow(row)
except FileNotFoundError:
    print("The Folder Is Not Found!")