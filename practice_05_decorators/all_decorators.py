import time 
from typing import Callable,Any

def timer(func:Callable[Any , Any])->Callable[[...] , Any]:
    def wrapper(*args , **kwargs)->Any:
        start_time:float = time.time()
        result = func(*args , **kwargs)
        end_time:float = time.time()
        print(f"function {func.__name__} takes {end_time - start_time} seconds")
        return result
    return wrapper

def func_name_and_args(function:Callable[[...] , Any])->Callable[[...], Any]:
    def wrapper(*args, **kwargs)->Any:
        print(f"function name is {function.__name__}")
        print(f"function args are {*args , kwargs}")
        return function(*args , **kwargs)
    return wrapper

def cache(func:Callable[[...] , Any])->Callable[Any , Any]:
    cachelist:dict[str,Any] = {}
    def wrapper(*args:tuple[Any] , **kwargs:dict[str , Any])->Any:
        key_args:str = ", ".join(str(i) for i in args)
        key_kwargs:str = ", ".join(f"{keys}={kwargs[keys]}" for keys in kwargs)
        key = key_args+key_kwargs
        nonlocal cachelist
        if (key in cachelist) :
            print("the same args were found in the cache , returning values without executing the function")
            result:Any = cachelist[key]
        else :
            result:Any = func(*args , **kwargs)
            cachelist[key] = result
            print(f"the args are new , executing the function and storing the output for later checkups ! and now cachesize is {len(cachelist)} and {cachelist.__sizeof__()} in bytes.")
        if len(cachelist)>20 :
            print("the cache limit is exceeded , flushing previous entries!")
            cachelist = {}
        return result
    return wrapper



