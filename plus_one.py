class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1]+=1
        load = 0
        for x in range(len(digits)-1,-1,-1):
            digits[x]+=load
            if digits[x] >= 10:
                digits[x] = 0
                load = 1
            else:
                load = 0
                break

        if load != 0:
            digits = [1] + digits
        return digits