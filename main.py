# Import Libraries
import fitz
from io import StringIO
import pandas as pd
import csv

# Variables
output = ""

# Read PDF
doc = fitz.open("keppel-corporation-limited-annual-report-2018.pdf")
page = doc[11]

text = page.get_text("blocks")
text.sort(key=lambda x: x[0])  # Sort x-axis to read from left to right of the PDF
for block in text:
    if block[6] == 0:
        output += block[4].replace("\n","") + "\n"  # Divide into paragraphs
to_list = output.split("\n")  # Convert the string into a list

# DataFrame
df = pd.DataFrame(to_list)
df.columns = ['Text']
df = df['Text'].str.replace('\W', ' ', regex=True)  # Remove special characters
df.to_csv('output.csv')