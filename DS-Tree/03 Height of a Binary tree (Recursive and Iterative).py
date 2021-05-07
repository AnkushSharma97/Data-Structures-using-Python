class TreeNode:
    def __init__(self,data):
        self.info=data
        self.left=None
        self.right=None

class BinaryTree:
    def height_recursive(self,root):
        if root is None:
            return -1
        else:
            left_height= self.height_recursive(root.left)
            right_height= self.height_recursive(root.right)
            if left_height>right_height:
                return (1+left_height)
            else:
                return(1+right_height)

    def height_iterative(self,root):
        current = root
        stack=[]
        height=-1
        max_height=-1
        last_visited=None
        while True:
            if current is not None:
                stack.append(current)
                height+=1
                if max_height<height:
                    max_height=height
                current=current.left
            elif len(stack)!=0:
                current=stack.pop()
                height-=1
                if current.right is not None and current.right !=last_visited:
                    stack.append(current)
                    current=current.right
                    height+=1
                    if max_height<height:
                        max_height=height
                else:
                    last_visited=current
                    current=None
                      
            else:
                break   
        return(max_height)


root = TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.right.left=TreeNode(4)

bt= BinaryTree()
print(bt.height_recursive(None))
print(bt.height_iterative(None))
