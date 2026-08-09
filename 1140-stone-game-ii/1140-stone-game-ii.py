class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        # Create a suffix sum array to quickly get the sum of remaining piles
        suffix_sums = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sums[i] = suffix_sums[i + 1] + piles[i]
            
        memo = {}
        
        def dfs(i, m):
            # If we've reached or passed the end, no stones left
            if i >= n:
                return 0
            # If remaining piles can all be taken within current 2M limit
            if i + 2 * m >= n:
                return suffix_sums[i]
            # Check memoization table
            if (i, m) in memo:
                return memo[(i, m)]
                
            max_stones = 0
            # Try all possible choices for X (1 to 2M)
            for x in range(1, 2 * m + 1):
                # Current player's stones = total remaining minus what the opponent gets next
                opponent_score = dfs(i + x, max(m, x))
                current_score = suffix_sums[i] - opponent_score
                max_stones = max(max_stones, current_score)
                
            memo[(i, m)] = max_stones
            return max_stones
            
        return dfs(0, 1)