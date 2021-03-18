class Btnode:
    def __init__(self,data):
        self.left_child=None
        self.info=data
        self.right_child=None


class BinaryTree:
    
    def preorder(self,root):
        if root==None:
            return
        print(root.info,end=" ")
        self.preorder(root.left_child)
        self.preorder(root.right_child)

    def inorder(self,root):
        if root==None:
            return
        self.inorder(root.left_child)
        print(root.info,end=" ")
        self.inorder(root.right_child)

    def postorder(self,root):
        if root==None:
            return
        self.inorder(root.left_child)
        self.inorder(root.right_child)
        print(root.info,end=" ")

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
'''
tree=Btnode('A') #root node as tree
tree.left_child=Btnode('B')
tree.right_child=Btnode('C')
tree.left_child.left_child=Btnode('D')
tree.left_child.right_child=Btnode('E')


bt=BinaryTree()
print("traversal of given tree is --> ",end='')
bt.postorder(tree)
