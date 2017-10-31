#Creat an array
import numpy as np

my_list1 = [1,2,3,4]
my_array1 = np.array(my_list1)
print my_array1
my_list2 = [11,22,33,44]
my_lists = [my_list1, my_list2]
my_array2 = np.array(my_lists)
print my_array2 
print 'my array is a ',my_array2.shape
print 'my array is a ',my_array2.dtype

# zeros, ones, empty can all be single or multy demetional 
arrayZ = np.zeros([5,4])
print arrayZ, "it's data type is", arrayZ.dtype
print "and it is a ", arrayZ.shape

my_ones_array = np.ones([2,2]) 
print my_ones_array

my_empty_array = np.empty(3)
print my_empty_array

#identiy array 
my_eye_array = np.eye(5)
print my_eye_array

# I can arange an array 
my_aranged_array1 = np.arange(5)
my_aranged_array2 = np.arange(5,20,2)
my_ara_arr = np.arange(5,10,2)
print my_aranged_array1
print my_aranged_array2
print my_ara_arr