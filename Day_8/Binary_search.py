#BINARY SEARCH
def BinarySearch(arr,key,low,high):
    if low<=high:
      mid=(low+high)//2
    if(arr[mid]<key):
       return BinarySearch(arr,key,mid+1,high)
    elif(arr[mid]>key):
        return BinarySearch(arr,key,low,mid-1)
    else:
        return mid
li=[12,45,71,13,40,87,9,74,6]
key=int(input("Enter a key to search :"))
result=BinarySearch(li,key,0,len(li)-1)
if (result==-1):
    print("Key not found")
else:
    print(f"Key found at {result+1}")   
