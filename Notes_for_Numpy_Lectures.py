
# coding: utf-8

# # Notes_for_Numpy_Lectures
# #############################################

# # Creating_Arrays

# In[2]:

import numpy as np


# In[3]:

my_list1 = [1,2,3,4]


# In[4]:

my_array1 = np.array(my_list1)


# In[5]:

my_array1


# In[6]:

my_list2 = [11,22,33,44]


# In[8]:

my_lists = [my_list1 , my_list2]


# In[9]:

my_array2 = np.array(my_lists)


# In[10]:

my_array2


# In[11]:

my_array2.shape


# In[12]:

my_array2.dtype


# In[15]:

my_zeros_array = np.zeros(5)


# In[16]:

my_zeros_array.dtype


# In[17]:

my_zeros_array


# In[18]:

np.ones([5,5])


# In[25]:

np.empty(5) #np.empty([5,5]) to get it square


# In[20]:

np.eye(5)


# In[22]:

np.arange(5)


# In[23]:

np.arange(5,50,2)


# # Using_Arrays_and_Scalars

# In[26]:

5/2


# In[28]:

5//2 # truncations 


# In[29]:

arr1 = np.array([[1,2,3,4],[8,9,10,11]])


# In[30]:

arr1


# In[32]:

arr1 * arr1 # multipyby location one to one


# In[36]:

arr1- arr1 # subtract or add value by value 


# In[37]:

1/ arr1 # givingus the invers ofeach value or arr1**(-1)


# In[38]:

arr1 ** 3


# # Indexing_Arrays

# In[39]:

arr = np.arange(0,11)


# In[41]:

arr


# In[42]:

arr[8]


# In[43]:

arr[1:5]


# In[44]:

arr[0:5]


# In[45]:

arr[0:5] = 100


# In[46]:

arr


# In[47]:

arr = np.arange(0,11)


# In[48]:

slice_of_arr = arr[0:6]
slice_of_arr


# In[50]:

slice_of_arr[:] = 99
slice_of_arr


# In[51]:

arr


# In[52]:

arr_copy = arr.copy()
arr_copy


# In[53]:

arr_2d = np.array(([5,10,15],[20,25,30],[35,40,45]))
arr_2d


# In[54]:

arr_2d[1]


# In[55]:

arr_2d[1][0]


# In[56]:

arr_2d


# In[60]:

arr_2d[:2,1:]


# In[63]:

arr2d = np.zeros([10,10])
arr2d


# In[65]:

arr_lenght = arr2d.shape[1]
arr_lenght


# In[66]:

for i in range(arr_lenght):
    arr2d[i] = 1


# In[67]:

arr2d


# In[68]:

for i in range(arr_lenght):
    arr2d[i] = i
arr2d


# In[69]:

arr2d[[2,4,6,8]]


# In[70]:

arr2d[[6,4,2,7]]


# # Array_Transposition

# In[72]:

arr = np.arange(50).reshape((10,5))
arr


# In[73]:

arr.T


# In[74]:

arr


# In[75]:

np.dot(arr.T,arr)


# In[76]:

arr3d = np.arange(50).reshape(5,5,2)
arr3d


# In[77]:

arr3d.transpose(1,0,2)


# In[83]:

arr = np.array([[1,2,3]])
arr


# In[84]:

arr.swapaxes(0,1)


# # Universal_Array_Functions

# In[87]:

arr= np.arange(11)
arr


# In[88]:

np.sqrt(arr)


# In[89]:

np.exp(arr)


# In[90]:

A = np.random.randn(10)
A


# In[91]:

B = np.random.randn(10)
B


# In[92]:

# Binary Functions
np.add(A,B)


# In[93]:

np.maximum(A,B)


# In[94]:

np.minimum(A,B)


# In[95]:

webpage = 'http://docs.scipy.org/doc/numpy/reference/ufuncs.html#available-ufuncs'
import webbrowser
webbrowser.open(webpage)


# # Array_Processing

# In[96]:

import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')


# In[98]:

points =np.arange(-5,5,0.1)


# In[99]:

dx,dy = np.meshgrid(points,points)


# In[100]:

dx


# In[101]:

dy


# In[102]:

z = (np.sin(dx) + np.sin(dy))
z


# In[103]:

plt.imshow(z)


# In[104]:

plt.imshow(z)
plt.colorbar()
plt.title('Plotfor sinx+sin(y)')


# In[105]:

# numpy where 

A = np.array([1,2,3,4])
B = np.array([100,200,300,400])


# In[106]:

condition = np.array([True,True,False,False])


# In[107]:

answer= [(A_val if cond else B_val) for A_val,B_val,cond in zip(A,B,condition)]


# In[108]:

answer


# In[109]:

answer2 = np.where(condition,A,B)
answer2


# In[110]:

from numpy.random import randn


# In[111]:

arr = randn(5,5)
arr


# In[113]:

np.where(arr<0,0,arr)


# In[114]:

arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
arr


# In[115]:

arr.sum()


# In[116]:

arr.sum(0)


# In[117]:

arr.mean()


# In[118]:

arr.std()


# In[119]:

arr.var()


# In[120]:

bool_arr = np.array([True,False,True])
bool_arr


# In[121]:

bool_arr.any()


# In[122]:

bool_arr.all()


# In[126]:

# Sort 
arr = randn(5)
arr


# In[127]:

arr.sort()
arr


# In[129]:

countries = np.array(['France','Germany','USA','Russia','USA','Mexico','Germany'])


# In[130]:

np.unique(countries)


# In[132]:

np.in1d(['France','USA','Sweden'],countries)


# # Array_Input_Output 

# In[134]:

arr = np.arange(5)
arr


# In[135]:

np.save('myarray',arr)


# In[136]:

arr = np.arange(10)
arr


# In[141]:

np.load('myarray.npy')


# In[142]:

arr1 = np.load('myarray.npy')
arr1


# In[143]:

arr2 = arr
arr2


# In[144]:

np.savez('ziparray.npz',x=arr1,y=arr2)


# In[145]:

archive_array = np.load('ziparray.npz')


# In[146]:

archive_array['x']


# In[147]:

archive_array['y']


# In[148]:

arr = np.array([[1,2,3],[4,5,6]])
arr


# In[150]:

np.savetxt('mytextarray.txt',arr,delimiter=',')


# In[152]:

arr = np.loadtxt('mytextarray.txt',delimiter = ',')


# In[153]:

arr


# In[ ]:



