import heapq


def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

    return arr


def rearrange_string(s):
    frequencies = {}

    for char in s:
        frequencies[char] = frequencies.get(char, 0) + 1

    heap = [(-count, char) for char, count in frequencies.items()]
    heapq.heapify(heap)

    result = []
    previous_count = 0
    previous_char = ""

    while heap:
        count, char = heapq.heappop(heap)
        result.append(char)
        count += 1

        if previous_count < 0:
            heapq.heappush(heap, (previous_count, previous_char))

        previous_count = count
        previous_char = char

    if len(result) != len(s):
        return None

    return "".join(result)


def merge_k_sorted_arrays(arrays):
    heap = []

    for array_index in range(len(arrays)):
        if arrays[array_index]:
            heapq.heappush(heap, (arrays[array_index][0], array_index, 0))

    result = []

    while heap:
        value, array_index, element_index = heapq.heappop(heap)
        result.append(value)

        next_index = element_index + 1

        if next_index < len(arrays[array_index]):
            next_value = arrays[array_index][next_index]
            heapq.heappush(heap, (next_value, array_index, next_index))

    return result


def median_of_medians(arr):
    if len(arr) <= 5:
        sorted_arr = sorted(arr)
        return sorted_arr[len(sorted_arr) // 2]

    medians = []

    for i in range(0, len(arr), 5):
        group = sorted(arr[i:i + 5])
        medians.append(group[len(group) // 2])

    return median_of_medians(medians)


def partition_three_way(arr, low, high, pivot):
    i = low
    j = low
    k = high

    while j <= k:
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j += 1
        elif arr[j] > pivot:
            arr[j], arr[k] = arr[k], arr[j]
            k -= 1
        else:
            j += 1

    return i, k


def select_kth(arr, low, high, k):
    while low <= high:
        current = arr[low:high + 1]
        pivot = median_of_medians(current)
        left, right = partition_three_way(arr, low, high, pivot)

        if k < left:
            high = left - 1
        elif k > right:
            low = right + 1
        else:
            return arr[k]

    return None


def kth_smallest_median_of_medians(arr, k):
    if k < 1 or k > len(arr):
        return None

    values = arr[:]
    return select_kth(values, 0, len(values) - 1, k - 1)


def read_array():
    return [int(value) for value in input("Enter array elements separated by spaces: ").split()]


def main():
    while True:
        print("\nEXPERIMENT 5: HEAP APPLICATIONS")
        print("1. Heap Sort")
        print("2. Rearrange String")
        print("3. Merge K Sorted Arrays")
        print("4. Median-of-Medians")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            arr = read_array()
            print("Sorted array:", heap_sort(arr))

        elif choice == "2":
            s = input("Enter a string: ")
            result = rearrange_string(s)

            if result is None:
                print("Rearrangement is not possible.")
            else:
                print("Rearranged string:", result)

        elif choice == "3":
            k = int(input("Enter number of sorted arrays: "))
            arrays = []

            for i in range(k):
                print("Array", i + 1)
                arrays.append(read_array())

            print("Merged array:", merge_k_sorted_arrays(arrays))

        elif choice == "4":
            arr = read_array()
            k = int(input("Enter k (1-based position): "))
            result = kth_smallest_median_of_medians(arr, k)

            if result is None:
                print("Invalid value of k.")
            else:
                print("Kth smallest element:", result)

        elif choice == "5":
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
