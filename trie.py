class Node:
    def __init__(self, value=''):
        self.value = value
        self.is_end = False
        self.children = {}

    def __repr__(self):
        return f"<Node '{self.value}' {[child for child in self.children]}>"


class Trie:
    def __init__(self):
        self._root = Node()

    def insert(self, word):
        """
        Creates nodes which represent a word if it does not exist.
        """

        node = self._root

        for character in word:
            if character in node.children:
                node = node.children[character]

            else:
                new_node = Node(character)
                node.children[character] = new_node
                node = new_node

        node.is_end = True

    def find(self, word):
        """
        Checks if a word exists in Trie or not.
        """

        node = self._root

        for character in word:
            if character not in node.children:
                return False

            node = node.children[character]

        return True
