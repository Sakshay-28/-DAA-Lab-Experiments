def maximum_product_subarray(arr):
    if len(arr) == 0:
        return None

    max_ending = arr[0]
    min_ending = arr[0]
    result = arr[0]

    for i in range(1, len(arr)):
        value = arr[i]

        if value < 0:
            max_ending, min_ending = min_ending, max_ending

        max_ending = max(value, max_ending * value)
        min_ending = min(value, min_ending * value)

        if max_ending > result:
            result = max_ending

    return result


def partition(arr, low, high):
    pivot = arr[high]
    i = low

    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[high] = arr[high], arr[i]
    return i


def quickselect_kth_largest(arr, k):
    n = len(arr)

    if k < 1 or k > n:
        return None

    target = n - k
    low = 0
    high = n - 1

    while low <= high:
        pivot_index = partition(arr, low, high)

        if pivot_index == target:
            return arr[pivot_index]
        elif pivot_index < target:
            low = pivot_index + 1
        else:
            high = pivot_index - 1

    return None


def fibonacci_dp(n):
    if n < 0:
        return None
    if n == 0:
        return 0
    if n == 1:
        return 1

    previous = 0
    current = 1

    for i in range(2, n + 1):
        next_value = previous + current
        previous = current
        current = next_value

    return current


def smallest_missing_positive(arr):
    n = len(arr)

    for i in range(n):
        while 1 <= arr[i] <= n and arr[arr[i] - 1] != arr[i]:
            correct_index = arr[i] - 1
            arr[i], arr[correct_index] = arr[correct_index], arr[i]

    for i in range(n):
        if arr[i] != i + 1:
            return i + 1

    return n + 1


def read_array():
    values = input("Enter array elements separated by spaces: ").split()
    arr = []

    for value in values:
        arr.append(int(value))

    return arr


def main():
    while True:
        print("\nEXPERIMENT 4: SELECTION AND DYNAMIC PROGRAMMING")
        print("1. Maximum Product Subarray")
        print("2. Kth Largest using Quick Select")
        print("3. Nth Fibonacci Number")
        print("4. Smallest Missing Positive Integer")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            arr = read_array()
            result = maximum_product_subarray(arr)

            if result is None:
                print("Array is empty.")
            else:
                print("Maximum product:", result)

        elif choice == "2":
            arr = read_array()
            k = int(input("Enter k: "))
            result = quickselect_kth_largest(arr, k)

            if result is None:
                print("Invalid value of k.")
            else:
                print("Kth largest element:", result)

        elif choice == "3":
            n = int(input("Enter n: "))
            result = fibonacci_dp(n)

            if result is None:
                print("Enter a non-negative integer.")
            else:
                print("Nth Fibonacci number:", result)

        elif choice == "4":
            arr = read_array()
            result = smallest_missing_positive(arr)
            print("Smallest missing positive integer:", result)

        elif choice == "5":
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
