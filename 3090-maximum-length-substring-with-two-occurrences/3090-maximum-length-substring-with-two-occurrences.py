class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        freq = {}
        left = 0
        max_len = 0
        
        for right in range(len(s)):
            # Add current character to frequency map
            char = s[right]
            freq[char] = freq.get(char, 0) + 1
            
            # If any character count exceeds 2, shrink the window from the left
            while freq[char] > 2:
                freq[s[left]] -= 1
                left += 1
                
            # Update the max length found so far
            max_len = max(max_len, right - left + 1)
            
        return max_len