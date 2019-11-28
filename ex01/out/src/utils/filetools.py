"""Package with utilitary methods to work with strings"""


def read_from_file(file: str) -> str:
    """
    Reads data from file

    :param file: Path to file
    :return: File contents
    """
    with open(file, 'r', encoding='utf-8') as file_obj:
        return file_obj.read()


def write_to_file(file: str, content: str) -> None:
    """
    Writes data to file

    :param file: Path to file
    :param content: File contents
    """
    with open(file, 'w', encoding='utf-8') as file_obj:
        file_obj.write(content)
