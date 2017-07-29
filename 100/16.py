class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3:
            return 0
        elif len(nums) == 3:
            return sum(nums)
        nums.sort()
        minVal = 1000000
        result = 0
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                tmp = nums[i] + nums[left] + nums[right]
                if abs(tmp-target) < minVal:
                    minVal = abs(tmp-target)
                    result = tmp
                if tmp == target:
                    return target
                if tmp > target:
                    right -= 1
                else:
                    left += 1
        return result


if __name__ == "__main__":
    s = Solution()
    arrs = [-1, 2, 1, -4]
    res = s.threeSumClosest(arrs, 1)
    print(res)
