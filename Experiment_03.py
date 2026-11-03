def matrix_multiplication(a, b):
    rows_a = len(a)
    cols_a = len(a[0])
    rows_b = len(b)
    cols_b = len(b[0])

    if cols_a != rows_b:
        raise ValueError("Matrix dimensions are not compatible.")

    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += a[i][k] * b[k][j]

    return result


def add_matrices(a, b):
    n = len(a)
    result = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            result[i][j] = a[i][j] + b[i][j]

    return result


def subtract_matrices(a, b):
    n = len(a)
    result = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            result[i][j] = a[i][j] - b[i][j]

    return result


def strassen(a, b):
    n = len(a)

    if n == 1:
        return [[a[0][0] * b[0][0]]]

    mid = n // 2

    a11 = [row[:mid] for row in a[:mid]]
    a12 = [row[mid:] for row in a[:mid]]
    a21 = [row[:mid] for row in a[mid:]]
    a22 = [row[mid:] for row in a[mid:]]

    b11 = [row[:mid] for row in b[:mid]]
    b12 = [row[mid:] for row in b[:mid]]
    b21 = [row[:mid] for row in b[mid:]]
    b22 = [row[mid:] for row in b[mid:]]

    m1 = strassen(add_matrices(a11, a22), add_matrices(b11, b22))
    m2 = strassen(add_matrices(a21, a22), b11)
    m3 = strassen(a11, subtract_matrices(b12, b22))
    m4 = strassen(a22, subtract_matrices(b21, b11))
    m5 = strassen(add_matrices(a11, a12), b22)
    m6 = strassen(subtract_matrices(a21, a11), add_matrices(b11, b12))
    m7 = strassen(subtract_matrices(a12, a22), add_matrices(b21, b22))

    c11 = add_matrices(subtract_matrices(add_matrices(m1, m4), m5), m7)
    c12 = add_matrices(m3, m5)
    c21 = add_matrices(m2, m4)
    c22 = add_matrices(subtract_matrices(add_matrices(m1, m3), m2), m6)

    result = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(mid):
        for j in range(mid):
            result[i][j] = c11[i][j]
            result[i][j + mid] = c12[i][j]
            result[i + mid][j] = c21[i][j]
            result[i + mid][j + mid] = c22[i][j]

    return result


def strassen_multiplication(a, b):
    if len(a[0]) != len(b):
        raise ValueError("Matrix dimensions are not compatible.")

    rows_a = len(a)
    cols_a = len(a[0])
    cols_b = len(b[0])
    size = 1
    largest = max(rows_a, cols_a, len(b), cols_b)

    while size < largest:
        size *= 2

    padded_a = [[0 for _ in range(size)] for _ in range(size)]
    padded_b = [[0 for _ in range(size)] for _ in range(size)]

    for i in range(rows_a):
        for j in range(cols_a):
            padded_a[i][j] = a[i][j]

    for i in range(len(b)):
        for j in range(cols_b):
            padded_b[i][j] = b[i][j]

    product = strassen(padded_a, padded_b)
    return [row[:cols_b] for row in product[:rows_a]]


def allocate_minimum_pages(pages, students):
    n = len(pages)

    if students > n or students <= 0:
        return -1

    low = max(pages)
    high = sum(pages)
    answer = high

    while low <= high:
        mid = (low + high) // 2
        required_students = 1
        current_pages = 0

        for page_count in pages:
            if current_pages + page_count > mid:
                required_students += 1
                current_pages = page_count
            else:
                current_pages += page_count

        if required_students <= students:
            answer = mid
            high = mid - 1
        else:
            low = mid + 1

    return answer


def median_of_two_sorted_arrays(a, b):
    if len(a) > len(b):
        return median_of_two_sorted_arrays(b, a)

    m = len(a)
    n = len(b)
    low = 0
    high = m

    while low <= high:
        partition_a = (low + high) // 2
        partition_b = (m + n + 1) // 2 - partition_a

        max_left_a = float("-inf") if partition_a == 0 else a[partition_a - 1]
        min_right_a = float("inf") if partition_a == m else a[partition_a]

        max_left_b = float("-inf") if partition_b == 0 else b[partition_b - 1]
        min_right_b = float("inf") if partition_b == n else b[partition_b]

        if max_left_a <= min_right_b and max_left_b <= min_right_a:
            if (m + n) % 2 == 0:
                return (max(max_left_a, max_left_b) + min(min_right_a, min_right_b)) / 2

            return max(max_left_a, max_left_b)

        if max_left_a > min_right_b:
            high = partition_a - 1
        else:
            low = partition_a + 1

    raise ValueError("Input arrays must be sorted.")


def read_matrix(rows, cols, name):
    matrix = []
    print("Enter", name, "row by row:")

    for _ in range(rows):
        row = list(map(int, input().split()))

        if len(row) != cols:
            raise ValueError("Incorrect number of columns.")

        matrix.append(row)

    return matrix


def main():
    while True:
        print("\nEXPERIMENT 3: MATRIX AND BINARY SEARCH")
        print("1. Conventional Matrix Multiplication")
        print("2. Strassen's Matrix Multiplication")
        print("3. Allocate Minimum Pages")
        print("4. Median of Two Sorted Arrays")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice in ("1", "2"):
            rows_a = int(input("Enter rows in first matrix: "))
            cols_a = int(input("Enter columns in first matrix: "))
            a = read_matrix(rows_a, cols_a, "first matrix")

            rows_b = int(input("Enter rows in second matrix: "))
            cols_b = int(input("Enter columns in second matrix: "))
            b = read_matrix(rows_b, cols_b, "second matrix")

            try:
                if choice == "1":
                    result = matrix_multiplication(a, b)
                else:
                    result = strassen_multiplication(a, b)

                print("Result:")
                for row in result:
                    print(row)

            except ValueError as error:
                print(error)

        elif choice == "3":
            pages = list(map(int, input("Enter pages in each book: ").split()))
            students = int(input("Enter number of students: "))
            print("Minimum maximum pages:", allocate_minimum_pages(pages, students))

        elif choice == "4":
            print("Enter first sorted array:")
            a = list(map(int, input().split()))
            print("Enter second sorted array:")
            b = list(map(int, input().split()))

            try:
                print("Median:", median_of_two_sorted_arrays(a, b))
            except ValueError as error:
                print(error)

        elif choice == "5":
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
