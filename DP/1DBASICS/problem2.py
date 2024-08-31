#  Climbing stairs problem of (LEETCODE).  link ("https://leetcode.com/problems/climbing-stairs/submissions/1374129508/")


# MEMORIZATION: 
class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[-1]*(n+1)
        def helper(ind,dp):
            if ind ==0 or ind == 1:
                return 1
            if dp[ind]!=-1:
                return dp[ind]
            dp[ind] = helper (ind-1 , dp)+ helper (ind-2 , dp)
            return dp[ind]
        return helper(n,dp)
# TABULATION:
class Solution:
    def climbStairs(self, n: int,dp=None) -> int:
        if n==0 or n == 1:
            return 1
        dp = [-1]*(n+1)
        dp[0]=1
        dp[1]=1
        for i in range (2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]


# SPACEOPTIMIZATON :
    
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

        