# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# 
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        # go through the first list
        # as well as the second list
        # add its values together
        # if it's > 10, then get the first digit
        # and remember the 10 and add 1 to the following node
        # if one of the list is empty, just add it to 0
        
        total = 0
        carry = 0
        new_list_root = ListNode(0)
        curr_head = new_list_root
        
        
        # here, if you go l1.next is not None, then it will skip the last one
        while l1 is not None or l2 is not None:
            
            # access value only when current node is not None
            l1_val = 0 if l1 is None else l1.val                
            l2_val = 0 if l2 is None else l2.val
            total = l1_val + l2_val + carry
            
            if total >= 10:
                carry = 1
                total = total - 10
            else:
                carry = 0
                
            # assign next only when it's not None
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
            curr_head.next = ListNode(total)
            curr_head = curr_head.next
        
        if carry == 1:
            curr_head.next = ListNode(1)
            
        
        return new_list_root.next
            
def printList(l):
    node = l
    res = []
    while node is not None:
        res.append(str(node.val))
        node = node.next
    
    print ("->".join(res))            
        

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)



l1 = ListNode(1)
l1.next = ListNode(8)

l2 = ListNode(0)

sol = Solution()
a = sol.addTwoNumbers(l1, l2)
printList(a)
    
printList(l1)

