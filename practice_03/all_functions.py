import math
def get_pow(num , power) -> int:
    ans :int = num ** power
    return ans

def get_sum_of_two_nums(n1 , n2)->int:
    return n1+n2

def multiply(a , b) ->str or int:
    if type(a) == int and type(b) == int:
        return a*b
    else :
        if type(a) != int and type(b) != int:
            return "both arguments can't be string , pass atleast one number two multiply!"
        elif type(a) == int :
            c:int = a
            a:str = b
            b:int = c
        ans_str = ""   
        for i in range(0 , b, 1):
            ans_str = ans_str + a

        return ans_str

def circle_area_and_circumf(r:int)->(int,int):
    return round(math.pi*r*r , 3) , round(2*math.pi*r ,3)

def greet(name:str=None)->None:
    if name == None or name == "":
        print("greetings user of no name!")
    else :
        print(f"greetings user {name}")

cube: int = lambda a : a**3

def variable_parameters_sum(*nums:tuple[int])->int :
    sum:int = 0
    for num in nums:
        sum += num
    return sum    

def variable_keyword_args(**kwargs:dict[any,any])->None:
    print(kwargs)
    print("----------------------")
    print(*kwargs)
    print("----------------------")
    # print(**kwargs)
    # print(type(**kwargs))
    print("----------------------")
    for keys in kwargs:
        print(keys,": ",kwargs[keys])

def generate_even_nums_upto_limit(limit:int)->int:
    for even_num in range(0 , limit+1, 2):
        yield even_num

def factorial(value:int)->int:
    if value == 0 or value == 1 : return 1
    return value * factorial(value-1)



