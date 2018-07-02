# find the largest sub array sum
# kadane's algorithm is O(n)
# it caclulates current_max and global_max
# current_max is what's contiguous, sub_array of the current_index

def kadanes(arr):
    current_max = global_max = arr[0]

    for i in range(1, len(arr)):
        curr_elem = arr[i]
        curr_max = max(curr_elem, curr_elem + curr_max)
        global_max = max(curr_max, global_max)

    return global_max



