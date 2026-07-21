# test_extract.py

from extract import extract_csv

df = extract_csv("datasets/employees.csv")

print(df.head())