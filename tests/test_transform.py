from extract import extract_csv
from transform import transform_data

df = extract_csv("datasets/employees.csv")

df = transform_data(df)

print(df)