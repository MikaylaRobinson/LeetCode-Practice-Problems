class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        working_max = float("-inf")
        if len(nums) == 1:
            return nums[0]
        for index, num in enumerate(nums):
            for i in range(index + 1, len(nums) + 1):
                current_sub_array = nums[index:i]
                current_sum = sum(current_sub_array)
                if current_sum > working_max:
                    working_max = current_sum
        return working_max