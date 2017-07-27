import collections


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        intersections = dict(collections.Counter(nums1) & collections.Counter(nums2))
        ret = []
        for k, v in intersections.items():
            ret += [k for i in range(v)]
        return ret