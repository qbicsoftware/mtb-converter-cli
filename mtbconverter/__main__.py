"""mtbconverter.__main__: executed, when mtbconverter directory is called as a script"""

import sys

def main(args=None):
    """The main routine, parsing arguments and calls the converter"""
    if args is None:
        args = sys.argv[1:]
    print(args)


if __name__ == "__main__":
    main()
