def union_intersection(a, b):
    i = 0
    j = 0
    union = []
    intersection = []

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            if not union or union[-1] != a[i]:
                union.append(a[i])
            i += 1
        elif a[i] > b[j]:
            if not union or union[-1] != b[j]:
                union.append(b[j])
            j += 1
        else:
            if not union or union[-1] != a[i]:
                union.append(a[i])
            if not intersection or intersection[-1] != a[i]:
                intersection.append(a[i])
            i += 1
            j += 1

    while i < len(a):
        if not union or union[-1] != a[i]:
            union.append(a[i])
        i += 1

    while j < len(b):
        if not union or union[-1] != b[j]:
            union.append(b[j])
        j += 1

    return union, intersection


def search_rotated_array(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid

        if arr[low] <= arr[mid]:
            if arr[low] <= target < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if arr[mid] < target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1


def merge(arr, left, mid, right):
    first = []
    second = []

    for i in range(left, mid + 1):
        first.append(arr[i])

    for i in range(mid + 1, right + 1):
        second.append(arr[i])

    i = 0
    j = 0
    k = left

    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            arr[k] = first[i]
            i += 1
        else:
            arr[k] = second[j]
            j += 1
        k += 1

    while i < len(first):
        arr[k] = first[i]
        i += 1
        k += 1

    while j < len(second):
        arr[k] = second[j]
        j += 1
        k += 1


def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)

    return arr


def merge_count_inversions(arr, left, mid, right):
    first = []
    second = []

    for i in range(left, mid + 1):
        first.append(arr[i])

    for i in range(mid + 1, right + 1):
        second.append(arr[i])

    i = 0
    j = 0
    k = left
    inversions = 0

    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            arr[k] = first[i]
            i += 1
        else:
            arr[k] = second[j]
            inversions += len(first) - i
            j += 1
        k += 1

    while i < len(first):
        arr[k] = first[i]
        i += 1
        k += 1

    while j < len(second):
        arr[k] = second[j]
        j += 1
        k += 1

    return inversions


def count_inversions(arr, left, right):
    inversions = 0

    if left < right:
        mid = (left + right) // 2
        inversions += count_inversions(arr, left, mid)
        inversions += count_inversions(arr, mid + 1, right)
        inversions += merge_count_inversions(arr, left, mid, right)

    return inversions


def read_array():
    return list(map(int, input("Enter array elements separated by spaces: ").split()))


def main():
    while True:
        print("\nEXPERIMENT 2: SEARCHING AND DIVIDE-AND-CONQUER")
        print("1. Union and Intersection of Two Sorted Arrays")
        print("2. Search in Rotated Sorted Array")
        print("3. Merge Sort")
        print("4. Count Inversions using Merge Sort")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Enter first sorted array:")
            a = read_array()
            print("Enter second sorted array:")
            b = read_array()
            union, intersection = union_intersection(a, b)
            print("Union:", union)
            print("Intersection:", intersection)

        elif choice == "2":
            arr = read_array()
            target = int(input("Enter target: "))
            print("Index:", search_rotated_array(arr, target))

        elif choice == "3":
            arr = read_array()
            print("Sorted array:", merge_sort(arr, 0, len(arr) - 1))

        elif choice == "4":
            arr = read_array()
            total = count_inversions(arr, 0, len(arr) - 1)
            print("Sorted array:", arr)
            print("Number of inversions:", total)

        elif choice == "5":
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
