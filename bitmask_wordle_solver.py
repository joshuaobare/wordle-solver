import time
import pickle
from collections import defaultdict


def get_mask(letters_list):
    mask = 0
    for char in letters_list:
        if 'a' <= char <= 'z':
            mask |= (1 << (ord(char) - ord('a')))
    return mask


def solve():
    raw_pattern = input("Pattern (e.g., 's a  '): ").lower()
    # Ensure pattern is exactly 5 chars, padding with spaces if needed
    target_pattern = raw_pattern.ljust(5)[:5]

    possible_str = input("Possible letters: ").lower()
    must_have_str = input("Must-have letters: ").lower()

    must_have_mask = get_mask(list(must_have_str))
    possible_mask = get_mask(list(possible_str))

    print("Loading optimized Trie...")
    with open("trie.pkl", "rb") as f:
        trie = pickle.load(f)

    found_words = []
    start_time = time.time()

    def backtrack(node, depth, current_path_mask, current_word):
        if depth == 5:
            if node.word_end and (current_path_mask & must_have_mask) == must_have_mask:
                found_words.append("".join(current_word))
            return

        remaining_needed = must_have_mask & ~current_path_mask
        if remaining_needed and not (node.descendant_mask & remaining_needed):
            return

        char_at_pos = target_pattern[depth]

        if char_at_pos != ' ':
            if char_at_pos in node.children:
                char_bit = 1 << (ord(char_at_pos) - ord('a'))
                backtrack(node.children[char_at_pos], depth + 1,
                          current_path_mask | char_bit, current_word + [char_at_pos])
        else:
            for char, child_node in node.children.items():
                char_bit = 1 << (ord(char) - ord('a'))
                if char_bit & possible_mask:
                    backtrack(child_node, depth + 1,
                              current_path_mask | char_bit, current_word + [char])

    backtrack(trie.root, 0, 0, [])

    for w in sorted(found_words):
        print(w)
    print(
        f"\nFound {len(found_words)} words in {time.time() - start_time:.4f}s")


if __name__ == "__main__":
    solve()
