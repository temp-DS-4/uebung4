import matplotlib.pyplot as plt

def mergeSort(arr):
    if len(arr) > 1:
        # Find the middle point and divide the array
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively sort both halves
        mergeSort(left_half)
        mergeSort(right_half)

        # Merge the sorted halves
        i = j = k = 0

        # Copy data to temp arrays left_half[] and right_half[]
        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1



my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
fig,ax = plt.subplot()
ax.plot(range(len(my_list)), my_list)
mergeSort(my_list)
ax.plot(range(len(my_list)), my_list)
plt.show()
