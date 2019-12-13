class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for index in range(-1, ((-1 * (len(digits))) - 1), -1):
            with_addition = digits[index] + 1
            if with_addition > 10:
                continue 
            elif with_addition == 10:
                digits[index] = 0
            else:
                digits[index] = with_addition
                return digits
        digits = [1] + digits
        return digits
