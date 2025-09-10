import math
import random
import sys
print(2.5*5)
print(2**100)
print(2**math.pi)
print(2**random.random())
print(2** random.choice([1 ,2 ,3 , 4]))
string = [1 ,2 ,3 ,4 ,5]
print(len("string"))
string[0]=-1

# print(string[0])
# print(string[1:4])
# print(dir("string"))
# print(dir((1,2,3,4)))
# mylist = [123 , 3.23 ,"astringinlistwithints" , ["alistinsidealist"]]
# print(dir(mylist))
print(sys.getrefcount("thismethodgivesthereferencecountofthisstring"))

l1= [1,290,360]
l2 = l1
l1 = 100
print(l2[0])
l1 = [1,290,360]
l1[0] = 100
print(l2[0])
li1 = [10,20,30]
li2 = [10,20,30]
li2[0]=100
print(li1[0])
li3 = li1[:]
li3[0] = 22
print(li3[0])
print(li1[0])
li1[0]=22
print(li1==li3)
print(li1 is li3)







