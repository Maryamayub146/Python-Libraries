import numpy as np
# one d array one dimensional arrays
Array = np.array([1,23,4,5,5,6])
print(Array)

# multi dimensional arrays
# matrix

arr_full = np.full((3,3),7)
print(arr_full)

# range function(start,stop,step)
range = np.arange(0,20,2)
print(range)

# creating identity matrices

identity_mtrix = np.eye(1)
print(identity_mtrix)

# shape in array
arr_shape = np.array([[1,23,4,4],
                     [2,34,5,6],
                     [2,35,6,7,8]])
print(arr_shape.shape)
# total number of elements in arrays
print(arr_shape.size)
# number of dimensional ndim
print(arr_shape.ndim)
# dytype check data types
data_type = np.array([2,3,4,5])
print(data_type.dtype)


# aggregation functions
func = np.array([10,20,30])
print(np.mean(func))
print(np.min(func))
print(np.max(func))
print(np.sum(func))

# reshape (rows or clumns ko change krna specify new shape if dimension match)
shap = np.array([1,2,3,4,5,6])
Reshape = shap.reshape(2,3),
print(Reshape)