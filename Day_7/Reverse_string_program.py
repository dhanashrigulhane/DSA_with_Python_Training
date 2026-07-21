str1 = input("Enter a string: ")
letters= []
for char in str1:
    if char != " ":
       letters.append(char)
res = ""
for char in str1:
    if char == " ":
        res = res + " "
    else:
        res = res+ letters.pop()
print("Reversed String : ", res)