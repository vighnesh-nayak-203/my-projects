class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linked_list:
    def __init__(self):
        self.root=node(None)
        self.length=0
    def add(self,data):
        c_Node=self.root
        while c_Node.next!=None:
            c_Node=c_Node.next
        a=node(data)
        c_Node.next=a
        print(f"{data} added at the end.")
        self.length+=1
    def pop(self):
        if self.length>0:
            c_Node=self.root
            p_Node=None
            while c_Node.next!=None:
                p_Node=c_Node
                c_Node=c_Node.next
            p_Node.next=None
            print(f"Last element:{c_Node.data} removed.")
            self.length-=1
        else:
            print("List is empty.")
    def prnt(self):
        c_Node=self.root
        while c_Node.next!=None:
            c_Node=c_Node.next
            print(c_Node.data)
    def insert(self,data,pos):
        if self.length>0 and self.length>=pos:
            c_Node=self.root
            for i in range(pos):
                p_Node=c_Node
                c_Node=c_Node.next
            a=node(data)
            p_Node.next=a
            a.next=c_Node
            self.length+=1
            print(f"{data} inserted at {pos}.")
        else:
            print("Position does not exists.")
    def delete(self,pos):
        if self.length==0:
            print("List is empty.")
        else:
            if pos<=self.length:
                c_Node=self.root
                for i in range(pos):
                    p_Node=c_Node
                    c_Node=c_Node.next
                p_Node.next=c_Node.next
                self.length-=1
                print(f"{c_Node.data} at position {pos} is removed.")
            else:
                print("Position out of range.")
    def size(self):
        print(f"Length of linked list is {self.length}.")
a=[[1,2],[2,4],[3,1],[5,6]]
a.sort(reverse=True)
print(a)