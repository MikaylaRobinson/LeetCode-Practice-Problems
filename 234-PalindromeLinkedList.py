class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        list_version = []

        while head:
            list_version.append(head.val)
            head = head.next

        for i in range(0, ((len(list_version))// 2)):
            if list_version[i] != list_version[~i]:
                return False
        return True
