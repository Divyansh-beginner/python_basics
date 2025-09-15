import bisect
marks:int = int(input("enter the marks:"))
grades:list = ["F", "D", "C", "B", "A"]
cutoffs:list = [60,70,80,90]
position:int = bisect.bisect(cutoffs,marks)
grade:str = grades[position]
print(f"your grade is: {grade}")
exit()

