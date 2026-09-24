class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = list(zip(position, speed))
        """
        sneaky zip shit just pairs them
        if 
        position = [1, 4, 7] speed = [3, 2, 1]
        then it makes 
        (1, 3)
        (4, 2)
        (7, 1)
        """
        stack = []
        for p, s in sorted(pair, reverse=True):
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
            