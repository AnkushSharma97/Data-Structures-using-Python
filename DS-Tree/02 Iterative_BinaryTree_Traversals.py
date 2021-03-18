#In recursive Travesral methds we use internal stack to implement the tree Traversals
#but in Iterative method we  will use our own explicit Stack for the implementation
#here we cant use static stack i.e. we need to use dynamic stack (the one created
#using linked list) because we dont know how much size stack needs to store tree's
#data in starting. or else we can use python list as well, as stack.
class Btnode:
    def __init__(self,data):
        self.left_child=None
        self.info=data
        self.right_child=None

class BinaryTree:
    def preorder(self,root):
        stack=[]
        stack.append(root)
        while len(stack)!=0:
            data=stack.pop()
            print(data.info,end=" ")
            if data.right_child is not None:
                stack.append(data.right_child)
            if data.left_child is not None:
                stack.append(data.left_child)
    def inorder(self,root):
        current=root
        stack=[]
        while True:
            if current is not None:
                stack.append(current)
                current=current.left_child
                #traversing till end of leftmost leaf
            elif len(stack)!=0:
                current=stack.pop()
                print(current.info,end=" ")
                current=current.right_child
            else:
                break

    def postorder(self,root):
        current=root
        stack=[]
        stack.append(current)
        while len(stack)!=0:
            if current is not None:
                if current.right_child is not None:
                    stack.append(current.right_child)
                if current.left_child is not None:
                    stack.append(current.left_child)
                current=current.left_child
                #traversing till end of leftmost leaf
            elif len(stack)!=0:
                current=stack.pop()
                if current.left_child==None and current.right_child==None:
                    last_visited=current
                    print(current.info,end=" ")
                    current=None #optional but if we use it it will not
                                 #go to if loop unnecessarily.
                elif current.right_child !=None:
                    if current.right_child==last_visited:
                        last_visited=current
                        print(current.info,end=" ")
                        current=None
                    else:       
                        stack.append(current)
                elif current.left_child!=None:
                    if current.left_child==last_visited:
                            last_visited=current
                            print(current.info,end=" ")
                            current=None
                    else:       
                        stack.append(current)

    def levelorder(self,root):
        from collections import deque #using internal deque or else we 
        queu=deque()                  #can implement our own queue as well
        queu.append(root)
        while len(queu)!=0:
            element=queu.popleft()
            print(element.info,end=" ")
            if element.left_child is not None:
                queu.append(element.left_child)
            if element.right_child is not None:
                queu.append(element.right_child)
            
            
       
'''here we will manually create the following tree using Btnode class:-
           A
          / \
         B   C
        / \
       D   E
          / \
         F   G
'''
root=Btnode('A') #root node as root
root.left_child=Btnode('B')
root.right_child=Btnode('C')
root.left_child.left_child=Btnode('D')
root.left_child.right_child=Btnode('E')
root.left_child.right_child.left_child=Btnode('F')
root.left_child.right_child.right_child=Btnode('G')


bt=BinaryTree()
print("traversal of given tree is --> ",end='')
bt.levelorder(root)
