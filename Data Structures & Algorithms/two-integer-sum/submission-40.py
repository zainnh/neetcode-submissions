"""
[Hi chat! Plz don't delete!] 

///////////////////////////////////What the Question is Asking////////////////////////////////////////////

So basically we are given an array of integers assigned to the variable name 'nums'. We are also given some integer 
assigned to the variable 'target'. Based on the integers in "nums", what two numbers in "nums" equals to the integer "target". 
The return/output is simply [i,j] where nums[i] + nums[j] = target. Notice we are not being asked what two numbers in 
nums gives us the target but rather the indices of the two numbers that gives us target. 

///Solution Explained///

1. create a hashmap called prevMap where key -> number seen and value -> index
2. i = index, n = value, enumerate in general is used when we want an index and a value. loop/enumerate through nums 
3. as we go through each value in nums, if target - n exists in hashmap then we have found two values that equal target (diff, n). 
4. if diff doesnt exist in hashamp, we simply add whatever n we are on into hashmap and repeat 
5. return prevMap[diff] -> gives us index of working value and i -> index of original value (the one we comparing it to)

"""""

#Trace nums = [4,5,6], target = 10

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      prevMap = {} #empty hashmap

      for idx, val in enumerate(nums): #idx: 0, val: 4 | idx: 1, val: 5 | idx: 2, val: 6 
        diff = target - val # 6 = 10 - 4 | 5 = 10 - 5 | 4 = 10 - 6 

        if diff in prevMap: #empty hashmap, 6 not inside (false) | check if 5 is inside (false) | check if is inside (true)
            return [prevMap[diff], idx] # prevMap[diff] = prevMap[4] = 0 and idx of current/comparison = 2 so output: [0,2]

        prevMap[val] = idx #updated hashmap (flip idx and value since we want index)
                           # {key: 4 value: 0}
                           # {key: 5, value: 1}


''' 



'''



        