class Solution:
    def majorityElement2(self, nums):
        out = []
        numbersSeen = {}
        for num in nums:
            if num not in numbersSeen:
                numbersSeen[num] = 1
            else:
                numbersSeen[num] += 1
            if numbersSeen[num] > len(nums)/3 and num not in out:
                out.append(num)
        return out

solution = Solution()

test = [3,2,4,4,2,2,333,2,1,1,333,1,3]

test2 = [2,2,1,1,1,2,2]

output = solution.majorityElement2(test)

output2 = solution.majorityElement2(test2)

print(test,"\nAnswer: ", output)

print(test2,"\nAnswer: ", output2)