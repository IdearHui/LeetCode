class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) > 10000:
            return -1
        count = 0
        res = 0
        for index, n in enumerate(nums):
            if n == 1:
                count += 1
                if index == len(nums)-1:
                    if count > res:
                        res = count
            else:
                if count > res:
                    res = count
                count = 0
        return res

if __name__ == "__main__":
    s = Solution()
    lists = [1, 1, 0, 1, 1, 1]
    result = s.findMaxConsecutiveOnes(lists)
    print(result)
