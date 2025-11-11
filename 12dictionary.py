# dictionary example
# creating a dictionary

my_dict={                #using curly brackets
    "name":"uv",
    "age":21,
    "skills":["c++","python"]
}
# there are also methods to create a dictionary like zip,dict(),list of tuples ...
print(my_dict)#print full dictionay
print(len(my_dict))# find the length of dictionary
print(type(my_dict)) # to find the tpe of data
# accessing elements
print(my_dict["name"]) #direct access
print(my_dict.get("name")) # with get method we can return a default value if key i snot found
print(my_dict.get("gender","not found"))
print(my_dict.keys()) #access all keys
print(my_dict.values())#access all values
print(my_dict.items()) #acess al items
my_dict["address"]="nehru nagar" #adding a key
my_dict["age"]=22 #updating a key
print(my_dict.update({"name":"yuvi"})) #updating by update( keyword)
print(my_dict)
# removing items from a dictionary + removin elements also
# by pop method
my_dict.pop("name")
print(my_dict)
my_dict.popitem()
print(my_dict)

# nesyed dictionary
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)





