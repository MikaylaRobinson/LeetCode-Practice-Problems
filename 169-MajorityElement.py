class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        majority_indicator = len(nums) / 2
        value_frequencies = {}
        for num in nums:
            if num in value_frequencies:
                value_frequencies[num] += 1
                if value_frequencies.get(num) > majority_indicator:
                    return num
            else:
                value_frequencies[num] = 1