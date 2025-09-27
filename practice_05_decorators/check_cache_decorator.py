import all_decorators
import time 

@all_decorators.cache
def func(x,y):
    time.sleep(4)
    return x+y

print(func(3,7))
print(func(3,7))

