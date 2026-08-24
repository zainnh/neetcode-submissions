"""
#What is Question Asking: 

So we are essentially given some array "nums". We return true if some value appears more than once in array. If "nums" doesn't have repeating value we return false. The objective is to create some algorithm where regardless of what array we are given we can see if a duplicate exists. 


Solution/Code Explained: 

class Solution: 
    def hasDuplicate(self, nums: List[int]) -> bool:

[We define a function called hasDuplicate that takes a list of integers called "nums" where the final return statement should be a boolean (true or false). The 'self' part is not important to know. We can think of it as a necessary covention since the fucntion exists inside the class. It is fair to internalize this as def hasDuplicate(nums): for better understanding.]

hashset = set()

[hashset is simply a variable name. We could name it as seen = set() and it means the same thing. hashset is not some special python syntax. The following just creates an empty set under the variable name hashset.
Note: (we usually use a hashset to see whether an item exists; hashmap to see key/value lookup.)] 

for n in nums: 
    if n in hashset: 
        return True 
    hashset.add(n)

return False 

[(ln:19) We loop through all elements in num (the given array) one at a time starting at index 0. (ln: 20-22) For each n in nums, we compare it to our current hashset to see if that n already inside. If not we then add that number to the hashset, and continue for all remaining n. Once we reach the end of nums and no duplicate/true has been run, we deafault to return False.] 

Consider the example: nums = [1,2,3,3]

[We start at index[0] which is 1 and then see if n (1) is in hashset ({}). Since our hashset is curently empty, we can add 1 to the set and continue to next n in nums. So currently set looks like {1}. Then we go to index[1] and see if n (2) is in hashset {1} (No). Add that n to hashset. Then we go to index[2] (3), and see if n in hashset. No. Add that n to hashset. Index[3] (3) and see if n is in hashset. Yes this time we do see n in the hashset 3 is in {1,2,3}, and return True. In the scenario where index[3] was say value: 4, we would return False, as we looped through all n in num and no n was in hashset.] 

"""

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums: 
            if n in hashset:
                return True 
            hashset.add(n)
        return False




        