class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if (not self.minStack) or (x <= self.minStack[-1]):
            self.minStack.append(x)
        else:
            self.minStack.append(self.minStack[-1])
        self.stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        self.minStack.pop()
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[0]

    def getMin(self):
        """
        :rtype: int
        """
        if self.minStack:
            return self.minStack[0]


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(1)
obj.push(2)
obj.push(3)
print(obj.getMin())
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
