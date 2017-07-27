class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i, n in enumerate(nums):
            if n >= target:
                return i
        else:
            return len(nums)