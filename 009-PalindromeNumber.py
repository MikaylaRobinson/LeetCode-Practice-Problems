class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        original_integer = x
        running_sum = 0
        while x > 0:
            digit_to_add = x % 10
            x = x // 10
            running_sum *= 10
            running_sum += digit_to_add

        if original_integer == running_sum:
            return True