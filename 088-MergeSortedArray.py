class Solution:
    def merge(self, nums1, m, nums2, n) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_index = m - 1
        nums2_index = n - 1
        # Populate nums1 from the end of the list
        for i in reversed(range(0, len(nums1))):
            if nums1_index < 0:
                nums1[i] = nums2[nums2_index]
                nums2_index -= 1
                continue
            if nums2_index < 0:
                nums1[i] = nums1[nums1_index]
                nums1_index -= 1
                continue
            
            if nums1[nums1_index] > nums2[nums2_index]:
                nums1[i] = nums1[nums1_index]
                nums1_index -= 1
            else:
                nums1[i] = nums2[nums2_index]
                nums2_index -= 1
            