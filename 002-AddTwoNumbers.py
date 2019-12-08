# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        output_list = None      
        carry_over = 0
        first_node = None

        while l1 or l2:
            value = carry_over
            
            if l1 is not None:
                value += l1.val
            if l2 is not None:
                value += l2.val
            
            carry_over = value // 10
            digit = value % 10

            if output_list is None:
                output_list = ListNode(digit)
                first_node = output_list
            else:
                next_digit = ListNode(digit)
                output_list.next = next_digit
                output_list = output_list.next 
            
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
            
        if (carry_over > 0):
            next_digit = ListNode(carry_over)
            output_list.next = next_digit
            output_list = output_list.next 
            
        return first_node