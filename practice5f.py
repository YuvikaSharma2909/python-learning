# 💬 Program to check if a post is talking about Harry

# 📝 Taking post input from the user
post = input("✏️ Enter your post: ")

# 🔍 Checking if the word 'harry' is mentioned
if "harry" in post.lower:
    print("🧙‍♂️ This post is talking about Harry! ⚡")
else:
    print("🤔 This post is NOT about Harry.")
