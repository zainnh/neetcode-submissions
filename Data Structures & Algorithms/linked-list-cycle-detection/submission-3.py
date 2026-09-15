# did it with the hash map tard solution last time but reels explained the fast / slow 2 pointer approach and i guess it is more space optimal. 

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

        