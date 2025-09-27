import all_decorators
import time

@all_decorators.timer
def example_function(*args , **kwargs)->None:
    time.sleep(*args , **kwargs)

example_function(2)