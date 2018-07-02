# aabbdcdeabacd

# pre:
# k discinct chars
# st string

# vars
# hash map of chars with counters
# start - starting
# y - current index
# curr_subst

# spcial cases:
# empty, type, None, 
# allowed chars - lower, upper, punctuation, 
# ascii code - 256


def kuni(st, k):
    chs = {}
    longest_st = ""
    start = 0
    unique_counter = 0
    
    for i, ch in enumerate(st):
        # find out if the character is unique
        # then add it to the unique counter
        # else just put it in to the hash map
        
        if ch not in chs.keys():
            chs[ch] = 0
            unique_counter += 1
        elif chs[ch] == 0:
            unique_counter += 1
        chs[ch] += 1

        if not unique_counter > k:
            if len(longest_st) < i-start+1:
                longest_st = st[start:i+1]

        while unique_counter > k:
            chs[st[start]] -= 1
            if chs[st[start]] == 0:
                unique_counter -= 1
                    
            start += 1
        
    return longest_st
            
s = "aabacbebebe"
k = 3
u = kuni(s, k)
print (u)
        
            
        
    
    
    
    
    
