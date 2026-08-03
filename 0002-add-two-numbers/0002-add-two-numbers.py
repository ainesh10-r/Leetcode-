# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Step 1: Traverse l1 to build its number string
        s1 = ""
        current = l1
        while current:
            s1 += str(current.val)
            current = current.next
            
        # Step 2: Traverse l2 to build its number string
        s2 = ""
        current = l2
        while current:
            s2 += str(current.val)
            current = current.next
            
        # Note: LeetCode's linked lists store digits in reverse order (e.g., 342 is represented as 2 -> 4 -> 3).
        # So we reverse the string to get the actual number value.
        num1 = int(s1[::-1])
        num2 = int(s2[::-1])
        
        # Step 3: Add them together
        total = num1 + num2
        
        # Step 4: Convert total back to a reversed string to build the result linked list
        total_str = str(total)[::-1]
        
        # Create a dummy head for our output linked list
        dummy_head = ListNode(0)
        current = dummy_head
        
        for char in total_str:
            current.next = ListNode(int(char))
            current = current.next
            
        return dummy_head.next#