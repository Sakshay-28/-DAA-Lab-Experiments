def prim_mst():
    vertices = int(input("Enter number of vertices: "))
    print("Enter adjacency matrix (use 0 where there is no edge):")
    graph = []

    for _ in range(vertices):
        row = list(map(int, input().split()))
        graph.append(row)

    selected = [False] * vertices
    selected[0] = True
    total_cost = 0
    edges = []

    for _ in range(vertices - 1):
        minimum = float("inf")
        start = -1
        end = -1

        for i in range(vertices):
            if selected[i]:
                for j in range(vertices):
                    if not selected[j] and graph[i][j] != 0 and graph[i][j] < minimum:
                        minimum = graph[i][j]
                        start = i
                        end = j

        if end == -1:
            print("The graph is not connected.")
            return

        selected[end] = True
        total_cost += minimum
        edges.append((start, end, minimum))

    print("Minimum Spanning Tree edges:")
    for start, end, weight in edges:
        print(start, "-", end, ":", weight)

    print("Minimum Spanning Tree cost:", total_cost)


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def left_height(root):
    height = 0

    while root:
        height += 1
        root = root.left

    return height


def right_height(root):
    height = 0

    while root:
        height += 1
        root = root.right

    return height


def count_complete_tree_nodes(root):
    if root is None:
        return 0

    left = left_height(root)
    right = right_height(root)

    if left == right:
        return (1 << left) - 1

    return 1 + count_complete_tree_nodes(root.left) + count_complete_tree_nodes(root.right)


def build_complete_tree(values):
    if not values:
        return None

    nodes = [TreeNode(value) for value in values]

    for i in range(len(nodes)):
        left_index = 2 * i + 1
        right_index = 2 * i + 2

        if left_index < len(nodes):
            nodes[i].left = nodes[left_index]

        if right_index < len(nodes):
            nodes[i].right = nodes[right_index]

    return nodes[0]


def longest_palindromic_subsequence(string):
    n = len(string)

    if n == 0:
        return 0

    dp = [[0] * n for _ in range(n)]

    for i in range(n - 1, -1, -1):
        dp[i][i] = 1

        for j in range(i + 1, n):
            if string[i] == string[j]:
                dp[i][j] = 2 + dp[i + 1][j - 1]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    return dp[0][n - 1]


def main():
    while True:
        print("\nEXPERIMENT 9: GRAPHS AND DP")
        print("1. Prim's Minimum Spanning Tree")
        print("2. Count Nodes in Complete Binary Tree")
        print("3. Longest Palindromic Subsequence")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            prim_mst()

        elif choice == "2":
            values = list(map(int, input("Enter complete binary tree node values in level order: ").split()))
            root = build_complete_tree(values)
            print("Total number of nodes:", count_complete_tree_nodes(root))

        elif choice == "3":
            string = input("Enter a string: ")
            print("Length of Longest Palindromic Subsequence:", longest_palindromic_subsequence(string))

        elif choice == "4":
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
