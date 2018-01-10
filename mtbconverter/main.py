"""mtbconverter.main: provides entry point main()."""

__version__ = "0.1.0"

import sys
from .mtbconverter import MtbConverter

def main():
    print("Startin mtbconverter version {}.".format(__version__))
    print(sys.argv)