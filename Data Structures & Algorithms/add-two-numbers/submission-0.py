# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        coeff = 1
        num1 = 0 
        while l1:
            num1 += coeff * l1.val
            coeff *= 10
            l1 = l1.next
        
        coeff = 1
        num2 = 0
        while l2:
            num2 += coeff * l2.val
            coeff *= 10
            l2 = l2.next

        res = str(num1 + num2)
        dummy = ListNode()
        tail = dummy
        
        for i in range(len(res)-1,-1,-1):
            tail.next = ListNode(res[i])
            tail = tail.next
        
        return dummy.next

        