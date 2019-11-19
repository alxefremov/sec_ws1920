import argparse
from datetime import datetime
import os
import sys

class Exercise00:
    STUDENT_NAME = "Nikita Karamov"

    def __init__(self, value="abcdefghijklmnopqrstuvwxyz"):
        self._txt = value;

    @staticmethod
    def deadline(fmt):
        return datetime(2019, 11, 13, 11, 59, 00).strftime(fmt)

    @property
    def txt(self):
        return self._txt[:17] + '...'

    def format(self, mode):
        if mode == 'order':
            return "{2} - {1} - {0}"
        elif mode == 'dict':
            return "x, y = ({x:.1f}, {y:.4f})"
        return ""

    def listfiles(self, dir, extension=None):
        for _, _, files in os.walk(dir):
            for file in files:
                if extension is None or file.endswith(extension):
                    yield file

    def __call__(self, **kwargs):
        output = []

        for k, v in kwargs.items():
            output.append("{} = {}".format(k, v))
        
        return "\n".join(sorted(output))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('file',
                        help="The input positional parameter.",
                        metavar='FILE')
    parser.add_argument('-b', '--bool',
                        action='store_true',
                        help="An optional boolean flag (Default: False).",
                        dest='bool')
    parser.add_argument('-f', '--float',
                        type=float,
                        default=0.0,
                        help="An optional parameter of type float (Default: 0.0).",
                        metavar='FLOAT',
                        dest='float')
    parser.add_argument('-i', '--int',
                        type=int,
                        default=0,
                        help="An optional parameter of type int (Default: 0).",
                        metavar="INT",
                        dest='int')

    args = parser.parse_args()

    print("input: {}\n--bool {}\n--float {}\n--int {}".format(
        args.file,
        args.bool,
        args.float,
        args.int
    ))

    sys.exit(42)
