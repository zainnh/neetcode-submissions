class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        l = 0
        char = set()

        for r in range(len(s)):
            while s[r] in char:
                char.remove(s[l])
                l +=1
            char.add(s[r])
            maxLength = max(maxLength, (r - l) + 1)
        return maxLength

         
        
       