class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class RecursiveParser:
    def __init__(self, tree, node_factory=None):
        self.tree = tree
        self.node_factory = node_factory or self.default_node_factory
        self.root, _ = self.parse()

    @staticmethod
    def default_node_factory(value):
        return TreeNode(value)

    def full_number_parse(self, idx):
        start = idx

        while idx < len(self.tree) and self.tree[idx].isdigit():
            idx += 1
        return self.tree[start:idx], idx

    def parse(self, index=0):
        value, index = self.full_number_parse(index)
        root = self.node_factory(value)

        if index < len(self.tree) and self.tree[index] == "(":
            index += 1
            if self.tree[index] != ",":
                root.left, index = self.parse(index)
            if self.tree[index] == ",":
                index += 1
            if self.tree[index] != ")":
                root.right, index = self.parse(index)
            index += 1
        return root, index

    def parse_tree(self):
        self.root, _ = self.parse()
        return self.root


