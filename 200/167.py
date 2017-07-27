class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(numbers) < 2:
            return [1]
        end = len(numbers) -1
        for index, num in enumerate(numbers):
            if num > target:
                end = index
        left = 0
        right = end
        while numbers[left] + numbers[right] != target and left < right:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
        return [left+1, right+1]

if __name__ == "__main__":
    s = Solution()
    nums = [2, 3]
    tar = 2
    res = s.twoSum(nums, tar)
    print(res)