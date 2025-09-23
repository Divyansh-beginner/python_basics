class Car:
    def __init__(self,**kwargs:dict)->None:
        for key in kwargs:
            setattr(self , "_Car__"+key , kwargs[key])

    def full_name(self)->None:
        print(f"brand is: {self.__brand} and name is: {self.__model}")
      
class Electric_car(Car):
    def __init__(self , **kwargs:dict)->None:
        self.__battery_size:int = kwargs.pop("battery_size")
        super().__init__(**kwargs)
        