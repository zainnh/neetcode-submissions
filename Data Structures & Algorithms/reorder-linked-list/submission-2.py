# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
need to re order in alternating reverse val order, 0, n-1, 1, n-2

we can do this with a doubly linked list and two pointers, we can have one fast pointer adn one slow to find the middle of the list, because then once we have the middle we can just reverse the rest of the list since after the mid point that is all the values we will reverse.


first -> find the mid point of the list

    then take the second half of the list and reverse it 

    then take both lists, node from first, then node from second, then repeat.



"""
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
           
        second = slow.next 
        slow.next = None
        previous = None

        while second:
            temp = second.next
            second.next = previous
            previous = second
            second = temp
    
        first, second = head, previous
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
        




        
        