class Solution(object):
    def findMaxAverage(self, nums, k):
        total = 0
        res = 0
        n = len(nums)

        low = 0
        high = k

       
        for i in range(low, high):
            total = total + nums[i]

        res = total

        
        while high < n:
            total = total - nums[low]
            total = total + nums[high]

            res = max(res, total)

            low += 1
            high += 1

        return float(res) / k