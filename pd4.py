# NaN (not a number)
# none (for object datatype)

# isnull() True - nan missing ha values
# false - value is present

import pandas as pd

dataSet ={
    "Name" : ["mary","harry","charry",None,"kahlil","amir"],
    "age"  : [23,24,None,27,22,29],
    "city" : ["guj","lahr","islm",None,"guj","dhdde"],
    "salary" : [11211,421325,65657,71334,81434,81213],
}

pdff = pd.DataFrame(dataSet)
# print(pdff.isnull().sum())
# print(pdff)

# how to remove none values 
# pdff.dropna(inplace=True)
# print(pdff)

#how to refill the none value

# pdff.fillna(1,inplace=True)
# print(pdff)

# how to add value related to colm or row

pdff["age"].fillna(pdff["age"].mean(),inplace=True)
pdff["salary"].fillna(pdff["salary"].mean(),inplace=True)
print(pdff)





