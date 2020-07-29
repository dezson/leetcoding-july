import re

class Solution:
    def reverseWords(self, s: str) -> str:
            s = s.split(' ')[::-1]
            s = ' '.join(s).strip()
            return re.sub(' +',' ',s)
