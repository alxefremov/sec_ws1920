#!/usr/bin/env python3
import argparse

from utils.constants import ALPHABET_SORTED, ALPHABET, POPULAR_WORDS
from utils.strtools import skip_and_lowercase, shingle


def _most_common_substrings(message: str, size: int) -> list:
    """
    Finds the most common substring of a given size inside a message using
    shingles

    :param message: message to inspect
    :param size: substring size
    :return: the most common substring
    """
    words = dict()

    for sh in shingle(message, size):
        if sh in words:
            words[sh] += 1
        else:
            words[sh] = 1
    return list(map(
        lambda i: i[0],
        sorted(words.items(), key=lambda i: i[1], reverse=True)
    ))


def _sort_message_letters(message: str,
                          alphabet: str,
                          reverse: bool = False) -> str:
    charmap = []
    for letter in alphabet:
        charmap.append([letter, 0])

    for character in message:
        if character in alphabet:
            charmap[alphabet.index(character)][1] += 1

    return ''.join(map(lambda p: p[0],
                       sorted(charmap, key=lambda p: p[1], reverse=reverse)))


def _derive_key(message: str,
                alphabet: str = ALPHABET,
                alphabet_sorted: str = ALPHABET_SORTED) -> str:
    cipher_map = dict()
    used_shingles = []

    for word in POPULAR_WORDS:
        similar_shingles = _most_common_substrings(message, len(word))
        i = 0
        while similar_shingles[i] in used_shingles:
            i += 1
        for j in range(len(similar_shingles[i])):
            if word[j] not in cipher_map \
                    and similar_shingles[i][j] not in cipher_map.values():
                cipher_map[word[j]] = similar_shingles[i][j]
        used_shingles.append(similar_shingles[i])

    message_sorted = _sort_message_letters(message, alphabet, True)

    alphabet_idx, message_idx = 0, 0

    while message_idx < len(message_sorted) \
            and alphabet_idx < len(alphabet_sorted):
        if message_sorted[message_idx] in cipher_map.values():
            message_idx += 1
            continue
        if alphabet_sorted[alphabet_idx] in cipher_map.keys():
            alphabet_idx += 1
            continue
        cipher_map[alphabet_sorted[alphabet_idx]] = message_sorted[message_idx]

    return ''.join(map(
        lambda it: it[1],
        sorted(
            cipher_map.items(),
            key=lambda it: it[0]
        )
    ))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="A program used to decipher the messages encrypted with the"
                    "monoalphabetic substitution cipher."
    )

    parser.add_argument('message',
                        help="The encrypted message",
                        metavar='MESSAGE')

    args = parser.parse_args()

    input_message = skip_and_lowercase(args.message)
    key = _derive_key(input_message)
    print(key)
