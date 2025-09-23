import all_classes
electric_car_obj:object = all_classes.Electric_car(brand = "Tesla" , model = "new_model" , battery_size = 24)
print(electric_car_obj._Car__brand)
print(electric_car_obj._Car__model)
print(electric_car_obj._Electric_car__battery_size)
electric_car_obj.full_name()
print('electric_car_obj.brand , "or" , electric_car_obj.__brand "will not work anymore"')

