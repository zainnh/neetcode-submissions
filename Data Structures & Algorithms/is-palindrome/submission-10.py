class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""                        #new string to compare without special char

        for char in s:                      #run the loop for the string s
            if char.isalnum():              # isalnum is only takes in numbers or letters
                cleaned += char.lower()     

        left = 0                            #left side index
        right = len(cleaned) - 1            #right side index

        while left < right:                 #left before right
            if cleaned[left] != cleaned[right]: #if left character is != to right
                return False                

            left += 1                       #move by +1
            right -= 1                      #move by -1

        return True