import all_decorators

@all_decorators.func_name_and_args
def example_function(*args , **kwargs)->None:
    print(*args , *kwargs)

example_function(10 , 20 , "string hello" , brand = "monkey" , model = "new model")
