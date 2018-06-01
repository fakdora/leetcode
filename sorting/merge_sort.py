# merge sort with space O(n)

def merge_sort(x):
    if len(x) < 2:
        return x
    
    mid = int(len(x) / 2)
    
    y = merge_sort(x[mid:])
    z = merge_sort(x[:mid])
    
    i, j = 0, 0
    result = []
    
    while i < len(y) and j < len(z):
        if y[i] < z[j]:
            result.append(y[i])
            i += 1
        else:
            result.append(z[j])
            j += 1

    if i < len(y):
        result += y[i:]
        
    if j < len(z):
        result += z[j:]
        
    
    return result

print (merge_sort([12, 11, 13, 5, 6, 7]))
