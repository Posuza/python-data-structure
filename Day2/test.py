print("Hello python")
acc = int(input("Enter a word"))
print(acc)
for a in acc:
    if a == "good":
        print("It is an integer")
    else:
        print("value must be a digit")

b = type(a)
if b == "str":
    print("It is  a string")
else:
    print("It is  a digit")