class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        def intoByte(n):
            ret = []
            while n != 0:
                if n % 2 == 0:
                    ret = [0] + ret
                else:
                    ret = [1] + ret
                n = n // 2
            return ret

        fst = intoByte(x)
        snd = intoByte(y)

        padding = max(len(fst), len(snd))
        if len(fst) < len(snd):
            fst = ([0] * (padding - len(fst))) + fst
        elif len(fst) > len(snd):
            snd = ([0] * (padding - len(snd))) + snd

        hamming_dist = 0
        for i in range(len(fst)):
            if fst[i] != snd[i]:
                hamming_dist += 1
        return hamming_dist
