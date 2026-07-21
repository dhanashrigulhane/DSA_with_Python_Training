

class node:
    def __init__(self,data):
       self.data=data
       self.next=None
class LinkedList:
    head=None
    def InsertAtBeg(self,data):
        newNode=node(data)
        if self.head==None: 
           self.head=newNode
        else:
            newNode.next=self.head
            self.head=newNode 
    def display(self):
        if self.head==None :
            print("Empty !")
        else:
            temp=self.head
            while temp!=None:
                print(temp.data, end="->")   
                temp=temp.next
            print()
    def InsertAtEnd(self,data):
        newNode=node(data)
        if self.head==None:
            self.head=newNode
            newNode.next=None
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            newNode.next=None
            temp.next=newNode  

    def InsertAtGivenPosition(self,pos,data):
        newNode=node(data)
        if(pos==1):
            self.InsertAtBeg(data) 
        else:
            if(self.head==None):
                print("List is empty")
            else:
                temp=self.head
                i=1
                while i<pos-1:
                    if temp!=None:
                        temp=temp.next
                        i+=1
                    else:
                        print("Invalid pos !!")
                        return
                newNode.next=temp.next
                temp.next=newNode  
    def DeleteAtBeg(self):
        if(self.head==None):
            print("List is empty")
        else:
            self.head= self.head.next   
    def DeleteAtGivenPosition(self):
        if(self.head==None):
            print("List is empty")
        else:
            temp=self.head  
        while temp.next.next != None:
            temp=temp.next
        temp.next=None                                                     
choice=1
ll=LinkedList()
while choice!=0:
    print("1.Insert at beg")
    print("2.Insert at end")
    print("3.Display")
    print("4.Insert at given position")
    print("5.Delete at beg")
    print("6.Delete at End")
    choice=int(input("Enter the choice :"))
    if choice==1:
        data=int(input("Enter data :"))
        ll.InsertAtBeg(data)
    elif choice==2:
        data=int(input("Enter the data of a node :")) 
        ll.InsertAtEnd(data)   
    elif(choice==3):
        ll.display()
    elif(choice==4):
        pos=int(input("Enter the position"))
        data=int(input("Enter the data :"))
        ll.InsertAtGivenPosition(pos,data) 
    elif(choice==5):
        ll.DeleteAtBeg()       
ll.linkedlist()        



