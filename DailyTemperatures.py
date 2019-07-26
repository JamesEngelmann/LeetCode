class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        def daysTillWarmerTemp(currentTemp, daysAfter):
            for daysSince, dayTemp in enumerate(daysAfter,1):
                if dayTemp > currentTemp:
                    return daysSince
        
        daysTill = []
        for day, temp in enumerate(T):
            if day+1 < len(T) and max(T[day+1:]) > temp:
                daysTill.append(daysTillWarmerTemp(temp, T[day+1:]))
            else:
                daysTill.append(0)
        
        return daysTill

T = [21, 31, 41]

solution = Solution()

print(solution.dailyTemperatures(T))