import time
from collections import defaultdict
from Trie import Trie
import pickle

words = []


def all_letters_present(word: str, must_have: list[str]):
    for letter in must_have:
        if letter not in word:
            return False

    return True


def backtrack(i: int, start_word: list[str], curr_word: list[str], possible_letters: list[str],
              trie: Trie, must_have_letters: list[str], skip_map: defaultdict[str, set[str]]):
    if i == 5:
        found_word = "".join(curr_word)
        checks_out = trie.find(found_word)
        if checks_out and all_letters_present(found_word, must_have_letters):
            words.append(found_word)
        return

    skipped = skip_map[i]
    for c in possible_letters:
        if c in skipped:
            continue
        if start_word[i] != " ":
            if start_word[i] == c:
                backtrack(i + 1, start_word, curr_word,
                          possible_letters, trie, must_have_letters, skip_map)
        else:
            if curr_word[i] == " ":
                curr_word[i] = c
            if trie.prefix_exists(curr_word[:i + 1]):
                backtrack(i + 1, start_word, curr_word,
                          possible_letters, trie, must_have_letters, skip_map)
            curr_word[i] = " "


def main():
    word = list(
        input("Input word so far, include confirmed characters and spaces:\t"))
    possible_letters = list(
        input("Type in all possible letters, no spaces:\t"))
    must_have_letters = list(
        input("Letters that must be included, no spaces:\t"))
    use_starters = input("Used all the starter words? y or n:\t")
    starter_words = ["quick", "brave", "nymph", "fjord", "twigs"]
    skip_map = defaultdict(set)
    trie = Trie()

    start_time = time.time()

    # ensure the trie pickle object has been generated, if not run word_list
    with open("trie.pkl", "rb") as f:
        trie = pickle.load(f)

    # if the starter words have been used, you can eliminate more options for each index
    if use_starters.capitalize() == "Y":
        for starter_word in starter_words:
            for i, c in enumerate(starter_word):
                skip_map[i].add(c)

    # letters that are correctly placed might have been marked for skipping in the previous step
    for i, c in enumerate(word):
        if c in skip_map[i]:
            skip_map[i].remove(c)

    backtrack(0, word.copy(), word.copy(), possible_letters,
              trie, must_have_letters, skip_map)

    with open("words.txt", "w", encoding="utf-8", newline="") as file:
        for n in sorted(list(set(words))):
            print(n)
            file.write(n + "\n")
    print(f"{len(set(words))} word{"s" if len(set(words)) != 1 else ""} found")
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()
