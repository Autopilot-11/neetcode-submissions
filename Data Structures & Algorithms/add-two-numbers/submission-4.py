# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            digit = l1.val + l2.val + carry
            if digit >= 10:
                tail.next = ListNode(digit - 10)
                carry = 1
                tail = tail.next
                l1 = l1.next
                l2 = l2.next
            else:
                tail.next = ListNode(digit)
                carry = 0
                tail = tail.next
                l1 = l1.next
                l2 = l2.next
        
        while l1:
            total = l1.val + carry
            carry = total // 10
            tail.next = ListNode(total % 10)

            tail = tail.next
            l1 = l1.next
        
        while l2:
            total = l2.val + carry
            carry = total // 10 
            tail.next = ListNode(total % 10)

            tail = tail.next
            l2 = l2.next
        
        if carry == 1:
            tail.next = ListNode(1)
        
        return dummy.next
        


        # Reconstruction method
        # coeff = 1
        # num1 = 0 
        # while l1:
        #     num1 += coeff * l1.val
        #     coeff *= 10
        #     l1 = l1.next
        
        # coeff = 1
        # num2 = 0
        # while l2:
        #     num2 += coeff * l2.val
        #     coeff *= 10
        #     l2 = l2.next

        # res = str(num1 + num2)
        # dummy = ListNode()
        # tail = dummy
        
        # for i in range(len(res)-1,-1,-1):
        #     tail.next = ListNode(res[i])
        #     tail = tail.next
        
        # return dummy.next

        