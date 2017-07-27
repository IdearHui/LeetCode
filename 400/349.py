import collections


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return (collections.Counter(nums1) & collections.Counter(nums2)).keys()

if __name__ == "__main__":
    s = Solution()
    n1 = [1, 2, 3, 3]
    n2 = [3, 3]
    res = s.intersection(n1, n2)
    print(res)
