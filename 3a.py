class Node:
    def __init__(self, value=None):
        self.value = value
        self.edges = []

class Tree:
    def __init__(self, root_value=None):
        self.root = Node(root_value)

    def add_node(self, parent, value):
        new_node = Node(value)
        parent.edges.append(new_node)
        return new_node

    def traverse(self, node, visit_func, depth=0):
        if node is not None:
            visit_func(node, depth)
            for edge in node.edges:
                self.traverse(edge, visit_func, depth + 1)

    #dekorator
    @property
    def min_value(self):
        values = []

        def collect_values(node, _):
            values.append(node.value)

        self.traverse(self.root, collect_values)

        return min(values) if values else None

    def __str__(self):
        tree_str = []
        self.traverse(self.root, lambda node, depth: tree_str.append("  " * depth + str(node.value)))
        return "\n".join(tree_str)

if __name__ == "__main__":
    my_tree = Tree(5)
    b_node = my_tree.add_node(my_tree.root, 3)
    c_node = my_tree.add_node(my_tree.root, 8)
    my_tree.add_node(b_node, 2)
    my_tree.add_node(b_node, 4)
    my_tree.add_node(c_node, 7)

    print("tree:")
    print(my_tree)
    print("Najmniejsza wartość w tree:", my_tree.min_value)
