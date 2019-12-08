class Solution:
    def romanToInt(self, s: str) -> int:
        common = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        special = {
            "IV": 2,
            "IX": 2,
            "XL": 20,
            "XC": 20,
            "CD": 200,
            "CM": 200,
        }

        running_value = 0
        for char in range(len(s)):
            running_value -= special.get(s[char : char + 2], 0)
            running_value += common.get(s[char], 0)
        return running_value
        
class Solution:
    def romanToInt(self, s: str) -> int:
        numerals_to_integers = {'I': 1, 'V': 5, 'X': 10, 'L':50, 'C': 100, 'D': 500, 'M': 1000}
        string_as_list = list(s)
        running_value = 0
        for index, char in enumerate(string_as_list):
            running_value += numerals_to_integers.get(char)
            if (char == 'V' or char == 'X') and string_as_list[index - 1] == 'I':
                running_value -= 1
            elif (char == 'L' or char == 'C') and string_as_list[index - 1] == 'X':
                running_value -= 10
            elif (char == 'D' or char == 'M') and string_as_list[index - 1] == 'C':
                running_value -= 100
        return running_value
        
    
        