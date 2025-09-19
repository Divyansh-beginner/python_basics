f = open("iterators.py")
# f is already a iterable object that we usually get by using the iter() method 
print(f ,"::::" ,iter(f) , "::::" , type(f))
# print(dir(f))
i = iter(f)

print(i , i.__next__() , next(i))
print(i is f)

