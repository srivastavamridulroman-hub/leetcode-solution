class Solution(object):
    def minSubArrayLen(self, target, nums):
        n = len(nums)
        low = 0
        high = 0
        total = 0
        res = float('inf')

        while high < n:
            total = total + nums[high]

            while total >= target:
                length = high - low + 1
                res = min(res, length)

                total = total - nums[low]
                low = low + 1

            high = high + 1

        if res == float('inf'):
            return 0
        return res