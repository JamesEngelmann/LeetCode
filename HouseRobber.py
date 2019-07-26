import itertools

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        for index, num in enumerate(nums):
            if nums[index+1] > num and index <= len(nums):
                

solution = Solution()

test = [2,7,9,3,1]

out = solution.rob(test)

print(out)