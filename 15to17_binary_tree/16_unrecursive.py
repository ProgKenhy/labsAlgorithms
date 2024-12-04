from tree_parser import RecursiveParser


def iterative_preorder(root):
    if root is None:
        return []

    stack = [root]
    result = []
    while stack:
        node = stack.pop()
        result.append(node.value)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
        check_stack = []
        for i in stack:
            check_stack.append(i.value)
        print(check_stack)

    return result


if __name__ == "__main__":
    tree_string = "8(3(1,6(4,7)),10(,14(13,)))"

    parser = RecursiveParser(tree_string)

    root = parser.parse_tree()

    """
            8
           ↙ ↘
          3   10
         ↙ ↘    ↘
        1   6    14
           ↙ ↘   ↙
          4   7 13
    """

    print("Нерекурсивный прямой обход:", iterative_preorder(root))
