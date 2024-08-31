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
    
class Solution:
    def tribonacci(self, n: int , dp = None) -> int:
        if dp is None:
            dp = [-1]*(n+1)
        if n ==0 :
            return 0
        if n ==1:
            return 1
        if n ==2 :
            return 1
        if dp[n] != -1:
            return dp [n]
        dp[n] = self.tribonacci(n-1,dp)+self.tribonacci(n-2,dp)+self.tribonacci(n-3,dp)
        return dp[n]  

# Space Optimization 
class Solution:
    def tribonacci(self, n: int ) -> int:
        if n ==0 :
            return 0
        if n ==1:
            return 1
        if n ==2 :
            return 1 
        p1 = 1
        p2 = 1
        p3 = 0    
        for i in range (3,n+1):
            cur_i = p1+p2+p3
            p3 = p2
            p2 = p1
            p1 = cur_i
        return p1
