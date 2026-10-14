
class Solution(object):
    def fun(self, have, need):
        for i in range(256):
            if have[i] < need[i]:
                return False
        return True

    def minWindow(self, s, t):
        n = len(s)
        m = len(t)

        if n < m:
            return ""

        have = [0] * 256
        need = [0] * 256

        for i in range(m):
            need[ord(t[i])] += 1

        low = 0
        res = float('inf')
        start = -1

        for high in range(n):
            have[ord(s[high])] += 1

            while self.fun(have, need):
                length = high - low + 1

                if res > length:
                    res = length
                    start = low

                have[ord(s[low])] -= 1
                low += 1

        if start == -1:
            return ""

        return s[start:start + res]
