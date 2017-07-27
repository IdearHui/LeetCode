import collections


class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = collections.Counter(nums)
        for k, v in dic.items():
            if v > 1:
                return v
