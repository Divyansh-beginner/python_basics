import pandas as pd

datalistlist = [
    [100,101,102,"hello"],
    ["one","two","three","four",None]
]
datadictlist = {
    "id" : [100,101,102,103],
    "name" : ["zero","one","two","three"]
}
datadictdict = {
    "id": {"one":101,"two":102,"three":103},
    "name":{"first":"name1","sec":"name2","third":"name3"}
}
datalistdict = [
     {"one":101,"two":102,"three":103},
     {"first":"name1","sec":"name2","third":"name3"},
     {"a":1001,"b":1002,"c":1003}
]
dflistlist = pd.DataFrame(datalistlist)
dfdictdict = pd.DataFrame(datadictdict)
dfdictdict = pd.DataFrame(datadictdict)
dflistdict = pd.DataFrame(datalistdict)

# print(dflistlist)
# print("*"*77)
# print(dfdictdict)
# print("*"*77)
# print(dfdictdict)
# print("*"*55)
print(dflistdict)