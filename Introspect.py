import requests
import inspect
import sys

print(sys.executable)
print(sys.version)
print(sys.platform)



# def fun():
#     pass

# class Human:
#     def toWork(self):
#         pass
#     def toEat(self):
#         pass
#
# list = []
#
# rq = requests
# fun1 = fun
# nick = Human
#
# print(requests.__name__)
# print(rq.__name__)
# print(fun1.__name__)
# print(fun.__name__)
# print(Human.__name__)
# print(nick.__name__)

# for method in dir(Human):
#     print(method)
#
# print(inspect.ismodule(requests))
# print(inspect.isclass(requests.Session))
# print(inspect.isfunction(requests.get))

# data = "string"
#
# dir()
#
# def fun():
#     pass
#
# startLetter = input("Input start latter: ")
#
# for method in dir(data):
#     if method.startswith(startLetter.lower()):
#         print(method)

# print(getattr(data, "reverse", None))
# print(getattr(data, "index", None))
# print(callable(data))
# print(callable(fun))

# class Parent:
#     pass
#
# class Child(Parent):
#     pass
#
# print(issubclass(Parent, Child))
# print(issubclass(Child, Parent))
#
# petr = Parent()
# petrPetrivich = Child()
#
# print(isinstance(petr, Parent))
# print(isinstance(petrPetrivich, Child))