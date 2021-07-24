from trie import Trie


trie = Trie.from_words([
    'bat', 'bats', 'batman', 'batgirl',
    'application', 'apartment', 'apple',
    'car', 'bus', 'airplane'
])

print(trie.search('bat'))
# ['bat', 'bats', 'batman', 'batgirl']

print(trie.search('ap'))
# ['application', 'apple', 'apartment']

print(trie.search('app'))
# ['application', 'apple']
