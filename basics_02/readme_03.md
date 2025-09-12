in python , enter dir(module/class/obj) to get all the names defined inside that obj/module/class.
but to know which are methods use :
callable(obj/../..) gives true: if obj is a function , else false
could use type() for it too.
or use help(obj/module/class).
usually all uppercase are constants, no need for ().
no _ means public and safe/normal to use.
one _ in front means: kinda private ones and not usually used.
Double __ : special methods.
 modules and packages(i.e. a .py file in library): lowercase (decimal , random , math)
 classes : in CamelCase(Decimal, Random, SystemRandom)
 methods: lowercase and underscores (getcontext(), setstate(), randint())
 consts: all caps (PI, E, TWOPI)
function(value)
obj.method() or objtype.method(obj)
value = Classes(entryvalue)
no need to learn signs of operators , find all the related __method__ using dir then the dunder ones are there for operators too, like: a - b → a.__sub__(b)

a * b → a.__mul__(b)

a / b → a.__truediv__(b)

a // b → a.__floordiv__(b)

a % b → a.__mod__(b)

a ** b → a.__pow__(b)

-a → a.__neg__()
