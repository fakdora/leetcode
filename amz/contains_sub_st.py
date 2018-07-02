def is_sub_st(a,b):
    # brute force
    # b is the short one
    i = 0
    leng = len(a)
    while i < len(a) - (len(b) - 1):
        temp_i = i
        j = 0
        while j < len(b) and temp_i < len(a):
            if a[temp_i] == b[j]:
                temp_i = temp_i + 1
                j = j + 1
            else:
                break

        if j == len(b):
            return True
        i = i + 1
        
    return False

def is_sub_st_kmp(a, b):
    
    

a = "hello"
b = "hel"
s = is_sub_st(a, b)
print s
        
            
    
