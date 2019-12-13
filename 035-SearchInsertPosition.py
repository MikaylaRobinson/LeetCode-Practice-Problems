class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target > nums[-1]:
            return len(nums)

        for index, num in enumerate(nums):
            if num >= target:
                return index
