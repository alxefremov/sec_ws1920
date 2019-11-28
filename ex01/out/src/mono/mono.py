#!/usr/bin/env python3

from utils.argument_parsers import en_de_crypt_tool
from utils.constants import ALPHABET
from utils.filetools import read_from_file, write_to_file
from utils.strtools import skip_and_lowercase


def _encrypt(input_text: str, key: str, alphabet: str = ALPHABET) -> str:
    """
    Encrypts a string using monoalphabetic substitution

    :param input_text: message to encrypt cipher
    :param key: substitution key
    :param alphabet: plaintext alphabet
    :return: encrypted message
    """
    result = ''
    for ch in input_text:
        result += key[alphabet.index(ch)]
    return result


if __name__ == "__main__":
    parser = en_de_crypt_tool("monoalphabetic substitution")
    args = parser.parse_args()

    input_message = skip_and_lowercase(read_from_file(args.file))

    if args.encrypt_key:
        output_message = _encrypt(input_message, args.encrypt_key, ALPHABET)
    else:
        # the cipher is symmetric, so switching the key and the alphabet would
        # make the function decrypting
        output_message = _encrypt(input_message, ALPHABET, args.decrypt_key)

    if args.out_file:
        write_to_file(args.out_file, output_message)
    else:
        print(output_message)
