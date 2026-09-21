class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        wiseTortoise, arrogantHare = 0, 0

        while True:
            wiseTortoise = nums[wiseTortoise]
            arrogantHare = nums[nums[arrogantHare]]

            if wiseTortoise == arrogantHare:
                break
        
        slowTard = 0

        while True:
            wiseTortoise = nums[wiseTortoise]
            slowTard = nums[slowTard]
            if wiseTortoise == slowTard:
                return wiseTortoise
