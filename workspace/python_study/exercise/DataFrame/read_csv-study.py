"""
read csv exercise
"""
csv_path = r"F:\Python\workspace\study\python3\csv\info.csv"

import pandas as pd

data = pd.read_csv(csv_path)
data = pd.read_csv(csv_path, dtype='double')
print(data)
