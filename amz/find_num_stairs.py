m = [1,2]

#notice that this is same as fib(n+1)
# fib(n) = fib(n-1) + fib(n-2)

class Solution(object):
    def climbStairs_bf(self, n):
        if n < 0:
            return 0
        if n == 0:
            return 1

        return self.climbStairs_bf(n-1) + self.climbStairs_bf(n-2)


    def climbStairs_recur_memo(self, n, memo):
        if n < 0:
            return 0
        if n == 0:
            return 1
        if memo[n] > 0:
            return memo[n]

        memo[n] =  self.climbStairs_recur_memo(n-1, memo) + self.climbStairs_recur_memo(n-2, memo)
        return  memo[n]

def num_ways_dp(n):
    nums = [0] * (n+1)
    nums[0] = 1
    nums[1] = 1
    
    for i in range(2, n+1):
        nums[i] = nums[i-1] + nums[i-2]
    
    return nums[n]
    

def num_ways_dp_efficient(n):
    nums = [0] * 2
    nums[0] = 1
    nums[1] = 1
    
    for i in range(2, n+1):
        total = nums[0] + nums[1]
        nums[1], nums[0] = total, nums[1]
        
    return nums[1]

# x = {1, 3, 5} possible steps, this can be done in dp way too
def num_ways(n, x):
    if n == 0 or n == 1:
        return 1
    if n < 0:
        return 0
    
    summ = 0 
    for num in x:
        if n-num >= 0:
            summ += num_ways(n-num, x)
        
    return summ

def num_ways_dp(n, x):
    if n == 0 or n == 1:
        return 1
    if n < 0:
        return 0
    nums = [0] * (n+1)
    nums[0] = 1
    summ = 0
    for i in range(1, n+1):
        total = 0
        for j in x:
            if i-j >= 0:
                total += nums[i-j]
        nums[i] = total

    return nums[n]
    

a = Solution()
n = 6
memo = [0] * (n +1)

print a.climbStairs_recur_memo(n, memo)
