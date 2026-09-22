class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1                #starts at slowest speed which is UNO banana
        right = max(piles)      #fastest speed which will be biggest pile in the list 

        result = right          #result would be the smallest valid speed discovered


        while left <= right:     #left to right
            speed = (left + right) // 2     #minEatingSpeed

            hours = 0           #total hours for current speed

            for pile in piles:
                hours += math.ceil(pile / speed)

            
            if hours <= h:
                result = speed
                right = speed - 1

            else:
                left =  speed + 1

        return result