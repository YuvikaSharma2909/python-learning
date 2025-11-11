import emoji

a=int(input("enter a:"))
b=int(input("enter b:"))
c=int(input("enter c:"))
d=int(input("enter d:"))
if (a>b) and (a>c) and  (a>d):
            greatest=a
elif (b>a) and (b>c) and  (b>d):
            greatest=b
elif (c>a) and (c>b) and  (c>d):
            greatest=c
else:
        greatest=d
# display result
print("the greatest no. is {slightly smiling face} ",greatest)# grinning face
print("\N{grinning face}")

# slightly smiling face
print("\N{slightly smiling face}")

# winking face
print("\N{winking face}")