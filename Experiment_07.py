from collections import Counter


class ChainingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash_function(key)

        if key not in self.table[index]:
            self.table[index].append(key)

    def search(self, key):
        index = self.hash_function(key)
        return key in self.table[index]

    def display(self):
        for index in range(self.size):
            print(index, ":", self.table[index])


class LinearProbingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash_function(key)

        for i in range(self.size):
            position = (index + i) % self.size

            if self.table[position] == key:
                return True

            if self.table[position] is None:
                self.table[position] = key
                return True

        return False

    def search(self, key):
        index = self.hash_function(key)

        for i in range(self.size):
            position = (index + i) % self.size

            if self.table[position] is None:
                return False

            if self.table[position] == key:
                return True

        return False

    def display(self):
        for index in range(self.size):
            print(index, ":", self.table[index])


def relative_sort(arr, order):
    frequency = Counter(arr)
    result = []

    for num in order:
        result.extend([num] * frequency[num])
        frequency.pop(num, None)

    remaining = []

    for num, count in frequency.items():
        remaining.extend([num] * count)

    remaining.sort()
    result.extend(remaining)

    return result


def minimum_window_substring(s, pattern):
    if not s or not pattern:
        return ""

    required = Counter(pattern)
    window = {}
    formed = 0
    required_count = len(required)
    left = 0
    min_length = float("inf")
    start_index = 0

    for right, char in enumerate(s):
        window[char] = window.get(char, 0) + 1

        if char in required and window[char] == required[char]:
            formed += 1

        while formed == required_count:
            current_length = right - left + 1

            if current_length < min_length:
                min_length = current_length
                start_index = left

            left_char = s[left]
            window[left_char] -= 1

            if left_char in required and window[left_char] < required[left_char]:
                formed -= 1

            left += 1

    if min_length == float("inf"):
        return ""

    return s[start_index:start_index + min_length]


def read_integer_array():
    return [int(value) for value in input("Enter array elements separated by spaces: ").split()]


def main():
    while True:
        print("\nEXPERIMENT 7: HASHING AND STRINGS")
        print("1. Hash Table using Separate Chaining")
        print("2. Hash Table using Linear Probing")
        print("3. Relative Sorting")
        print("4. Minimum Window Substring")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            size = int(input("Enter hash table size: "))
            table = ChainingHashTable(size)

            while True:
                print("\n1. Insert")
                print("2. Search")
                print("3. Display")
                print("4. Back")
                operation = input("Enter your choice: ")

                if operation == "1":
                    key = int(input("Enter key: "))
                    table.insert(key)
                elif operation == "2":
                    key = int(input("Enter key to search: "))
                    print("Found" if table.search(key) else "Not found")
                elif operation == "3":
                    table.display()
                elif operation == "4":
                    break
                else:
                    print("Invalid choice.")

        elif choice == "2":
            size = int(input("Enter hash table size: "))
            table = LinearProbingHashTable(size)

            while True:
                print("\n1. Insert")
                print("2. Search")
                print("3. Display")
                print("4. Back")
                operation = input("Enter your choice: ")

                if operation == "1":
                    key = int(input("Enter key: "))

                    if not table.insert(key):
                        print("Hash table is full.")
                elif operation == "2":
                    key = int(input("Enter key to search: "))
                    print("Found" if table.search(key) else "Not found")
                elif operation == "3":
                    table.display()
                elif operation == "4":
                    break
                else:
                    print("Invalid choice.")

        elif choice == "3":
            arr = read_integer_array()
            order = read_integer_array()
            print("Relative sorted array:", relative_sort(arr, order))

        elif choice == "4":
            s = input("Enter the main string: ")
            pattern = input("Enter the pattern: ")
            result = minimum_window_substring(s, pattern)
            print("Minimum window substring:", result if result else "No valid window found.")

        elif choice == "5":
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
