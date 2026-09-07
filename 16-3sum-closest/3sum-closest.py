class Solution(object):
    def threeSumClosest(self, nums, target):
        if not nums:
            return 0

        nums.sort()
        res = float('inf')
        temp = 0

        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1

            while l < r:
                total = nums[i] + nums[l] + nums[r]

                if abs(target - total) < res:
                    res = abs(target - total)
                    temp = total

                if total < target:
                    l += 1

                elif total > target:
                    r -= 1

                else:
                    return total

        return temp