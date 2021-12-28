# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        local = ListNode(-999)
        temp_local = local
      
        while(list1 or list2):
            if list1 and list2:
                if list1.val < list2.val:
                    local.next = ListNode(list1.val)
                    local = local.next
                    list1 = list1.next
                else:
                    local.next = ListNode(list2.val)
                    local = local.next
                    list2 = list2.next
            elif list1:
                local.next = ListNode(list1.val)
                local = local.next
                list1 = list1.next
            else:
                local.next = ListNode(list2.val)
                local = local.next
                list2 = list2.next
        

        
        return temp_local.next
