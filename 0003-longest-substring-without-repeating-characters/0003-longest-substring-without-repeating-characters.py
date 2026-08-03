class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen={}#stored index location
        left=0
        max_len=0

        for right in range(len(s)):#slowerly moves to the next character
            char=s[right]#current position
            if char in seen and seen[char]>=left:#checks if duplicate is there 
                 left=seen[char]+1#skips the dublicate 
            seen[char]=right#informs the index about the current postion we are in
            current_len=right-left+1#measures the len from the current postion to the starting position
            max_len=max(max_len,current_len)#finds the maximum len among them through compare 
        return max_len