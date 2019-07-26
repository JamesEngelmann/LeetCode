class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def calculateCoins(left,center,right):
            return left*center*right

        coins = []
        tempNums = nums

        if ((len(nums) >= 0 and len(nums) <= 500) and
            (max(nums) >= 0 and max(nums) <= 100)):
            print("Length of Nums: ", len(nums))
            while len(coins) <= len(nums):
                loopCoins = []
                print(tempNums)
                for n, num in enumerate(tempNums):
                    if len(nums) == 1:
                        loopCoins.append(calculateCoins(left=1,
                                                        center=num,
                                                        right=1))
                    elif n == 0:
                        loopCoins.append(calculateCoins(left=1,
                                                        center=num,
                                                        right=tempNums[n+1]))
                    elif n == len(tempNums)-1:
                        loopCoins.append(calculateCoins(left=tempNums[n-1],
                                                        center=num,
                                                        right=1))
                    else:
                        loopCoins.append(calculateCoins(left=tempNums[n-1],
                                                        center=num,
                                                        right=tempNums[n+1]))
                    print("Loop Coins: ", loopCoins)
                coins.append(max(loopCoins))
                tempNums.pop(loopCoins.index(max(loopCoins)))
            return max(coins)

test = [3,1,5,8]

solution = Solution()

print(solution.maxCoins(test))