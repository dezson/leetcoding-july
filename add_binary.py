class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) > len(b):
            b = (len(a)-len(b)) * "0" + b
        elif len(b) > len(a):
            a = (len(b)-len(a)) * "0" + a

        carry_on = 0
        res = ""
        for i in range(len(a)-1,-1,-1):
            if int(a[i]) + int(b[i]) == 0:
                if carry_on == 0:
                    res = "0" + res
                else:
                    res = "1" + res
                    carry_on = 0

            elif int(a[i]) + int(b[i]) == 1:
                if carry_on == 0:
                    res = "1" + res
                else:
                    res = "0" + res
                    carry_on = 1

            elif int(a[i]) + int(b[i]) == 2:
                if carry_on == 0:
                    res = "0" + res
                    carry_on = 1
                else:
                    res = "1" + res
                    carry_on = 1


        return res if carry_on == 0 else "1" + res
