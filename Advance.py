# advance numpy inster np.insert(array,index,value,axis=none)
import numpy as np
arr = np.array([[1,23,4,5,6,7],[2,34,5,67,77]])

insert = np.insert(arr,0,[2,3,4],axis=0)
print(insert)

# insert a 2d array
insert_2d = np.array([[1,6],[2,4]])
adds = np.insert(insert_2d,1,[1,2],axis=None)
print(adds)

# concatenate krna joine krna 2 arrays ko 

arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])

add_arr = np.concatenate((arr1,arr2))
print(add_arr)


# kisi bhi array ko delete krna ha remove krna ho elements ko
remove_ele = np.array([[1,2,34,5,6,6,7]])
delete = np.delete(remove_ele , 2)
print(delete) 

# data ko row or columns mein merge krna ha ya vertical horizental then use stacking
# vstack hstack

print(np.vstack((arr1,arr2)))
print(np.hstack((arr2,arr1)))

# broadcasting mein loops ki zarorat ni parti 
# easilly write code without using loops

# how numpy handle arrays of different shape

# matching dimension,.....mtlb same [1,2,3]+[2,3,4] same shape

# expended single elements ........[1,23,4]+[2] ....output..3,25,6

# incompatible shape .....not same array then code return errors

# is tara krty ha broadcasting one d array ka
broadC = np.array([1,24,3])

result = broadC*2

print(result)

# 2d array broadcasting
array1 = np.array([[1,2,3],[2,3,4]])
array2 = np.array([2,3])
resize = array2.reshape([1,1])
res = array1 +array2

print(res)
