class Solution(object):  
    def num_ways_to_give_change_recursion(self, amount, coins):
        if amount == 0:
            return 1
        if amount < 0:
            return 0
        ways = 0
        for coin in coins:
            ways += self.change(amount-coin, coins)
            coins = coins[1:]
            
        return ways
    
    def change_recursion_with_index(self, amount, coins, coin_index):
        if amount == 0:
            return 1
        if amount < 0:
            return 0
        ways = 0
        for i in range(coin_index, len(coins)):
            ways += self.change(amount-coins[i], coins, i)
            
        return ways
        
    def change_dp(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
    
        ways = [0] * (amount + 1)
        ways[0] = 1
        
        for coin in coins:
            for value, way in enumerate(ways):
                if value >= coin:
                    ways[value] = ways[value] + ways[value-coin]
                    
        return ways[amount]
