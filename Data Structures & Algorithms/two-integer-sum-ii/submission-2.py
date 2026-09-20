# list is sorted so two pointer method

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0                    #iniate left pointer
        right = len(numbers) - 1    #iniate right pointer

        while left < right:         # problem states left has to be less than right
            Answer = numbers[left] + numbers[right] # this is to find target

            if Answer == target:
                return [left + 1, right + 1] #returns the index of indicies but we don't want it at 0
            
            elif Answer < target:      # move left pointer up one
                left += 1
            
            else:
                right -= 1      # move right pointer down 1 
                                # no need for return -1 or anything because there is valid solution 

            
