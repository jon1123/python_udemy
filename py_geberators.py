###### Python Generators #######
def gencube(n):
    # out = []
    for num in range(n):
        # out.append(num**3)
        yield num**3
    # return out
    ## note that 'out' would be stored in memory 

for x in gencube(10):
    print(x)    

print(' ')

def genfibon(n):
    a = 1
    b = 1
    
    for i in range(n):
        yield a
        a, b = b, a+b
##        c = a + b
##        a = b
##        b = c

for num in genfibon(10):
    print(num)

print(' ')

def fibon(n):
    a = 1
    b = 1
    
    output = []
    for i in range(n):
        output.append(a)
        a,b = b, a+b
        
    print(output)

fibon(10)

print(' ')

# next()

def simple_gen():
    for x in range(3):
        yield x
        
g = simple_gen()
print(next(g))
print(next(g))
print(next(g))

print(' ')

# iter()

s= 'hello'

for let in s:
    print (let)

print('')

s_iter = iter(s)
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))

############
import random

def rand_num(low,high,n):
    for i in range(n):
        yield random.randint(low,high)

for num in rand_num(1,10,12):
    print(num)
    
