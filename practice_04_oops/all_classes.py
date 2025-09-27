class Car:
    Total_counter:int = 0
    Ecar_counter:int = 0
    def __init__(self,**kwargs:dict)->None:
        for key in kwargs:
            setattr(self , f"_{self.__class__.__name__}__{key}" , kwargs[key])
        __class__.Total_counter += 1
            
    def __getattr__(self , method:str)->any :
        if method.startswith( "get_"):
            method_name:str = method.__getitem__(slice(4,None,1))
            mangled_name:str = f"_{self.__class__.__name__}__{method_name}"
            if mangled_name not in self.__dict__ :
                raise AttributeError(method)
            else : 
                return lambda : self.__dict__[mangled_name] 
        raise AttributeError(method)

    def print_full_name(self)->None:
        if f"_{self.__class__.__name__}__brand" in self.__dict__ and f"_{self.__class__.__name__}__model" in self.__dict__ :
            print(f"brand is: {self.__dict__[f"_{self.__class__.__name__}__brand"]} and name is: {self.__dict__[f"_{self.__class__.__name__}__model"]}")
        else : print("No brand or model attribute is given for this method to work !")

    def fuel_type(self):
        if self.__class__.__name__ == "Car" :
           return f"fuel type is petroleum"
        elif self.__class__.__name__ == "Electric_car":
            return f"fuel type is electricity !"
        else : pass

    @classmethod
    def general_discription(cls)->str:
        return f"its a {cls.__name__}."

      
class Electric_car(Car):
    def __init__(self , **kwargs:dict)->None:
        self.__battery_size:int = kwargs.pop("battery_size")
        super().__init__(**kwargs)
        __class__.Ecar_counter += 1
        