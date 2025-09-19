print("checking for file opening.")
print("line 2")
print("line 3")
mylist:list = [1,2,3,4,5]
iterator:iter = iter(mylist)
print(iterator)
print(type(iterator))
# print(dir(iterator))
# print(help(iterator.__iter__()))
print(iterator.__sizeof__())
print(iterator.__str__())
# print(iterator.__self__())
iterator.__next__()
i = iterator.__next__()
print(i , " ::::" , iterator , type(i) , iterator.__next__() , ":::" , next(iterator))
print(i  , iterator.__next__() , i , "::" , iterator)
print(next(iterator))


