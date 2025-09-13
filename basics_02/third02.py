import random
import inspect
import decimal

# print(dir(random))
# print(dir(random.randint))
# print(help(random.randint))
print(type(random.randint))
# print(help(random.choice))
print(type(random.__file__))
print(inspect.__file__)
print(random.randint.__le__)
# print(help(decimal.Decimal))
print(0.1+0.1+0.1-0.3)
# print(2**10000)
x = 10
# print(dir(x))
# print(True + 4) #gives 5
print({1,2,3,4}) #its a set , braces without key:value pair is set(from maths).
x = "astring"
# print(dir(x))
# print(help(x.__class__))
print(x[0])
# print(help(x.lstrip))
# print(help(x.rstrip))
# print(help(x.strip))
# print(help(x.__getitem__))
# print(help(x.removeprefix))
# print(help(x.rjust))
# print(help(x.split))
# print(help(x.__reduce__))
# print(help(x.__str__))
# print(help(x.__getitem__))
# print(help(slice))
# print(x.__getitem__(slice(0,4,None)))
# print(help(x.replace))
# print(x.replace("tri","pro",-1))
# print(help(x.encode))
# print(help(x.format))
# print(help(x.maketrans))
# print(help(x.translate))
# print(help(x.split))
y = "could {} be added later as a {} ?"
print(y.format("this","variable"))
y = ["string","anotherstring"]
# print(dir(y))
# print(help(y.__getitem__))
print(y.__getitem__(slice(1,None,None)))
# print(help(x.join))
print(r"hello\nmybrothe")
print(r"c\user\\")













