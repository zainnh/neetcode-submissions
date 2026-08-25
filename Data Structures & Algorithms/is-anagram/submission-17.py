""" 
Recall: A hashmap is pretty much a table that stores things by key, value. We can also call this a dictionary/dict.
We typically use a hashmap -> fast key/value lookup. 

/////////////////////////////////////////////// What is Question Asking: /////////////////////////////////////////////////////////

We are basically given two strings represented by the variable s and the variable t. 
The goal is to see if s and t have the exact same amount of numerical characters 
for all characters in s and t. For example the word rat, has: 1 'r', 1 'a', and 1 't'. 
This means that whatever the other string we are comparing to must also have 1 'r', 1 'a' and 1 't'. 
A valid example can be the word "tar". You may also notice that by using only string "s" characters we can pretty much write string "t" using only the characters "s" has. 

////////////////////////////////////// Solution/Code Explained:////////////////////////////////////////////////////////////////

Here is the general idea to the solution: We count every letter in s, count every letter in t, and see if the two count ups match. 

ex: "anagram" → {a:3, n:1, g:1, r:1, m:1} |     Since all 'a','n','g','r', and 'm' match in values,
    "nagaram" → {a:3, n:1, g:1, r:1, m:1} |     statement returns true. 

Since we previously discussed that we can create "t" from "s", its fair to say that "t" and "s" contain the same amount of characters. So 
we can start the soution with an edge case where if the lengths are the not same, we immediately return False. 

code: if len(s) != len(t): 
        return False 

Now that the edge case is out the way. We start the actual solution by creating two empty hashmaps/dict for "s" and "t". 

code: countS, countT = {}, {} 

Essentially these two empty dicts will hold letter and count (key, value). Right now its empty as we haven't seen any letters yet. We 
then walk through both strings one letter at a time. Since we however proved that both lengths are the same, we only need one loop, where we loop through i indices for s, where index i can point to both strings at once. 

#This creates a loop that is as long as s, going one index at a time. 
code: for i in range(len(s)) 

Inside the loop we are basically defining key -> value for the two empty hashmaps CountS and CountT that we made earlier. We loop through all i in s and t, where s[i] becomes our key. The value is created by adding 1 to .get(s[i]). So suppose our loop start at s[0] for some s.
Whatever char s[0] represents does not have any value assigned to it so the value is 0, however the expression is 1 + .get(s[i]), so the value is actually 1. Now in our hashmap we have the key: a, value: 1. Now suppose s[1] is also a, since the key: a, already has value: 1, .get(s[1]) will get that value of 1 and then we add another 1 to it so new value: 2. You may notice in the code it says countS.get(s[i], 0). The 0 after s[i] is the part of the code that tells us that whatever char s[i] represents, its value: 0. If nothing can be extracted from get, and since the hashmap we created is an empty hashmap, all starting count for each character will hit that 0. 

code: countS[s[i]] = 1 + countS.get(s[i], 0)
      countT[t[i]] = 1 + countT.get(t[i], 0)

Now what our code has done is essentially created two hashmaps for both s and t. If both hashmaps are the same, then we know the two strings 
are anagrams of each other. However if they are not the same, we know they cannot be anagrams of each other. 

code: return CountS == CountT 


////////////////////////////////////////////////////Time/Space Complexity:(simply)//////////////////////////////////////////////////

Time: How many times you do something (runtime)
Space: How many things you are holding (memory usage)

Calculate Time: 
Lets look at every letter in string. String is 7 letters -> run/loop 7 times. String is 50,000 letter -> run 50,000 times. 
In [ln: 80-82] we can see why this statement holds, so therefore time complexity is O(n) as the amount of times it loops is completely 
dependant on how long the strings are. 

Calculate Space Complexity: 
Now lets look at the two dicts/hashmaps we created. The constraints as defined in the problem says s and t can only conist of lowercase
letters. There are 26 letters in the alphabet meaning the amount of keys is locked at 26 for its maximum. The only thing that can change is the value of these keys (ex: 50,000). Since the amount of keys is locked and doesn't grow with some n input, Space Complexity would be O(1). 

So time complexity is O(n), while space complexity is O(1). 


""" 


class Solution: 
    def isAnagram(self, s: str, t: str) -> bool: #define function
    #edge case 
        if len(s) != len(t): 
            return False 

        #create empty hashmap
        countS, countT = {}, {}

        #create valid hashmap for s and n
        for i in range(len(s)): 
            countS[s[i]] = 1 + countS.get(s[i],0)
            countT[t[i]] = 1 + countT.get(t[i],0)

        #are both hashmap the same 
        return countS == countT

""" 
Note: We could also technically sort both strings in alphabetical order and see if both sorted strings are
the same, but worse runtime of O(n log n) and O(n) space. You could also swap the dict for a size 26 array to skip hashing overhead and
it'll run a bit faster in practice (same time and space complexity though). Wont go much into depth for that but good to know ig. """ 

        