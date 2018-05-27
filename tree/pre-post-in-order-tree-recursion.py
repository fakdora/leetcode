class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def print_inorder(root):
    # l -> parent -> r
    if root:
        print_inorder(root.left)
        print(root.value)
        print_inorder(root.right)
        
def print_postorder(root):
    # l -> r -> parent
    if root:
        print_postorder(root.left)
        print_postorder(root.right)
        print(root.value)
        
def print_preorder(root):
    # l -> r -> parent
    if root:
        print(root.value)
        print_preorder(root.left)
        print_preorder(root.right)
    
# Driver code
root = Node(1)
root.left      = Node(2)
root.right     = Node(3)
root.left.left  = Node(4)
root.left.right  = Node(5)
#root.left.right.right  = Node(6)

print("\nPreorder traversal of binary tree is")
print_preorder(root)

print ("\nInorder traversal of binary tree is")
print_inorder(root)

print("\nPostorder traversal of binary tree is")
print_postorder(root)
