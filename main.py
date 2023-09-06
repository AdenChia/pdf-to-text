# Import Libraries
import fitz
from io import StringIO
import pandas as pd
import csv

doc = fitz.open("keppel-corporation-limited-annual-report-2018.pdf")
page = doc[11]
output = ""
text = page.get_text("blocks")
text.sort(key=lambda x: x[0])
for block in text:
    if block[6] == 0:
        output += block[4].replace("\n","") + "\n"
to_list = output.split("\n")

df = pd.DataFrame(to_list)
df.columns = ['Text']
df = df['Text'].str.replace('\W', ' ', regex=True)
df.to_csv('output.csv')