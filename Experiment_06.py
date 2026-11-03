import heapq


def counting_sort(arr):
    if not arr:
        return []

    if min(arr) < 0:
        raise ValueError("Counting Sort accepts non-negative integers only.")

    counts = [0] * (max(arr) + 1)

    for num in arr:
        counts[num] += 1

    result = []

    for num in range(len(counts)):
        result.extend([num] * counts[num])

    return result


def bucket_sort(arr):
    if len(arr) <= 1:
        return arr[:]

    minimum = min(arr)
    maximum = max(arr)

    if minimum == maximum:
        return arr[:]

    bucket_count = len(arr)
    buckets = [[] for _ in range(bucket_count)]

    for num in arr:
        index = int((num - minimum) / (maximum - minimum) * (bucket_count - 1))
        buckets[index].append(num)

    result = []

    for bucket in buckets:
        bucket.sort()
        result.extend(bucket)

    return result


def at_most_k_distinct(arr, k):
    if k < 0:
        return 0

    frequency = {}
    left = 0
    count = 0

    for right in range(len(arr)):
        frequency[arr[right]] = frequency.get(arr[right], 0) + 1

        while len(frequency) > k:
            frequency[arr[left]] -= 1

            if frequency[arr[left]] == 0:
                del frequency[arr[left]]

            left += 1

        count += right - left + 1

    return count


def subarrays_with_exactly_k_distinct(arr, k):
    if k <= 0:
        return 0

    return at_most_k_distinct(arr, k) - at_most_k_distinct(arr, k - 1)


def minimize_array_sum(arr, k):
    heap = [-num for num in arr]
    heapq.heapify(heap)

    for _ in range(k):
        if not heap:
            break

        largest = -heapq.heappop(heap)
        reduced = (largest + 1) // 2
        heapq.heappush(heap, -reduced)

    return -sum(heap)


def read_integer_array():
    return [int(value) for value in input("Enter array elements separated by spaces: ").split()]


def read_float_array():
    return [float(value) for value in input("Enter array elements separated by spaces: ").split()]


def main():
    while True:
        print("\nEXPERIMENT 6: LINEAR-TIME SORTING")
        print("1. Counting Sort")
        print("2. Bucket Sort")
        print("3. Subarrays with Exactly K Distinct")
        print("4. Minimize Array Sum after K Operations")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            arr = read_integer_array()
            print("Sorted array:", counting_sort(arr))

        elif choice == "2":
            arr = read_float_array()
            print("Sorted array:", bucket_sort(arr))

        elif choice == "3":
            arr = read_integer_array()
            k = int(input("Enter k: "))
            print("Number of subarrays:", subarrays_with_exactly_k_distinct(arr, k))

        elif choice == "4":
            arr = read_integer_array()
            k = int(input("Enter number of operations: "))
            print("Minimum array sum:", minimize_array_sum(arr, k))

        elif choice == "5":
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
