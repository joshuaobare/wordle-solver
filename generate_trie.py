import pickle
from Trie import Trie


def main():
    trie = Trie()
    words = []

    with open("word_list.txt", "r") as f:
        words = [word.strip() for word in f if word.strip()]

    for word in words:
        if len(word) == 5:
            trie.insert(word)

    with open("trie.pkl", "wb") as f:
        pickle.dump(trie, f)


if __name__ == "__main__":
    main()
