# global_var = 20
# def func():
#     local_var = 10
#     print(local_var)
#     print(global_var)
#
# func()
# print(global_var)
#print(local_var)

#global xy
# def cool():
#     global xy
#     xy=200
#     print(xy)
#
# cool()
# print(xy)

# def myFunc():
#     print("Hello")
# myFunc()
#
# def myFunc1(name):
#     print("Hello", name)
# myFunc1("Shivam")

# def myFunc2(a,b):
#     return (a+b)
#
# # x = myFunc2(2,6)
# # print(x)
# a = int(input("Enter a Value: "))
# b= int(input("Enter b value: "))
# x= myFunc2(a,b)
# print("x value is :", x)

# def func(i,j=100):
#     return (i,j)
#
# #print(func(j=10,i=20))
# print(func(200))
# print(func(200,300))

# def func(greetmsg, name):
#     print(greetmsg, name)
#
# func(greetmsg = "Good morning", "Raju")

# def func(a,b):
#     if a>b:
#         return a,b
#     else :
#         return b,a
# 
# print(func(20,33))
# print(type(func(22,11)))

# class A:
#     a=20
#     b=30
#     def func(self,a,b):
#         self.a=10
#         self.b=20
#         print("Class A")
#         return a,b
# obj= A()
# print(obj.func(20,30))

# p,s=1000,2000
# class myClass:
#     p,s=100,200
#     def myFunc(self):
#        p,s=10,20
#        print(p+s)
#        print(self.p+self.s)
#        print(p+s)
#        print(globals()['p']+globals()['s'])
#
#     def myMethod1(self,s):
#         print("its static method", s)
#
# obj = myClass()
# obj.myFunc()
# obj1=myClass()
# obj1.myFunc()
# #myClass.myMethod1(9)

# class A:
#     def __init__(self):
#         print("this is init constructor")
#
#     def __str__(self):
#         print("this is str constructor")
#
#     def display(self,c):
#         print("its method display for x",c)
#
# obj1=A()
# obj2=A()
# obj1.display(4)
#
# class A:
#     def __init__(self, val1, val2):
#         print(val1, val2)
#         self.val1 = val1
#         self.val2 = val2
#
#     def display(self,val3):
#         print(self.val1 * self.val2 * val3)
#
#     def add(self):
#         print(self.val1+self.val2)
#
# obj1 =A(10,20)
# obj1.display(3)
# obj1.add()

# class A:
#     name = 'John'
#     def __init__(self,name):
#         print(name)
#         print(self.name)
#
# obj1 = A("David")

class B:
    def __init__(self,eid,ename,sal, desg):
        self.eid = eid
        self.ename = ename
        self.sal = sal
        self.desg = desg

    def __str__(self):
        print(self.eid, self.sal, self.desg)
        return self.ename


obj1 =B(101, "John", 25000,'IT')
print(obj1)
#obj1.display()
obj2 = B(102,"Rishi", 28000,'Testing')
#obj2.display()


