class Solution(object):
    def moveZeroes(self, nums):
        j = -1

        for i in range(len(nums)):
            if nums[i] == 0:
                j = i
                break

        # No zero found
        if j == -1:
            return

        for i in range(j + 1, len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1