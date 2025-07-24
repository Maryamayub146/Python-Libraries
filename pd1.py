import pandas as pd

# pd = pd.read_csv("/Users/maryamayub/Downloads/python/sales_data_sample.csv", encoding="latin1")

# print("frist 5 rows display")
# print(pd.head(5))
# print("last 5 rows display")
# print(pd.tail(5))

# how data store after data manipulation
data ={
    "Name" : ["mary","harry","charry","abc","kahlil","amir"],
    "age"  : [3,4,5,7,2,9],
    "city" : ["guj","lahr","islm","lhr","guj","dhdde"],
    "salary" : [111,232,434,334,434,213],
}

df = pd.DataFrame(data)
print(df.info())
print("descriptive statistics")
print(df.describe())
print(f'shape:{df.shape}')

multple_cond = df[(df['age']>5) & (df["salary"]>200)]
print(multple_cond)

print(df.describe())
print(df["age"]>5)

sort_val = df.sort_values(by="age",ascending=True)
print(sort_val)


# .<....csv mein file save
# df.to_csv("output.csv",index=False)

# df.to_excel("output.xlsx",index=False) 

# df.to_json("out.json",index=False)