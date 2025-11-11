t1=()
t2=(10,20,30,40) #tuples with same elements
t3=("ankit",5,4.5)
t4=(4)#it will return int dattaype not tuple beacuase for tuple we must use comma after a elemet if it is only single element
print(type(t4))
t5=(4,)
print(type(t5))
print(len(t3))

print(t3[2])
print(t3[-2])

# if we wnt to change in a tuple so we need to convert a tuple into list then took changes then covert it into list

y=list(t3)
y.append(True)
t3=tuple(y)
print(t3)

# now lets unpack a tuple

(a,b,c,d)=t3
print(a)

# add two tupples
join=t2+t3
print(join)

# to multiply the content
multiply=t2*2
print(multiply)

# count method
x=t2.count(5)
print (x)

# index method
y=t2.index(20)
print(y)
