class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        for i in range(n):
            if (i+1) % 3 == 0 and (i+1) % 5 != 0:
                result.append("Fizz")
            elif (i+1) % 5 == 0 and (i+1) % 3 != 0:
                result.append("Buzz")
            elif (i+1) % 3 == 0 and (i+1) % 5 == 0:
                result.append("FizzBuzz")
            else:
                result.append(str(i+1))
        return result

if __name__ == "__main__":
    s = Solution()
    r = s.fizzBuzz(1)
    print(r)
