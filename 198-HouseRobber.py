class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        elif len(nums) == 1:
            return nums[0]
        
        elif len(nums) == 2:
            return max(nums)

        max_log = [nums[0], max(nums[0], nums[1])]

        for i in range(2, len(nums)):
            max_log.append(max(max_log[i-2] + nums[i], max_log[i-1]))
        return max_log[-1]