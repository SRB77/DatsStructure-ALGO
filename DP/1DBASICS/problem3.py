# https://leetcode.com/problems/climbing-stairs/description/

# tribonnaci number problem in the leetcode 

# Tabulation 

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1 :
            return 1
        prev =  1
        prevtwo =  1
        for i in range(2,n+1):
            current_i = prev+prevtwo
            prevtwo = prev
            prev = current_i
        return prev

# Memoization
    
