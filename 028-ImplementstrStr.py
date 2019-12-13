class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == haystack:
            return 0

        for i in range(0, len(haystack) - len(needle) + 1):
            needle_length = len(needle)
            if needle == haystack[i: i + needle_length]:
                return i 
        return -1
