# chem = 50
# maths = 59
# phy = 60
# pi = 3.14
# name = "dhanashri"
# print(type(chem))
# print(type(maths))
# print(type(phy))
# print(type(pi))
# print(type(name))

#How to check the address of any variable?
#using id() to return the address of variable
# chem = 50
# maths = 59
# phy = 60
# pi = 3.14
# name = "dhanashri"
# print(id(chem))
# print(id(maths))
# print(id(phy))
# print(id(pi))
# print(id(name))

#What is type casting.
#converison from one data type into another is called type casting
# print(2+2)
# print("2"+"2")
# val1= int(input("Enter first value :"))
# val2= int(input("Enter second value :"))
# print(val1 + val2)

# print(int(3.14))
# print(int(True))
# print(int(False))
# print(int("4"))
#print(int("dhanashri"))
#we cannot convernt complex value to int
#we cannot convert floating point value  string to int and convert string to int
#print(int(10+7j))


#float
# print(float(3))
# print(float(True))
# print(float(False))
# print(float("4"))
# print(float(4.22))
#print(float(10+3j))
#print(float("hii"))

#complex()
# print(complex(3))
# print(complex(True))
# print(complex(False))
# print(complex(12.4))
# print(complex("5"))
# print(complex("5.6"))
# print(complex(True,False))
# print(complex(4,-2))
# print(complex("name"))# we cannot convernt name into complex


#bool() is used to convert
# print(bool(0))
# print(bool(False))
# print(bool(1+2j))
# print(bool(True))
# print(bool(-1))
# print(bool(0+0))
# print(bool(""))


# val1 = int(input("Enter first value : "))
# val2 = int(input("Enter second value : "))
# print("Before swapping")
# print("Val1 = ",val1, "  " ,"Val2 = ",val2)
# temp = val1
# val1 = val2
# val2 = temp
# print("After swapping")
# print("Val1=",val1, "  ","Val2=",val2)


# val1 = int(input("Enter first value : "))
# val2 = int(input("Enter second value : "))
# print("Before swapping")
# print("Val1 = ",val1, "  " ,"Val2 = ",val2)
# val1= val1 + val2
# val2 = val1 - val2
# val1 = val1 - val2
# print("After swapping")
# print("Val1=",val1, "  ","Val2=",val2)

#Simple interest program
# principal = int(input("Enter principal amount : "))
# rate_of_interest= int(input("Enter the rate of interest : "))
# time = int(input("Enter the duration of loan amount : "))
# simple_interest = principal * rate_of_interest * time/100
# print("Simple_interest_amount = ",simple_interest)


# pi = 3.14
# radius = int(input("Enter the radius : "))
# Area = pi * radius * radius
# print("Area_of_circle = ",Area)


# pi = 3.14
# radius = int(input("Enter the radius : "))
# circumference = 2 *pi * radius
# print("Circumference =  ",circumference)

# h=float(input("Enter the height in feet : "))
# inch = h* 12
# cm = inch * 2.54
# print("Inch : ",inch)
# print("Centimeter : ",cm)

# num= 123
# a = num % 10 #a=3
# num=num // 10 # num=12
# b= num % 10   #b=2
# c=num //10    #c=1
# reverse = a*100 + b* 10 + c*1
# print("Reverse = ",reverse)

# num= 1234567
# a = num % 10 #a=7
# num=num // 10 # num=123456
# b= num % 10   #b=6
# num=num //10    #num=12345
# c=num % 10  #c=5
# num=num //10  #num=1234
# d=num % 10 #d=4
# num = num //10 #num = 123
# e = num %10 #e = 3
# num = num //10 #num =12
# f = num%10  #f= 2
# g = num//10 #g=1
# reverse = a*1000000 + b* 100000 + c*10000 + d*1000 + e*100 +f*10 + g*1
# print("Reverse = ",reverse)

# cel=float(input("Enter the temp in celsius : "))
# f= 1.8 * cel +240
# print("Temp in Frarenahit = ",f)



#operators 
#special operators 1) Identity operators for address comparison
#1.ls 
#2.ls not 
# math = 50
# chem = 50
# phy =50
# english= 80
# print(id(math))
# print(id(chem))
# print(id(phy))
# print(id(english))


# x = 10
# y = 10
# print( x is y) # value is same so true 
# print( x is not y)# is not means different memory

# x = 10
# y = 10
# z = 20
# print(x is not y)
# print(z is not y)

#Membership operators
#we check that object is present or not in collection data structure(list, tuple,dict,set,string) 1) in if the given object is present then it return true
#not in if the given object is not present then it return false

# a= "help4code"
# print('p' in a)
# print('z' in a)


# name="dhanashrig"
# print(name[0])
# print(name[1:7:2])
# print(name[::-1])
# print(name[0:])
# print(name[2:])


# age = int(input("Enter the age : "))
# if age > 18 :
#     print("Voter is eligible for voting ")
# else:
#     print("Voter is not eligible for voting")


# a = int(input("Enter the first value : "))
# b = int(input("Enter the second value : "))
# c = int(input("Enter the third value : "))
# if a > b and a > c :
#     print("First value is greater than b and c ")
# elif b > a and b > c :
#     print("Second value is greater than a and c ")
# else:
#     print("Third value is greater than a and b ")


