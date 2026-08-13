# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        left = list1
        right = list2
        temp = ListNode()
        cur = temp

        while left is not None or right is not None:
            if left is None:
                cur.next = right
                right = right.next
            elif right is None:
                cur.next = left
                left = left.next
            elif left.val <= right.val:
                cur.next = left
                left = left.next
            elif left.val > right.val:
                cur.next = right
                right = right.next
            cur = cur.next

        return temp.next


        