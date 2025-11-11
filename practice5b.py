msg =input("enter a message:")
p1="make a lot of money"
p2="buy now"
p3="subscribe this" 
p4="click this"
if p1 in msg or p2 in msg or p3 in msg or p4 in msg :
    print("🚫 This is a SPAM comment! ❌")
else:
    print("✅ This comment is NOT spam. 👍")
