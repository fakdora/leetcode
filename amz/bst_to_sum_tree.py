#Given a Binary Search Tree (BST), convert it to a
# Greater Sum Tree such that every key of the original
# BST is changed to the original value plus sum of all
# values greater than the original key in BST.
# https://leetcode.com/problems/convert-bst-to-greater-tree/description/


'''
in order
    left, root, right
pre order
    root, left, right
post order
    left, right, root


# BST is changed to the original value plus sum of all
# values greater than the original key in BST.

rever inorder
    right root left?

'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.total = 0

    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode

        right doesn't change
        root = right + root
        left = right + root + left
        """
        if root is not None:
            self.convertBST(root.right)
            self.total += root.val
            root.val = self.total
            self.convertBST(root.left)


l = TreeNode(2)
right = TreeNode(13)
root = TreeNode(5)
root.left = l
root.right = right


sol = Solution()
print sol.convertBST(root)

def printinorder(root):
    if root is not None:
        printinorder(root.left)
        print root.val
        printinorder(root.right)
print '-----'
printinorder(root)
print '-----'

def traverse(rootnode):
  thislevel = [rootnode]
  while thislevel:
    nextlevel = list()
    for n in thislevel:
      print n.val,
      if n.left: nextlevel.append(n.left)
      if n.right: nextlevel.append(n.right)
    print
    thislevel = nextlevel


print traverse(root)
