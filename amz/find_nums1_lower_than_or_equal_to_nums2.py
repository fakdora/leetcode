def find_nums1_lower_than_or_equal_to_nums2(nums1, nums2):
    i = 0
    j = 0
    total = 0

    nums1 = sorted(nums1)
    nums2 = sorted(nums2)

    while i < len(nums1):
        num1 = nums1[i]
        while j < len(nums2):
            num2 = nums2[j]
            j+=1  # notice it always increments or infinite loop
            if num1 <= num2:
                total += 1
                break
        i+=1
    return total


n1 = [3, 5, 6,6,7,9]
n2 = [1, 3, 5,7,7]
print(find_nums1_lower_than_or_equal_to_nums2(n1, n2))
