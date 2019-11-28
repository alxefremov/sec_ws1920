import argparse


def en_de_crypt_tool(cipher_name: str) -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="A program used to encrypt and decrypt messages using a "
                    f"{cipher_name} cipher."
    )

    parser.add_argument('file',
                        help="File, containing the message to be encrypted",
                        metavar='FILE')
    key_group = parser.add_mutually_exclusive_group(required=True)
    key_group.add_argument('--encrypt',
                           help="Encrypt the file with key KEY",
                           metavar='KEY',
                           dest='encrypt_key')
    key_group.add_argument('--decrypt',
                           help="Decrypt the file with key KEY",
                           metavar='KEY',
                           dest='decrypt_key')
    parser.add_argument('--out',
                        help="The file to output the result to. "
                             "If omitted, outputs to stdout",
                        metavar='FILE',
                        dest='out_file')

    return parser
