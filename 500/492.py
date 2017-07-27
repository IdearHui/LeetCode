import math


class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        MAX = 10000001
        result_list = []
        result = []
        if area > MAX:
            return []
        if area > 1:
            r = int(math.floor(math.sqrt(area)))
            for i in range(2, r+1):
                if (area % i) == 0:
                    result_list.append([area // i, i])
        for index, r_l in enumerate(result_list):
            if r_l[0] >= r_l[1]:
                dist = abs(r_l[0]-r_l[1])
                if dist < MAX:
                    MAX = dist
                    result = result_list[index]
        if len(result_list) == 0:
            return [area, 1]
        return result

if __name__ == "__main__":
    s = Solution()
    res = s.constructRectangle(10000000)
    print(res)
