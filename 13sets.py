thisset = {"apple", "banana", "cherry",True,1}
print(thisset)
# duplicate are not allowed that's why remove one apple and it will be unordered

thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)
# True and 1 is considered the same value:

thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

# False and 0 is considered the same value:

thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)

# lenght of a set
print(len(thisset))
# adding set item
thisset.add(5)
print(thisset)

