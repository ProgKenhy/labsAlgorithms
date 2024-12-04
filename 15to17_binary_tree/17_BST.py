from tree_parser import TreeNode, RecursiveParser


def tree_to_string(root):
    if not root:
        return ""
    left = f"({tree_to_string(root.left)})" if root.left or root.right else ""
    right = f"({tree_to_string(root.right)})" if root.right else ""
    return f"{root.value}{left}{right}"


def visualize_tree(root, level=0, prefix="Root: "):
    if root is None:
        return

    # Печать текущего узла
    print(" " * (level * 4) + prefix + str(root.value))

    # Рекурсивный вызов для левого и правого поддерева
    if root.left or root.right:
        if root.left:
            visualize_tree(root.left, level + 1, "L--- ")
        else:
            print(" " * ((level + 1) * 4) + "L--- None")

        if root.right:
            visualize_tree(root.right, level + 1, "R--- ")
        else:
            print(" " * ((level + 1) * 4) + "R--- None")


def print_tree_graphically(root):
    """
    Функция для красивого графического вывода дерева.
    Использует горизонтальные и вертикальные линии для отображения структуры.
    """

    def build_tree_string(root, prefix="", is_left=True):
        if root is None:
            return ""

        tree_str = ""
        if root.right:
            tree_str += build_tree_string(root.right, prefix + ("│   " if is_left else "    "), False)

        tree_str += prefix + ("├── " if is_left else "└── ") + str(root.value) + "\n"

        if root.left:
            tree_str += build_tree_string(root.left, prefix + ("    " if is_left else "│   "), True)

        return tree_str

    print(build_tree_string(root))


def search_node(root, value):
    value = str(value)
    stack = [(root, None)]

    while stack:
        node, parent = stack.pop()
        if not node:
            continue
        if node.value == value:
            return node, parent
        stack.append((node.right, node))
        stack.append((node.left, node))

    return None, None


def add_node(root, value):
    if not root:
        return TreeNode(str(value))  # Узлы хранятся как строки
    if value < int(root.value):
        root.left = add_node(root.left, value)
    elif value > int(root.value):
        root.right = add_node(root.right, value)
    return root


def delete_node(root, value):
    if not root:
        return root
    if value < int(root.value):
        root.left = delete_node(root.left, value)
    elif value > int(root.value):
        root.right = delete_node(root.right, value)
    else:
        if not root.left and not root.right:
            return None
        if not root.left:
            return root.right
        if not root.right:
            return root.left

        min_larger_node = find_min(root.right)
        root.value = min_larger_node.value
        root.right = delete_node(root.right, int(min_larger_node.value))
    return root


def find_min(node):
    while node.left:
        node = node.left
    return node


def menu(root):
    while True:
        print("\nМеню:")
        print("1. Поиск элемента")
        print("2. Добавление элемента")
        print("3. Удаление элемента")
        print("4. Вывести дерево")
        print("5. Визуализировать дерево")
        print("6. Выход")

        choice = input("Выберите опцию: ")

        if choice == "1":
            try:
                value = int(input("Введите значение для поиска: "))
                node, parent = search_node(root, value)
                if node:
                    parent_value = parent.value if parent else "Нет (это корень)"
                    print(f"Элемент найден: {node.value}, родитель: {parent_value}.")
            except ValueError:
                print("Ошибка: введите корректное число.")

        elif choice == "2":
            try:
                value = int(input("Введите значение для добавления: "))
                root = add_node(root, value)
                print("Элемент добавлен.")
            except ValueError:
                print("Ошибка: введите корректное число.")

        elif choice == "3":
            try:
                value = int(input("Введите значение для удаления: "))
                node, parent = search_node(root, value)
                if node:
                    root = delete_node(root, value)
                    print("Элемент удалён.")
                else:
                    print("Элемент не найден.")
            except ValueError:
                print("Ошибка: введите корректное число.")

        elif choice == "4":
            print("Дерево:", tree_to_string(root))

        elif choice == "5":
            print("Дерево графически:")
            print_tree_graphically(root)

        elif choice == "6":
            print("Выход. Итоговое дерево:")
            print(tree_to_string(root))
            break

        else:
            print("Неверный ввод, попробуйте снова.")


if __name__ == "__main__":
    tree_string = '8(3(1,6(4,7)),10(,14(13,)))'
    parser = RecursiveParser(tree_string)
    root = parser.root
    print(tree_to_string(root))
    menu(root)
