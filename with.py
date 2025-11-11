with open("file.txt", "r") as file:
    data = file.read().lower()
    if("python" in data):
        print("the word python is present")
    else:
        print("the word python is not  present")
    file.close()