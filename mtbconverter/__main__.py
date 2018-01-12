"""mtbconverter.__main__: executed, when mtbconverter directory is called as a script"""
import sys
from .mtbconverter import MtbConverter
from .argparser import *
from .utils import getbarcode
from zipfile import ZipFile

__version__ = "0.1.0"

commands = ['convert', 'push']

def main(args=None):
    """The main routine, parsing arguments and calls the converter"""
    print("Mtbconverter version {}.".format(__version__))
    if args is None:
        args = sys.argv
    if "-h" in args[1] or "--help" in args[1]:
        print(help_message())
    if args[1] not in commands:
        print(help_message())
    if args[1] == 'convert':
        parser = conversion_parser()
        start_conversion(parser.parse_args(args[2:]))

def start_conversion(args):
    converter = MtbConverter(ZipFile(args.i), getbarcode(args.i))
    converter.convert()

def help_message():
    msg = "Usage: mtbconverter.py [-h] [command]\n\n"\
    "command:\n"\
    "\tconvert\t- Converts variant information into CentraXX XML.\n"\
    "\tpush\t- Pushes one ore more XML files to CentraXX.\n"
    return msg

if __name__ == "__main__":
    main()
