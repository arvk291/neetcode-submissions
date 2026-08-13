# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head:
            h, t = head, head.next
            while t is not None:
                if h==t:
                    return True
                h = h.next
                if t.next is not None:
                    t = t.next.next
                else:
                    return False
            
        return False