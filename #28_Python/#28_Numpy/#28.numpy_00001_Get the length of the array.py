def bubble_sort(arr):
    # Get the length of the array
    n = len(arr)
    # Loop through the array
    for i in range(n):
        # Loop through the array from the beginning to the end
        for j in range(0, n-i-1):
            # If the current element is greater than the next element
            if arr[j] > arr[j+1]:
                # Swap the elements
                arr[j], arr[j+1] = arr[j+1], arr[j]