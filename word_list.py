import pickle


class TrieNode:
    def __init__(self):
        self.word_end = False
        self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()

            curr = curr.children[c]

        curr.word_end = True

    def find(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]

        return True

    def prefix_exists(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]

        return True


trie = Trie()
words = []

with open("word_list.txt", "r") as f:
    words = [word.strip() for word in f if word.strip()]

for word in words:
    if len(word) == 5:
        trie.insert(word)

with open("trie.pkl", "wb") as f:
    pickle.dump(trie, f)
