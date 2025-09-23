x = 10
# def f():
#     return x+1
# print(x)
# value=f()
# print(value)
# def f2():
#     global x 
#     x += 1

# f2()
# print(x)

def f3():
    x = 55
    print(x)
    def inner(): 
        nonlocal x 
        x = 33
        print(x)
    print(x)
    inner()
    print(x)

print(x)
f3()
print(x)