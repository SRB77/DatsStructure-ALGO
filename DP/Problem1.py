# # introduction to DYNAMIC PROGRAMMING 

# # PROBLEM 1 : PRINT THE Fibonacci number of the given index . usign three techniques of DP . (MEMOIZATION ,TABLUATION, SPACE OTIMIZATION).



# # 1.Memoization (option1)
# def fibo(n,dp=None):
#     if dp is None:
#         dp = [-1]*(n+1)
#     if n ==1:
#         return 1
#     if n == 0:
#         return 0
#     if dp[n] != -1:
#         return dp[n]
#     dp[n]=fibo(n-1,dp)+fibo(n-2,dp)
#     return dp[n]
# print(fibo(8));

# # MEMOIZATION (option2)
# def fibo2(n):
#     dp = [-1]*(n+1)
#     def find(ind,dp):
#         if n ==0:return 0
#         if n ==1:return 1
#         if dp[ind] != -1:
#             return dp[ind]
#         dp[ind] =  find(ind-1,dp)+find(ind-2,dp)
#         return  find(ind-1,dp)+find(ind-2,dp)
#     return find(n,dp)
# print(fibo(8))





#TABULATION 
def Fibonacci(n):
    dp = [-1]*(n+1)
    dp[0]=0
    dp[1]=1
    for i in range(2,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]
print(Fibonacci(4))