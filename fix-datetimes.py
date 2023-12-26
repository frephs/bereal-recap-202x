import os
import re
from datetime import datetime

# Function to extract date from the filename
def extract_date(filename):
    match = re.search(r'(\w+ \d+, \d+).png', filename)
    if match:
        return match.group(1)
    return None

# Get all PNG files in the current directory
png_files = [file for file in os.listdir('.') if file.endswith('.png')]

# Iterate through PNG files and set modification time
for file in png_files:
    date_str = extract_date(file)
    if date_str:
        date_obj = datetime.strptime(date_str, '%B %d, %Y')
        timestamp = date_obj.timestamp()
        os.utime(file, (timestamp, timestamp))
        # now also rename the file
        # Rename the file with the datetime yyyymmdd.png format
        new_filename = date_obj.strftime('%Y%m%d') + '.png'
        os.rename(file, new_filename)


