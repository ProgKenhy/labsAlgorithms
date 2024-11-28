from tree_parser import RecursiveParser


class NonRecursiveParser(RecursiveParser):
    def parse(self, idx=0):
        stack = []
        current_node = None
        root = None

        while idx < len(self.tree):
            char = self.tree[idx]

            if char.isdigit():
                value, idx = self.full_number_parse(idx)
                new_node = self.node_factory(value)

                if not root:
                    root = new_node

                if current_node:
                    if not current_node.left:
                        current_node.left = new_node
                    elif not current_node.right:
                        current_node.right = new_node

                stack.append(new_node)
                current_node = new_node

            elif char == '(':
                idx += 1
            elif char == ',':
                idx += 1
                if stack:
                    current_node = stack[-1]
            elif char == ')':
                idx += 1
                if stack:
                    current_node = stack.pop()
            else:
                idx += 1
        return root, idx


if __name__ == '__main__':
    tree_string = "8(3(1,6(4,7)),10(,14(13,)))"

    # Используем рекурсивный парсер
    parser = NonRecursiveParser(tree_string)
    root = parser.root

    def preorder(node):
        """
        Прямой обход: узел -> левое поддерево -> правое поддерево.
        :param node: Текущий узел
        """

        if node:
            print(node.value, end=" ")
            preorder(node.left)
            preorder(node.right)

    print("Прямой обход")
    preorder(root)