class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        set_version = set(nums)
        sum_of_set = sum(set_version)
        sum_of_original = sum(nums)
        return (2*sum_of_set - sum_of_original)
        