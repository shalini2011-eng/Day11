# class A():
#     def m1(self):
#         print("this is m1 method")
#
# class B(A):
#     def m2(self):
#         print("this is m2 method")
#
# class C(A):
#     def m3(self):
#         print("this is m3 method")
#
# obj1 = C()
# obj1.m1()
# obj1.m3()
#
# obj2 = B()
# obj2.m2()
# obj2.m1()

# class A():
#     def m1(self):
#         print("this is m1 method of class A")
#
# class B(A):
#     def m1(self):
#         print("this is m1 method of Class B")
#         super().m1()
#
# obj =B()
# obj.m1()
#
# obj2 = A()
# obj2.m1()

# class A:
#     a,b = 1000,2000
#
# class B(A):
#     i,j=100,200
#
#     def m1(self,x,y):
#         print(x+y)
#         print(self.i+self.j)
#         print(self.a+self.b)
#
# obj1 = B()
# obj1.m1(10,20)

# class Parent:
# #     name = "scott"
# #
# # class child(Parent):
# #     name = "john"
# #
# # childObj = child()
# # print(childObj.name)

# class calculation:
#     def add(self, name=None):
#         if name is not None:
#             print("Hello ", name)
#         else :
#             print("Hello")
#
# obj = calculation()
# obj.add()
# obj.add("raju")

class A:
    def calc(self,a=0,b=0, c=0):
        print(a+b+c)

obj = A()
obj.calc()
obj.calc(10)
obj.calc(10,20)
obj.calc(10,20,30)
