# Python program for implementation of MergeSort

# Merges two subarrays of arr[].
# First subarray is arr[low..mid]
# Second subarray is arr[mid+1..high]
def merge(arr, low, mid, high):

    left_arr = arr[low:mid+1]
    right_arr = arr[mid+1:high+1]
    first_half_length = len(left_arr)
    second_half_length = len(right_arr)

    # Merge the temp arrays back into arr[low..high]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    current = low     # Initial index of merged subarray

    while i < (mid-low+1) and j < (high-mid) :
        if left_arr[i] <= right_arr[j]:
            arr[current] = left_arr[i]
            i += 1
        else:
            arr[current] = right_arr[j]
            j += 1
        current += 1


    # Copy the remaining elements of left_arr[], if there are any
    while i < first_half_length:
        arr[current] = left_arr[i]
        i += 1
        current += 1
    # # this is not necessary cuz right half is shorter 
    # while j < second_half_length:
    #     arr[current] = right_arr[j]
    #     j += 1
    #     current += 1

# low is for left index and high is right index of the
# sub-array of arr to be sorted
def mergeSort(arr, low, high):
    if low < high:
        mid = (low + (high)) / 2
        # Sort first and second halves
        mergeSort(arr, low, mid)
        mergeSort(arr, mid+1, high)
        merge(arr, low, mid, high)

# merge([5,2,6], 1, 1, 2)

# Driver code to test above
arr = [12, 11, 13, 5, 6, 7, 1]
n = len(arr)

for i in range(n):
    print ("%d" %arr[i]),
print

mergeSort(arr,0,n-1)
for i in range(n):
    print ("%d" %arr[i]),


