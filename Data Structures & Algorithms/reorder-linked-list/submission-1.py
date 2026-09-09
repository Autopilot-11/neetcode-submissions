# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        counter = 0 
        lst_node = []
        while head != None:
            lst_node.append(head)
            head = head.next
            counter += 1

        if counter % 2 == 0:
            front = lst_node[0:counter//2]
            back = lst_node[counter//2:]
            back.reverse()
        else:
            front = lst_node[0:counter//2+1]
            back = lst_node[counter//2+1:]
            back.reverse()
        
        new_head = ListNode()
        head = new_head
        for i in range(len(back)):
            new_head.next = front[i]
            new_head = new_head.next
            new_head.next = back[i]
            new_head = new_head.next
        
        if len(front) > len(back):
            new_head.next = front[-1]
            new_head = new_head.next
        
        new_head.next = None
        head = head.next
