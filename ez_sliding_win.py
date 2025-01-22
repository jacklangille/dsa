from typing import List
# You are given an array of integers and a number  k . Find the maximum sum of any contiguous subarray of size  k .



def max_sum_subarray(arr, k):
    max_sum = 0
    window_sum = 0

    # Compute the sum of the first window
    for i in range(k):
        window_sum += arr[i]

    print(f"First window sum: {window_sum}")
    # Slide the window across the array
    for i in range(k, len(arr)):
        # Add the new element and remove the old one
        window_sum += arr[i]
        window_sum -= arr[i-k]
        
        # Update max_sum if the new window_sum is larger
        max_sum = max(max_sum, window_sum)

    return max_sum

nums = [2, 1, 5, 1, 3, 2]
k = 3
max_sum_subarray(nums, k)

def sliding_window_visual(arr, k):
    # Calculate the initial sum of the ASCII values for the first window
    window_sum = sum(ord(c) for c in arr[:k])  # Use ord() to get ASCII values
    max_sum = window_sum

    print(f"Initial window: {''.join(arr[:k])}, Sum = {window_sum}")

    # Iterate through the rest of the array, sliding the window
    for i in range(k, len(arr)):
        incoming = arr[i]
        outgoing = arr[i - k]

        # Update the window sum using ASCII values
        window_sum += ord(incoming) - ord(outgoing)
        max_sum = max(max_sum, window_sum)

        # Print visual representation
        current_window = ''.join(arr[i - k + 1:i + 1])
        print(f"Window slides: {current_window}, Added '{incoming}', Removed '{outgoing}', Sum = {window_sum}")

    print(f"Max Sum = {max_sum}")

# Example usage with ASCII letters
arr = list("abcdefg")  # ASCII letters
print(f"Input: {arr}")
k = 3
sliding_window_visual(arr, k)
