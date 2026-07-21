class stac:
  def __init__(self):
     
      
   self.size=5
   self.top=0-1
   self.stack=[0]*self.size
  def overflow(self):

    if(self.top==self.size-1):
        return True
    return False

  def underflow(self):
    if(self.top==-1):
        return True
    return False
  
  def push(self,data):
     if(self.overflow()):
        print("Overflow")
     else:
        self.top+=1
        self.stack[self.top]=data
  def pop(self):
     if(self.underflow()):
        print("Underflow")
     else:
        self.top-=1

  def display(self):
         for i in range(self.top,-1,-1):
            print(self.stack[i])                

s=stac()
choice=1
while choice!=0:
    print("1.Push()")
    print("2.Pop()")
    print("3.Display()")
    choice=int(input("Enter your choice : "))
    if (choice==1):
        data=int(input("Enter the data :"))
        s.push(data)
    elif (choice==2):
        s.pop()
    elif(choice==3):
        s.display()        




