
import pandas as pd
import numpy as np

df = pd.read_excel("ujass.xlsx")

X = df.to_numpy()

rows_list = []
values = []

for row in X:
    rows = ([row[3], row[2], row[4]])
    rows = (' '.join(str(row) for row in rows))
    rows_list.append(rows)
    value = row[5]
    values.append(value)

dictionary_2025 = dict(zip(rows_list, values))

for key, value in dictionary_2025.items():
    if value < 300:
      print(f"{key} : {value}")





