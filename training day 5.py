'''#local variable 
def f1():
    a = 4
    b = 5
    print(a*b) 
f1()
#global variable
a = 10
def f1():
    print(a)
f1()
####### below program print 20 because of override
x = 10
def f1():
    global x
    x = 20
    print(x)
f1()
#####################################################
def f1():
    a = 10
    def f2():
        print('hello')
        nonlocal a
        a = 40 
        print (a)
        f2()
        f1()

#CLASSES AND OBJECTS
class demo:
    def display (self,a,b):
        print ('sum is :' ,a+b)
ob = demo()
a = int(input('enter a:'))
b = int(input('enter b:'))
ob.display(a,b)

#CONSTRUCTOR 
class A:
    def __init__(self):
        print('hello')
    def display(self):
        print('how are you')
obj = A()
obj.display()

#ASSIGNMENT 3 
#question 1
def f1():
    global name 
    name = 'A' 
def f2():
    global name 
    name = 'B' 
f1()
f2()
print (name)

#question 2
a = 10
def f():
    print ('Inside f() : ', a) 
def g():
    a = 20 
    print ('Inside g() : ',a) 
def h():
    global a 
    a = 30     
    print ('Inside h() : ',a)
    print ('global : ',a)
f()
print ('global : ',a)
g()
print ('global : ',a)
h()
print ('global : ',a)

#question 3

a_var = 10
b_var = 15
e_var = 25
d_var = 100
def a_func(a_var):
    print("in a_func a_var =", a_var) 
    b_var = 100 + a_var 
    d_var = 2 * a_var 
    print("in a_func b_var =", b_var) 
    print("in a_func d_var =", d_var) 
    print("in a_func e_var =", e_var) 
    return b_var + 10 
c_var = a_func(b_var)
print("a_var =", a_var)
print("b_var =", b_var)
print("c_var =", c_var)
print("d_var =", d_var)'''

#question 4
a,b,x,y = 1,15,3,4
def fun(x, y):
    global a 
    a = 42 
    x,y = y,x 
    b = 33 
    b = 17 
    c = 100 
    print (a,b,x,y) 
fun(17,4)
print (a,b,x,y)

#question 5
def f():
    x = 42
def g(): 
    global x 
    x = 43 
    print("Before calling g: ",x) 
g() 
print("After calling g: ",x) 
 
f()
print("x in main: " ,x)

#question 6 
def outer():
    s="Ludhiana"
def inner1():
    s="punjab"
def inner2():
    nonlocal s
    s="Chandigarh"
def inner3():
    global s
    s="Haryana"
    print(s)
    inner1()
    print(s)
    inner2()
    print(s)
    inner3()
    print(s)
    outer()
    print(s)

    #question 8
    a,b=100,200
class MyClass():
    a,b=10,20
def add(self,a,b):
    print(a+b)
    print(globals()['a']+globals()['b'])
    print(self.a+self.b)
def mul(self,a,b):
    print(a*b)
    print(globals()['a']+globals()['b'])
    print(self.a*self.b)
c = MyClass()
c.add(3,3)
c.mul(4,4)