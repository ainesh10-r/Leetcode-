from collections import Counter
from typing import List

class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        # Count remainders modulo 3
        count = Counter(stone % 3 for stone in stones)
        
        # If remainder 0 count is even
        if count[0] % 2 == 0:
            return count[1] > 0 and count[2] > 0
            
        # If remainder 0 count is odd
        return abs(count[1] - count[2]) > 2