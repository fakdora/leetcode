
class Node():
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

root = Node(20)
root.left = Node(8)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left =  Node(10)
root.left.right.right = Node(14)
root.right = Node(22)
root.right.right = Node(25)

def print_level(node):

    if node is None:
        return

    curr_level = [node]
    to_print = []

    while curr_level:
        next_level = []
        for curr_node in curr_level:
            print curr_node.val,
            if curr_node.left is not None:
                next_level.append(curr_node.left)
            if curr_node.right is not None:
                next_level.append(curr_node.right)
        print

        curr_level = next_level

print_level(root)




