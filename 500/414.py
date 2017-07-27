class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for n in nums:
            if n in dic.keys():
                dic[n] += 1
            else:
                dic[n] = 1
        dic_nums = dic.keys()
        dic_nums = sorted(dic_nums)[::-1]
        if len(dic) > 2:
            return dic_nums[2]
        return dic_nums[0]


if __name__ == "__main__":
    s = Solution()
    nu = [1,2,3,3,4]
    res = s.thirdMax(nu)
    print(res)
