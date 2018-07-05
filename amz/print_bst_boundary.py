class Node():
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None
    def __str__(self):
        return str(self.val)

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


root = Node(20)
root.left = Node(8)
root.left.left = Node(4)
root.left.right = Node(12)

root.left.left.right = Node(41)
root.left.left.right.left = Node(42)
root.left.left.right.right = Node(43)

root.left.left.right.left.left = Node(422)
root.left.left.right.left.right = Node(423)

root.left.right.left =  Node(10)
root.left.right.right = Node(14)
root.left.right.left.left =  Node(9)

root.left.right.right = Node(14)
root.left.right.right.left = Node(13)
root.left.right.right.right = Node(17)
root.left.right.right.right.right = Node(18)
root.right = Node(22)
root.right.right = Node(25)

print_level(root)


def printLeaves(root):
    if(root):
        printLeaves(root.left)

        # Print it if it is a leaf node
        if root.left is None and root.right is None:
            print root.val,

        printLeaves(root.right)

# A function to print all left boundary nodes, except a
# leaf node. Print the nodes in TOP DOWN manner
def printBoundaryLeft(root):

    if(root):
        if (root.left):

            # to ensure top down order, print the node
            # before calling itself for left subtree
            print root.val,
            # if root.val == 42: print 'found 1'
            printBoundaryLeft(root.left)

        elif(root.right):
            print root.val,
            # if root.val == 42: print 'found'
            printBoundaryRight(root.right)

        # do nothing if it is a leaf node, this way we
        # avoid duplicates in output


# A function to print all right boundary nodes, except
# a leaf node. Print the nodes in BOTTOM UP manner
def printBoundaryRight(root):

    if(root):
        # if root.val == 41:
        #     print 'hey'


        if (root.right):
            # to ensure bottom up order, first call for
            # right subtree, then print this node
            # print 'r.right: ' + str(root.right.val)
            printBoundaryRight(root.right)
            print root.val,

        elif(root.left):
            # print 'r.left: ' + str(root.left.val)
            printBoundaryRight(root.left)
            print root.val,

        # do nothing if it is a leaf node, this way we
        # avoid duplicates in output


# A function to do boundary traversal of a given binary tree
def printBoundary(root):
    if (root):
        print root.val,

        # Print the left boundary in top-down manner
        printBoundaryLeft(root.left)

        # Print all leaf nodes
        printLeaves(root.left)
        printLeaves(root.right)

        # Print the right boundary in bottom-up manner
        printBoundaryRight(root.right)

print
printBoundary(root)

