def candy(ratings):
    length = len(ratings)
    candies = [1] * length
    
    # compare current one to the left one
    for i in range(1, length):
        if ratings[i] > ratings[i-1]:
            candies[i] = candies[i-1] + 1
    
    # compare current one to the right one
    for i in reversed(range(length-1)):
        if ratings[i] > ratings[i+1]:
            candies[i] = max(candies[i], candies[i+1] + 1)
            
    return sum(candies)
            
