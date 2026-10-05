class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        n = len(fruits)
        low = 0
        res = -1
        freq = {}

        for high in range(n):

            # Add current fruit
            freq[fruits[high]] = freq.get(fruits[high], 0) + 1

            # Shrink window if we have more than 2 types
            while len(freq) > 2:
                freq[fruits[low]] -= 1

                if freq[fruits[low]] == 0:
                    del freq[fruits[low]]

                low += 1

            # Current valid window
            res = max(res, high - low + 1)

        return res