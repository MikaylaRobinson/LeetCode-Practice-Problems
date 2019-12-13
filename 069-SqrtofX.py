class Solution:
    def mySqrt(self, x: int) -> int:
        square_root = 0
        while square_root**2 < x:
            square_root += 1
        if square_root **2 > x:
            square_root -= 1
        return square_root
