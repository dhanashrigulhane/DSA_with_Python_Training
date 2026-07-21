dict1={}
string1=input("Enter string: ")
for char in string1:
    if char in dict1:
        dict1[char]+=1
    else:
        dict1[char]=1
arr=[]
for key in dict1.keys():
    arr.append(key)
arr.sort()
for keys in arr:
    print(keys,":",dict1[keys])