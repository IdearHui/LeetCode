class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        res = triangle[-1]
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                res[j] = min(res[j], res[j+1]) + triangle[i][j]
        return res[0]

if __name__ == "__main__":
    s = Solution()
    tri = [[2], [3, 4], [6, 5, 7], [1, 4, 8, 3]]
    tri1 = [[]]
    result = s.minimumTotal(tri)
    print(result)