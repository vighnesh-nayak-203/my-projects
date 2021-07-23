class Node:
    def __init__(self,data):
        self.right=None
        self.left=None
        self.data=data
class Solution:
    def __init__(self):
        self.emptyNodes=[]
    def insert(self,root,data):
        if root==None:
            a=Node(data)
            return a
        else:
            if root.left==None:
                root.left=self.insert(root.left,data)
                self.emptyNodes.append(root.left)
            elif root.right==None:
                root.right=self.insert(root.right,data)
                self.emptyNodes.append(root.right)
            else:
                a=self.emptyNodes[0]
                if any(v==None for v in [a.left,a.right]):
                    self.insert(a,data)
                else:
                    self.emptyNodes.pop(0)
                    a=self.emptyNodes[0]
                    self.insert(a,data)
            return root

    def getHeight(self,root):
        if root.right==None and root.left==None:
            return 0
        elif root.right==None:
            return self.getHeight(root.left)+1
        elif root.left==None:
            return self.getHeight(root.right)+1
        else:
            a=self.getHeight(root.right)+1
            b=self.getHeight(root.left)+1
            return max(a,b)
    def levelOrder(self,root):
        h=self.getHeight(root)
        print(" "*((2**h)-1)+str(root.data)+" "*((2**h)-1))
        b=[root.left,root.right]
        while not all(k is None for k in b):
            h-=1
            b1=[]
            for i in b:
                print(" "*((2**h)-1)+str(i.data)+" "*((2**h)-1),end=" ")
                b1.append(i.left)
                b1.append(i.right)
            b=b1
            print("")

                

T=int(input("No. of nodes:"))
myTree=Solution()
root=None
for i in range(T):
    a=input("Node Values:")
    root=myTree.insert(root,a)
height=myTree.getHeight(root)
print(f"Height={height}")
myTree.levelOrder(root)