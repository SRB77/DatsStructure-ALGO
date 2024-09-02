# House robber : https://leetcode.com/problems/house-robber/description/

class Solution:
    def rob(self, nums):
        n = len(nums)
        dp = [-1] * (n)
        def find(ind,dp):
            if ind >=n:
                return 0 
            if dp[ind] != -1:
                return dp[ind]
            take = nums[ind]+find(ind+2,dp)
            nottake = 0+find(ind+1,dp)
            dp[ind] = max(take,nottake)
            return max(take ,nottake)
        return find(0,dp)


