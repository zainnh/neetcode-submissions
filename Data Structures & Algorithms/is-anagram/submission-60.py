class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        freq1, freq2 = {}, {}

        for _ in range(len(s)):
            freq1[s[_]] = 1 + freq1.get(s[_], 0)
            freq2[t[_]] = 1 + freq2.get(t[_], 0)
        return freq1 == freq2