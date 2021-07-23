class Node:
    def __init__(self, value=''):
        self.value = value
        self.is_end = False
        self.children = {}

    def __repr__(self):
        return f"<Node '{self.value}' {[child for child in self.children]}>"


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        node = self.root

        for character in word:
            if character in node.children:
                node = node.children[character]

            else:
                new_node = Node(character)
                node.children[character] = new_node
                node = new_node

        node.is_end = True

    def search(self):
        pass
