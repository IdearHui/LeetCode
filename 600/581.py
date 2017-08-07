class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right, n = -1, -2, len(nums)-1
        min_v, max_v = nums[-1], nums[0]
        for i in range(1, len(nums)):
            max_v = max(max_v, nums[i])
            min_v = min(min_v, nums[n-i])
            if nums[i] < max_v:
                right = i
            if nums[n-i] > min_v:
                left = n - i
        return right - left + 1


if __name__ == "__main__":
    so = Solution()
    arr = [1, 3, 2, 2, 2]
    res = so.findUnsortedSubarray(arr)
    print(res)
