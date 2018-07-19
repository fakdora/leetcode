
def max_value_of_sub_seq(nums):
    max_sums = nums[:]
    
    for curr_index in range(1, len(nums)):
        for before_index in range(curr_index):
            if nums[curr_index] > nums[before_index] and max_sums[curr_index] < max_sums[before_index] + nums[curr_index]:
                max_sums[curr_index] = max_sums[before_index] + nums[curr_index]

    return max(max_sums)

def find_sub_seq_that_gives_max_sum(nums):
    max_sums = nums[:]
    sequences = [0] * len(nums)
    for i in range(len(nums)):
        sequences[i] = i

    for curr_index in range(1, len(nums)):
        for before_index in range(curr_index):
            if nums[curr_index] > nums[before_index] and max_sums[curr_index] < max_sums[before_index] + nums[curr_index]:
                max_sums[curr_index] = max_sums[before_index] + nums[curr_index]
                sequences[curr_index] = before_index
    
    max_index = max_sums.index(max(max_sums))
    curr_index = max_index
    next_index = sequences[max_index]
    max_sequence = [nums[curr_index]]

    while next_index != curr_index:
        curr_index = next_index
        next_index = sequences[curr_index]
        max_sequence.append(nums[curr_index])

    return list(reversed(max_sequence))

arr = [10,9,2,5,3,7,101,18]
arr = [1, 101, 2, 3, 100, 4, 5]
arr = [4,6,1,3,8,4,6]

#print max_value_of_sub_seq(arr)
print find_sub_seq_that_gives_max_sum(arr)
