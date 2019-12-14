# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        current_node = head
        original_head = head
        while current_node.next:
            new_next = current_node.next.val
            while new_next == current_node.val:
                current_node.next = current_node.next.next
                if current_node.next is None:
                    return original_head

                new_next = current_node.next.val
            current_node = current_node.next
        return original_head