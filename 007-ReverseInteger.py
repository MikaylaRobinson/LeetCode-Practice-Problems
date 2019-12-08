class Solution:
    def reverse(self, x: int) -> int:
        running_sum = 0
        
        is_negative = True if x < 0 else False

        if is_negative:
            x *= -1

        while x > 0:
            digit_to_add = x % 10
            x = x // 10
            running_sum *= 10
            running_sum += digit_to_add
            
        if is_negative:
            running_sum = running_sum * -1
        
        if running_sum not in range(-2 ** 31, 2 ** 31 - 1):
            return 0
        
        return running_sum
