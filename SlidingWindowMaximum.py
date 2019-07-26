class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        out = []
        if k > 1:
            for index, num in enumerate(nums):
                if index <= len(nums)-k:
                    out.append(max(nums[index:index+k]))
                else:
                    return out
        else:
            return nums
nums = [1,3,-1,-3,5,3,6,7]
k = 3

nums2 = [1]
k2 = 1

solution = Solution()

output = solution.maxSlidingWindow(nums, k)

print(output)

print(solution.maxSlidingWindow(nums2, k2))