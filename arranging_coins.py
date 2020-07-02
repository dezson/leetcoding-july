class Solution:
    def arrangeCoins(self, n: int) -> int:
        lo = 0
        hi = n
        while hi >= lo:
            k = lo + (hi - lo) // 2
            curr = k * (k + 1) // 2
            if curr == n:
                return k
            if curr > n:
                hi = k - 1
            else:
                lo = k + 1
        return hi

    def arrangeCoinsSlow(self, n: int) -> int:
        i = 0
        c = 0
        while True:
            i += 1
            c += i
            if c < n:
                continue
            elif c == n:
                return i
            else:
                return i - 1
