class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        begin = 0
        end = len(nums) - 1
        if begin >= end:
            return nums[begin]
        m = self.partition(nums, begin, end)
        if m == k:
            return nums[m]
        elif m < k:
            return self.findKthLargest(nums[m+1:], k)
        else:
            return self.findKthLargest(nums[:m], k)

    def partition(self, arr, l, r):
        i = l
        while l < r:
            if arr[l] < arr[r]:
                arr[i], arr[l] = arr[l], arr[i]
                i += 1
            l += 1
        arr[l], arr[i], = arr[i], arr[l]
        return i
