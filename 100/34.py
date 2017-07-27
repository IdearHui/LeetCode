class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ret = [-1, -1]
        if not nums:
            return ret
        l, r = 0, len(nums) - 1
        while l + 1 < r:
            mid = (l + r) / 2
            if nums[mid] >= target:
                r = mid
            else:
                l = mid
        if nums[l] == target:
            ret[0] = l
        elif nums[r] == target:
            ret[0] = r

        l, r = 0, len(nums) - 1
        while l + 1 < r:
            mid = (l + r) / 2
            if nums[mid] <= target:
                l = mid
            else:
                r = mid
        if nums[r] == target:
            ret[1] = r
        elif nums[l] == target:
            ret[1] = l
        return ret


if __name__ == "__main__":
    so = Solution()
    arr = [2, 2]
    res = so.searchRange(arr, 2)
    print(res)
