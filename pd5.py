# sorting AND aggregation

# sort the values mean arrange the values e.g if data like this [2,4,1,5,3] after sorting [1,2,3,4,5] that is called sorting
# method df.[by="colm_name",acsending = true/false ,inplace = true]

import pandas as pd

dataSet ={
    "Name" : ["mary","harry","charry",None,"kahlil","amir"],
    "age"  : [23,24,25,27,22,29],
    "city" : ["guj","lahr","islm",None,"guj","dhdde"],
    "salary" : [1,5,6,4,2,3],
}

sort = pd.DataFrame(dataSet)
sort.sort_values(by=["age","salary"], ascending=[True,False], inplace=True)

# aggregation invlove caluclate values sum ,mean ,std, min, max, .....>

# syntax df["col_name"].mean()

mean = sort["age"].min()
print(mean)