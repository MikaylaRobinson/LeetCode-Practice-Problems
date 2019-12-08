# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        combined_list = None
        next_value = None
        first_node = None
        
        while l1 or l2:
            if l1 is None:
                next_value = l2.val
                l2 = l2.next
            elif l2 is None:
                next_value = l1.val
                l1 = l1.next
            elif l1.val <= l2.val:
                next_value = l1.val
                l1 = l1.next
            elif l1.val > l2.val:
                next_value = l2.val
                l2 = l2.next

            if combined_list is None:
                combined_list = ListNode(next_value)
                first_node = combined_list
            else: 
                next_digit = ListNode(next_value)
                combined_list.next = next_digit
                combined_list = combined_list.next
        return first_node
