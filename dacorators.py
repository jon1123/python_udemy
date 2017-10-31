'''Decorators'''

def func():
    print(1)
    #return 1

func()

s = 'This is a golbal variable'

def func():
    print(locals())

print(globals())
print(globals()['s'])

func()
    
def hello(name = 'Jose'):
    print( 'Hello ' + name)

hello()

greet=hello

#del hello()  // dose not work??? 

greet()
######## video 2 ###########
### Functions within Functions

def hello_1(name='Jose'):
    print('The hello() function has been executed.')
    def greet():
        return '\t This is inside the greet() function.'
    
    def welcome():
        return '\t This is inside the welcome() function.'
    
    if name == 'Jose':
        print( greet)
    else:
        print( welcome)
##    print(greet())
##    print(welcome())
##    print('Now we are back inside the Hello() function.')

hello_1()
#welcome() not localy defined
print(' \n')

####Functions as arguments
def hello_2():
    return 'Hi Jose.'

def other(func):
    print('Other code gose hear!')
    print(func())

other(hello_2)

def new_decorator(func):
    
    def wrap_func():
        print('Code here, before executing the func.')
        
        func()
        
        print('Code hear will execute after the func().')
    
    return wrap_func

def func_needs_decorator():
    print('This function needs a decorator!')

func_needs_decorator()
print(' ')
func_needs_decorator = new_decorator(func_needs_decorator)
func_needs_decorator()
print(' ')

#this dose the same thing the @ symbole is a decorator in python 
@new_decorator
def func_needs_decorator_1():
    print('This function needs a decorator?')

func_needs_decorator_1()