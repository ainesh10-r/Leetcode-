class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        # Put all elements into a set for O(1) lookups
        num_set = set(nums)
        
        # Step 1: Calculate the longest sequential prefix sum
        current_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                current_sum += nums[i]
            else:
                break
                
        # Step 2: Find the smallest integer >= current_sum that is missing from the set
        while current_sum in num_set:
            current_sum += 1
            
        return current_sum