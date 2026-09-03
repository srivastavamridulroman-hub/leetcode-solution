class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        n = len(nums)
        start = 0
        end = 0
        product = 1
        count = 0

        if k <= 1:
            return 0

        while end < n:
            product = product * nums[end]

            while product >= k:
                product = product // nums[start]
                start = start + 1

            count = count + (end - start + 1)

            end = end + 1

        return count