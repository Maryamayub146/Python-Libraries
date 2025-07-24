import pandas as pd

data = pd.read_csv("/Users/maryamayub/Downloads/python/sales_data_sample.csv",encoding="latin1")
print(data)
print("how many rows or columns in this datase")
print(data.info())
df = pd.DataFrame(data)
# print(data.head(10))
# print(data.describe())
# specific_rwo = data.iloc[24]
# print(specific_rwo)
# apply_cond = df[(df['ORDERNUMBER']>10150) & (df["QUANTITYORDERED "]>40)]
# print(apply_cond)