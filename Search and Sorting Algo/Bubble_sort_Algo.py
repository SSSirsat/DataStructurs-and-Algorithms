print("Hello, World!")

def bubble_sort(arr):
    n = len(arr)
    for passes in range(0,n):
        for j in range(0,n-1-passes):
            if (arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr



unsorted_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = bubble_sort(unsorted_list)
print("Sorted list:", sorted_list)

