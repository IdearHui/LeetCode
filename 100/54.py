class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return None
        rows = len(matrix)
        cols = len(matrix[0])
        start = 0
        result = []
        while rows > 2*start and cols > 2*start:
            end_x = rows-1-start
            end_y = cols-1-start
            for i in range(start, end_y+1):
                result.append(matrix[start][i])
            if start < end_x:
                for i in range(start+1, end_x+1):
                    result.append(matrix[i][end_y])
            if start < end_x and start < end_y:
                for i in range(end_y-1, start-1, -1):
                    result.append(matrix[end_x][i])
            if start < end_x-1 and start < end_y:
                for i in range(end_x-1, start, -1):
                    result.append(matrix[i][start])
            start += 1
        return result


if __name__ == "__main__":
    s = Solution()
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    res = s.spiralOrder(mat)
    print(res)
