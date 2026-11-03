def insertion_sort_iterative(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


def insertion_sort_recursive(arr, n=None):
    if n is None:
        n = len(arr)

    if n <= 1:
        return arr

    insertion_sort_recursive(arr, n - 1)
    key = arr[n - 1]
    j = n - 2

    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = key
    return arr


def dutch_national_flag(arr):
    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        elif arr[mid] == 2:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
        else:
            raise ValueError("Array must contain only 0, 1 and 2.")

    return arr


def majority_element(arr):
    candidate = None
    count = 0

    for value in arr:
        if count == 0:
            candidate = value
            count = 1
        elif value == candidate:
            count += 1
        else:
            count -= 1

    count = 0

    for value in arr:
        if value == candidate:
            count += 1

    if count > len(arr) // 2:
        return candidate

    return None


def read_array():
    return list(map(int, input("Enter array elements separated by spaces: ").split()))


def main():
    while True:
        print("\nEXPERIMENT 1: BASIC SORTING AND ARRAY PROBLEMS")
        print("1. Insertion Sort (Iterative)")
        print("2. Insertion Sort (Recursive)")
        print("3. Dutch National Flag Problem")
        print("4. Majority Element")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            arr = read_array()
            print("Sorted array:", insertion_sort_iterative(arr))

        elif choice == "2":
            arr = read_array()
            print("Sorted array:", insertion_sort_recursive(arr))

        elif choice == "3":
            arr = read_array()

            try:
                print("Sorted array:", dutch_national_flag(arr))
            except ValueError as error:
                print(error)

        elif choice == "4":
            arr = read_array()
            result = majority_element(arr)

            if result is None:
                print("No majority element exists.")
            else:
                print("Majority element:", result)

        elif choice == "5":
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
