import pickle
import time


class TrieNode:
    __slots__ = ['children', 'word_end', 'descendant_mask']

    def __init__(self):
        self.children = {}
        self.word_end = False
        self.descendant_mask = 0


class OptimizedTrie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        word_mask = 0
        for char in word:
            word_mask |= (1 << (ord(char) - ord('a')))

        for c in word:
            curr.descendant_mask |= word_mask
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word_end = True
        curr.descendant_mask |= word_mask


def build_and_save(input_file="word_list.txt", output_file="trie.pkl"):
    trie = OptimizedTrie()
    start_time = time.time()

    print(f"Reading {input_file}...")
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            count = 0
            for line in f:
                word = line.strip().lower()
                if len(word) == 5 and word.isalpha():
                    trie.insert(word)
                    count += 1
                    if count % 10000 == 0:
                        print(f"Inserted {count} words...")
    except FileNotFoundError:
        print("Error: word_list.txt not found.")
        return

    print(f"Saving to {output_file}...")
    with open(output_file, 'wb') as f:
        pickle.dump(trie, f)

    print(f"Done! Processed {count} words in {time.time() - start_time:.2f}s")


if __name__ == "__main__":
    build_and_save()
