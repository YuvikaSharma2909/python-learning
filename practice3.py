name=input("enter your name :")
print(f"good afternoon {name}")

letter='''
Dear <|Name|>,
you are selected!
<|Date|>
'''
print(letter.replace("<|Name|>","harry").replace("<|Date|>","29 sep 2025"))

msg=" harry  is a good boy"
print(msg.find("  "))
msg1="harry  is a good boy"
print(msg1.replace("  "," "))
