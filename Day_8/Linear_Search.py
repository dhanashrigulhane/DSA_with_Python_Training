def linearSearch(arr,key):
    for i in range(0,len(arr)):
        if arr[i]==key:
            return i
    return -1

li=[12,45,71,13,40,87,9,74,6]
key=int(input("Enter a key to search :"))
result=linearSearch(li,key)
if (result==-1):
    print("Key not found")
else:
    print(f"Key found at {result+1}")    








