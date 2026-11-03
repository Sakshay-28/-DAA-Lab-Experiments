from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert_bst(root, value):
    if root is None:
        return Node(value)

    if value < root.value:
        root.left = insert_bst(root.left, value)
    elif value > root.value:
        root.right = insert_bst(root.right, value)

    return root


def inorder(root):
    if root is None:
        return []

    return inorder(root.left) + [root.value] + inorder(root.right)


def preorder(root):
    if root is None:
        return []

    return [root.value] + preorder(root.left) + preorder(root.right)


def postorder(root):
    if root is None:
        return []

    return postorder(root.left) + postorder(root.right) + [root.value]


def lowest_common_ancestor(root, first, second):
    while root is not None:
        if first < root.value and second < root.value:
            root = root.left
        elif first > root.value and second > root.value:
            root = root.right
        else:
            return root.value

    return None


def build_binary_tree(values):
    if not values or values[0] == "N":
        return None

    root = Node(int(values[0]))
    queue = deque([root])
    index = 1

    while queue and index < len(values):
        current = queue.popleft()

        if index < len(values) and values[index] != "N":
            current.left = Node(int(values[index]))
            queue.append(current.left)

        index += 1

        if index < len(values) and values[index] != "N":
            current.right = Node(int(values[index]))
            queue.append(current.right)

        index += 1

    return root


def largest_bst_info(root):
    if root is None:
        return True, 0, float("inf"), float("-inf")

    left_is_bst, left_size, left_min, left_max = largest_bst_info(root.left)
    right_is_bst, right_size, right_min, right_max = largest_bst_info(root.right)

    if left_is_bst and right_is_bst and left_max < root.value < right_min:
        size = left_size + right_size + 1
        minimum = min(left_min, root.value)
        maximum = max(right_max, root.value)
        return True, size, minimum, maximum

    return False, max(left_size, right_size), float("-inf"), float("inf")


def largest_bst_size(root):
    return largest_bst_info(root)[1]


def main():
    while True:
        print("\nEXPERIMENT 8: BINARY SEARCH TREES")
        print("1. BST Construction")
        print("2. Lowest Common Ancestor in BST")
        print("3. Largest BST in Binary Tree")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            values = [int(value) for value in input("Enter values to insert separated by spaces: ").split()]
            root = None

            for value in values:
                root = insert_bst(root, value)

            print("Inorder traversal:", inorder(root))
            print("Preorder traversal:", preorder(root))
            print("Postorder traversal:", postorder(root))

        elif choice == "2":
            values = [int(value) for value in input("Enter BST values separated by spaces: ").split()]
            root = None

            for value in values:
                root = insert_bst(root, value)

            first = int(input("Enter first node: "))
            second = int(input("Enter second node: "))

            if first not in inorder(root) or second not in inorder(root):
                print("One or both nodes are not present in the BST.")
            else:
                print("Lowest Common Ancestor:", lowest_common_ancestor(root, first, second))

        elif choice == "3":
            values = input("Enter level-order values separated by spaces (use N for null): ").split()
            root = build_binary_tree(values)
            print("Size of largest BST:", largest_bst_size(root))

        elif choice == "4":
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
