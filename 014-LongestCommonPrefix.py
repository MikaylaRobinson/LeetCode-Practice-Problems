def shorten_prefix(original_prefix, new_word):
    # Shorten words to the same length
    new_length = min(len(original_prefix), len(new_word))
    word_1 = original_prefix[:new_length]
    word_2 = new_word[:new_length]

    new_prefix = ''
    for char1, char2 in zip(word_1, word_2):
        if char1 == char2:
            new_prefix = new_prefix + char1
        else:
            break
    return new_prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        working_prefix = strs[0]
        for i in range(1, len(strs)):
            if working_prefix == "":
                return working_prefix
            else:
                working_prefix = shorten_prefix(working_prefix, strs[i])
        return working_prefix