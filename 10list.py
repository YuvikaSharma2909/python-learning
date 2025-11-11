friends=["apple",2,23.4,False,"orange"]
# access elements
print(friends[1])
print(friends[-4])
print(friends[0:3])
friends[1]=5      #list are mutuable that mean we can change
print(friends[1])
print(type(friends))
friends.insert(4,"mango") #add items in a specified index
print(friends)
friends.append(3)
print(friends)
ship=["chikoo",4]
friends.extend(ship)
print(friends)
friends.remove(5)
print(friends)
friends.pop(4)
print(friends)


