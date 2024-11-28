from tree_parser import RecursiveParser

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


    def preorder(node):
        """
        Прямой обход: узел -> левое поддерево -> правое поддерево.
        :param node: Текущий узел
        """

        if node:
            print(node.value, end=" ")
            preorder(node.left)
            preorder(node.right)


    def inorder(node):
        """
        Центральный обход: левое поддерево -> узел -> правое поддерево.
        :param node: Текущий узел
        """
        if node:
            inorder(node.left)
            print(node.value, end=" ")
            inorder(node.right)


    def postorder(node):
        """
        Концевой обход: левое поддерево -> правое поддерево -> узел.
        :param node: Текущий узел
        """
        if node:
            postorder(node.left)
            postorder(node.right)
            print(node.value, end=" ")


    print("Прямой обход")
    preorder(root)

    print("\nЦентральный обход")
    inorder(root)

    print("\nКонцевой обход")
    postorder(root)
