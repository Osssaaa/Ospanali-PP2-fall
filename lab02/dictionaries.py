thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)                     
print(len(thisdict))                
print(type(thisdict))               

thisdict = dict(name = "David", age = 28, country = "Russia")
print(thisdict)                     

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])            
x = thisdict.get("model")
print(x)                            
x = thisdict.keys()
print(x)                            
x = thisdict.values()
print(x)                            
x = thisdict.items()
print(x)                            

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
print(car) 
car["year"] = 2020
print(car) 

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict)                     

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
print(car) 
car["color"] = "red"
print(car)