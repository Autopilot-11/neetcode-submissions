# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        slow = head
        counter = 0

        # Edge case check: remove the entire list:
        if fast.next is None and n == 1:
            head = head.next
            return head

        while counter < n:
            fast = fast.next
            counter += 1

        if fast is None:
            head = head.next
            return head

        while fast.next:
            fast = fast.next
            slow = slow.next
            print(slow.val)

        slow.next = slow.next.next
        
        return head

        
        