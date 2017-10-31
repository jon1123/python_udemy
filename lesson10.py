import numpy as np
arr = np.arange(50).reshape((10,5))
#print(arr)
#print(arr.T)
dot_arr = np.dot(arr.T,arr)
#print(dot_arr)
arr3d = np.arange(50).reshape((5,5,2))
#print(arr3d)
#print('............')
#print(arr3d.transpose((1,2,0)))  
#change the order of the numbers to change the way it is transposed 
arr1 = np.array([1,2,3])
print(arr1)
print(arr1.swapaxes(0,1))
# swapaxwes is not working 