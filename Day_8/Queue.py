class QueueIM:
    def __init__(self):
        self.front=-1
        self.rear=-1
        self.size=5
        self.queue=[0]*self.size
    def enqueue(self,data):
       if self.rear==self.size-1:
          print("Overflow ")
       elif self.front==-1 and self.rear==-1:
          self.front+=1
          self.rear+=1
          self.queue[self.rear]=data
       else:
          self.rear+=1
          self.queue[self.rear]=data
          
    def dequeue(self):
       if self.front==self.size:
          print("Underflow")
       else:
          print(f'{self.queue [self.front]} item dequeue') 
          self.front+=1 
    def display(self):
       for i in range(self.front,self.rear+1):
          print(self.queue[i],end=" ")
       print()                
choice=1
qu=QueueIM()
while choice!=0:
   
  print("1.Enqueue :")
  print("2.Dequeue :")
  print("3.Display :") 
  choice=int(input("Enter the choice :"))   
  if choice==1:
    data=int(input("Enter the data : "))
    qu.enqueue(data)
  elif choice==2:
     qu.dequeue()
  elif choice==3:
     qu.display()  
