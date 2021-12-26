# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pointer = pointer_2 = head
        
        for i in range(n):
            pointer = pointer.next
            
        while pointer and pointer.next:
            pointer = pointer.next
            pointer_2 = pointer_2.next
            
        if pointer:
            pointer_2.next = pointer_2.next.next
            
        else:
            head = head.next
            
                
            
            
        
        return head
            
            
            