from collections import deque


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self, level=0, prefix="Root: "):
        ret = "\t" * level + prefix + str(self.value) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret


def find_max_value(node):
    current = node
    # Йдемо до найправішого вузла
    while current.right is not None:
        current = current.right
    # Повертаємо значення найправішого вузла
    return current.value


def find_min_value(node):
    current = node
    # Йдемо до найлівішого вузла
    while current.left is not None:
        current = current.left
    # Повертаємо значення найлівішого вузла
    return current.value


def sum_of_values(node):
    if node is None:
        return 0
    return node.value + sum_of_values(node.left) + sum_of_values(node.right)


def visualize_tree(node):
    if not node:
        print("Дерево порожнє")
        return

    queue = deque([node])
    while queue:
        level_size = len(queue)
        for i in range(level_size):
            current = queue.popleft()
            print(current.value, end=" ")

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        print()


# Створення дерева
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(8)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)

# Візуалізація дерева
print(f"{root}")

# Виклик функції пошуку максимального значення
print("Найбільше значення в дереві:", find_max_value(root))

# Виклик функції пошуку мінімального значення
print("Найменше значення в дереві:", find_min_value(root))

# Виклик функції знаходження суми всіх значень дерева
print("Сума всіх значень у дереві:", sum_of_values(root))
