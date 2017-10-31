#Universal Array Functions 
import numpy as np
arr = np.arange(11)
print(arr)
print('....')
squ = np.sqrt(arr)
print(squ)
print('....')
ex = np.exp(arr)
print(ex)
print('.....')
A = np.random.randn(10)
print(A)
print('.....')
B = np.random.randn(10)
print(B)
print('.....')
byfun = np.add(A,B)
print(byfun)
print('.....')
ma = np.maximum(A,B)
print(ma)
print('.....')
website = 'http://docs.scipy.org/doc/numpy/reference/ufunce.html#availble-ufuncs'
web2 = 'http://google.com'
import webbrowser
#webbrowser.open(website)
webbrowser.open(web2)