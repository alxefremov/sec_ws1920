#!/usr/bin/env python3

from utils.argument_parsers import en_de_crypt_tool
from utils.constants import ALPHABET
from utils.filetools import read_from_file, write_to_file
from utils.strtools import skip_and_lowercase


def _compose_key(key: str, message_len: int) -> str:
    result = key*((message_len // len(key)) + 1)
    return result[:message_len]


def _crypt(encrypt: bool, input_text: str, key: str, alphabet: str = ALPHABET) -> str:
    """
    Encrypts a string using Vigenère cipher

    :param input_text: message to encrypt with cipher
    :param key: cipher key
    :param alphabet: plaintext alphabet
    :return: encrypted message
    """
    result = ''
    composed_key = _compose_key(key, len(input_text))

    for ch_idx in range(len(input_text)):
        if encrypt:
            new_idx = alphabet.index(input_text[ch_idx]) \
                    + alphabet.index(composed_key[ch_idx])
        else:
            new_idx = alphabet.index(input_text[ch_idx]) \
                      - alphabet.index(composed_key[ch_idx])

        if new_idx < 0:
            new_idx += len(alphabet)
        elif new_idx >= len(alphabet):
            new_idx -= len(alphabet)
        result += alphabet[new_idx]

    return result


if __name__ == "__main__":
    parser = en_de_crypt_tool("Vigenère")
    args = parser.parse_args()

    input_message = skip_and_lowercase(read_from_file(args.file))

    if args.encrypt_key:
        output_message = _crypt(True, input_message, args.encrypt_key, ALPHABET)
    else:
        output_message = _crypt(False, input_message, args.decrypt_key, ALPHABET)

    if args.out_file:
        write_to_file(args.out_file, output_message)
    else:
        print(output_message)
