
class Solution(object):
    def minSubArrayLen(self, target, nums):
        n = len(nums)
        low = 0
        curr_sum = 0
        res = float('inf')

        for high in range(n):
            curr_sum += nums[high]

            while curr_sum >= target:
                length = high - low + 1
                res = min(res, length)

                curr_sum -= nums[low]
                low += 1

        if res == float('inf'):
            return 0

        return res
