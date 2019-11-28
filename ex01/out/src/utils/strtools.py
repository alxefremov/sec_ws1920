"""Package with utilitary methods to work with strings"""


def skip_and_lowercase(message: str) -> str:
    """
    Removes all non-alphabetic symbols from the string and converts it to
    lowercase

    :param message: The message to convert
    :return: The converted message
    """
    return ''.join(filter(lambda x: x.isalpha(), message)).lower().strip()


def shingle(message: str, shingle_size: int):
    """
    Shingle generator for a message. Breaks message into equal size blocks, each
    one character offset from the previous.

    :param message: message to shingle
    :param shingle_size: size of the shingle
    """
    for i in range(len(message) - shingle_size + 1):
        yield message[i:i + shingle_size]
