class Solution:
    def majorityElement(self, nums):
        def getMajorityElement(numbersSeen,maxNum):
            for key, value in numbersSeen.items():
                print(key, value)
                if value == maxNum:
                    return int(key)

        numbersSeen = {}
        for num in nums:
            if num not in numbersSeen:
                numbersSeen[num] = 1
            else:
                numbersSeen[num] += 1
        return getMajorityElement(numbersSeen, maxNum=max(numbersSeen.values()))

solution = Solution()

test = [3,2,4,4,2,2,333,2,1,1,333,1,3]

test2 = [2,2,1,1,1,2,2]

output = solution.majorityElement(test)

output2 = solution.majorityElement(test2)

print(test,"\nAnswer: ", output)

print(test2,"\nAnswer: ", output2)