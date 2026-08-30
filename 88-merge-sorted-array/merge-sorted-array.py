class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i = 0
        j = 0
        id = 0
        res = []

        while i < m and j < n:
            if nums1[i] < nums2[j]:
                res.append(nums1[i])
                id += 1
                i += 1
            else:
                res.append(nums2[j])
                id += 1
                j += 1

        while j < n:
            res.append(nums2[j])
            id += 1
            j += 1

        while i < m:
            res.append(nums1[i])
            id += 1
            i += 1

        for k in range(m + n):
            nums1[k] = res[k]