import pandas as pd

NUM_ROWS = 5000

departments = ["IT", "HR", "Finance", "Sales", "Marketing"]

data = []

for i in range(1, NUM_ROWS + 1):
    data.append(
        {
            "employee_code": f"EMP{i:03d}",
            "name": f"Employee_{i}",
            "department": departments[(i - 1) % len(departments)],
            "salary": 40000 + ((i - 1) % 20) * 1000,
        }
    )

df = pd.DataFrame(data)

df.to_csv("datasets/employees_5000.csv", index=False)

print(f"Generated {NUM_ROWS} records successfully.")
