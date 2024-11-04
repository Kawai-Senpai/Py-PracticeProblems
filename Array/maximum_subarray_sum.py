# Question: Find the maximum sum of a contiguous subarray.

def max_subarray_sum(arr):

    if(len(arr) < 1):
        return 0
    
    max_sum = current_sum = arr[0]
    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

# Sample inputs
samples = [
    [-2, 1, -3, 4, -1, 2, 1, -5, 4],
    [1],
    [5, 4, -1, 7, 8],
    [-1, -2, -3, -4],
    [2, 1, -5, 4, -3, 4, 2]
]

# Print outputs for each sample
for i, sample in enumerate(samples, 1):
    result = max_subarray_sum(sample)
    print(f"Example {i}: Input: {sample} => Output: {result}")