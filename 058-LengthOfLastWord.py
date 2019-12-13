class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        letter_counter = 0

        if s == "":
            return 0

        for char in reversed(s):
            if char != " ":
                letter_counter += 1
            elif char == " " and letter_counter > 0:
                break
        return letter_counter
    

