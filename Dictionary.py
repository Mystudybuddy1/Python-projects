#Dictionary
dict = {"name":"Aarush","class":"6","surname":"Verma","School name":"BRGS"}
print(dict)
print(type(dict))
print(len(dict)) 
print(dict["name"])
x = dict.keys()
print(x)
y = dict.values()
print(y)
x = dict.items()
print(x)
dict["surname"] = "soni"
print(dict)
dict.pop("School name")
print(dict)
del dict["class"]
print(dict)
dict.clear()
print(dict)