name=input("Enter your name :")
if len(name)>3 and name.isalpha():
    print(f"hello {name},How are you?")
else:
    print("Invalid user name")