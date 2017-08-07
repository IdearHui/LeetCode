class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sums = 0
        nums.sort()
        for n in range(len(nums)):
            if n % 2 == 0:
                sums += nums[n]
        return sums
