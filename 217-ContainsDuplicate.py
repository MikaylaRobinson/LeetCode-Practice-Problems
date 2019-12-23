class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        frequency_tracking = {}
        for val in nums:
            if val not in frequency_tracking.keys():
                frequency_tracking[val] = 1
            else:
                return True
        return False