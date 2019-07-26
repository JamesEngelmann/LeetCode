class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.insert(0,x)

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop(0)

    def top(self):
        """
        :rtype: int
        """
        return self.stack[0]

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.stack)


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
print(obj.stack)
obj.push(0)
print(obj.stack)
obj.push(-3)
print(obj.stack)
print("Min: ", obj.getMin())
obj.pop()
print(obj.stack)
print("Top: ", obj.top())
print("Min: ", obj.getMin())
