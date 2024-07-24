import winsound
import time

# Function to play sound effect
def play_swap_sound():
    frequency = 1000  # Set frequency to 1000 Hertz
    duration = 100  # Set duration to 100 milliseconds
    winsound.Beep(frequency, duration)
    time.sleep(0.1)  # Add a small delay to ensure the sound plays

# Function to print the array
def print_array(arr, left, right):
    print(f'Current array: {arr[left:right+1]}')

# Merge function to merge two halves
def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    # Create temporary arrays
    L = arr[left:mid + 1]
    R = arr[mid + 1:right + 1]

    # Initial indices of first and second subarrays
    i = 0
    j = 0

    # Initial index of merged subarray
    k = left

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        play_swap_sound()
        print_array(arr, left, right)
        k += 1

    # Copy the remaining elements of L[], if there are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        play_swap_sound()
        print_array(arr, left, right)
        k += 1

    # Copy the remaining elements of R[], if there are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        play_swap_sound()
        print_array(arr, left, right)
        k += 1

# Main function to implement Merge Sort
def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2

        # Sort first and second halves
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)

        merge(arr, left, mid, right)

# Function to execute the Merge Sort and print each step
def sort_and_print_steps(arr):
    print(f'Initial array: {arr}')
    merge_sort(arr, 0, len(arr) - 1)
    print(f'Sorted array: {arr}')

# Example usage
if __name__ == "__main__":
    array = [11, 1, 30, 2, 51, 6, 29, 7, 67, 15, 118, 4, 89, 23]
    sort_and_print_steps(array)
