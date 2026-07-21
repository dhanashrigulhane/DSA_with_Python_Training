
from collections import deque

class node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None

class Trees:
    def __init__(self):
        self.root = None

    def insert(self, data):
        newNode = node(data)

        if self.root is None:
            self.root = newNode
            return

        q = deque([self.root])

        while q:
            temp = q.popleft()

            if temp.left is None:
                temp.left = newNode
                return
            else:
                q.append(temp.left)

            if temp.right is None:
                temp.right = newNode
                return
            else:
                q.append(temp.right)
    def bfs(self):

        if self.root==None:
            print("Empty")
            return
        q=deque([self.root])
        while q:

           temp=q.popleft()
           print(temp.data,end=",")
           if temp.left!=None:
             q.append(temp.left)
           if temp.right!=None:
               q.append(temp.right)            
    def dfs(self):
      if self.root is None:
        print("Empty")
        return
      s = [self.root]
      while s:
        temp = s.pop()      
        print(temp.data, end=", ")
        if temp.right is not None:
            s.append(temp.right)
        if temp.left is not None:
            s.append(temp.left)          

    def inorder(self, root):
        if root is not None:
            self.inorder(root.left)
            print(root.data, end=",")
            self.inorder(root.right)
    def preorder(self, root):
        if root is not None:
            print(root.data, end=",")
            self.preorder(root.left)
            self.preorder(root.right)
    def postorder(self, root):
        if root is not None:
            self.postorder(root.left)
            self.postorder(root.right) 
            print(root.data, end=",")       

t = Trees()
t.insert(10)
t.insert(20)
t.insert(50)
t.insert(30)
t.insert(40)
t.insert(60)
#t.bfs()
#t.dfs()

#t.inorder(t.root)
#t.preorder(t.root)
t.postorder(t.root)









