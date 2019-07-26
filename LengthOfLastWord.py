class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or s == '':
            return 0
        else:
            print(len(s.split(' ')[-1]))
            return len([s.split(' ')][-1])

s = Solution()

test = "a"

length = s.lengthOfLastWord(test)

print(length)
