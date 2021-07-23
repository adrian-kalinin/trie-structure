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
        Creates nodes that represent a word if it does not exist.
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
        Returns boolean result that depends on existence of given word.
        """

        node = self._root

        for character in word:
            if character not in node.children:
                return False

            node = node.children[character]

        return True

    def _dfs(self, node, prefix, words):
        """
        Depth-first traversal to find complete words.
        """

        if node.is_end:
            words.append(prefix + node.value)

        for child in node.children.values():
            self._dfs(child, prefix + node.value, words)

    def search(self, prefix):
        """
        Returns a list of words that start with given prefix.
        """

        node = self._root
        words = []

        for character in prefix:
            if character in node.children:
                node = node.children[character]

            else:
                return words

        self._dfs(node, prefix[:-1], words)

        return words

    @classmethod
    def from_words(cls, words):
        """
        Returns Trie with given words.
        """

        _trie = cls()

        for word in words:
            _trie.insert(word)

        return _trie
