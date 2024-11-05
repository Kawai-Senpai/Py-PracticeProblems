# Find out 2 elements (Indexes) in the array whose sum is equal to the given number

def find_elements_for_sum(arr, sum):
    complements = {}
    for i in range(len(arr)):
        if arr[i] in complements:
            return i, complements[arr[i]]
        else:
            complement = sum - arr[i]
            complements[complement] = i
    return None, None

# Testing 
# Input: [1, 2, 3, 4, 5, 6, 7, 8, 9], 10
idx1, idx2 = find_elements_for_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 10)
print(idx1, idx2)