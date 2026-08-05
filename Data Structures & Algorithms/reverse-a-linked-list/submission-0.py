from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base Case: If list is empty or has only one node, it's already reversed.
        if not head or not head.next:
            return head
        
        # Recursive Step: Reverse the rest of the list (starting from the second node).
        # 'new_head' will be the last node of the original list (the new head).
        new_head = self.reverseList(head.next)
        
        # Re-linking: 
        # head.next is currently the last node of the reversed sublist.
        # Make that node point back to the current 'head'.
        head.next.next = head
        
        # Break the old link to prevent cycles (current head becomes the new tail).
        head.next = None
        
        # Return the new head of the fully reversed list.
        return new_head   