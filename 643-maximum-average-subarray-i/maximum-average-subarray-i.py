class Solution(object):
    def findMaxAverage(self, nums, k):
        n = len(nums)
        if n < k:
            return 0

        window_sum = sum(nums[:k])
        max_sum = window_sum

        for i in range(k,n):
            window_sum +=nums[i]-nums[i-k]
            max_sum = max(max_sum, window_sum)

        return float(max_sum)/k        