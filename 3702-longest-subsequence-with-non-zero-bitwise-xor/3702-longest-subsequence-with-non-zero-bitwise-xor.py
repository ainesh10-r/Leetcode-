from typing import List

class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        total_xor = 0
        for num in nums:
            total_xor ^= num
            
        # If the total XOR is not zero, the entire array is our answer
        if total_xor != 0:
            return len(nums)
            
        # If total XOR is zero, check if we can exclude one element to make it non-zero
        # As long as the array contains at least one non-zero element, dropping one element works.
        for num in nums:
            if num != 0:
                return len(nums) - 1
                
        # If all elements are 0, no non-zero subsequence is possible
        return 0