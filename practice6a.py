# def greatest(a,b,c):
#     if a>b and a>c:
#         greatest=a
#     elif b>a and b>c:
#         greatest=b
#     else:
#         greatest= c
#         return greatest

# print(greatest(2,3,4))

# def ftoc(farehnite):
#     return (5*(farehnite-32))/9
# print(f"{ftoc(212)}°c" )
def sumofn(num):
    if num==1 :
        return 1
    else:
         return num+sumofn(num-1)
    
print(sumofn(5))    




