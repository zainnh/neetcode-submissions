class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen_s = {}
        seen_t = {}        

        if len(s) != len(t):
            return False

        for letter_s in s:
            if letter_s in seen_s:
                seen_s[letter_s] += 1
            else:
                seen_s[letter_s] = 1
        
        for letter_t in t:
            if letter_t in seen_t:
                seen_t[letter_t] += 1;
            else:
                seen_t[letter_t] = 1;

        return seen_s == seen_t
        


            
                
            
                
                


        