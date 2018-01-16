"""mtbconverter.__main__: executed, when mtbconverter directory is called as a script"""
import sys
from mtbparser import snv_utils
from .mtbconverter import MtbConverter
from .argparser import *
from .utils import getbarcode
from zipfile import ZipFile
from .cx_controlled_vocabulary import ControlledVocabulary
from .cx_parameters import Parameters

__version__ = "0.1.0"

COMMANDS = ['convert', 'push', 'catalogue']


def main(args=None):
    """The main routine, parsing arguments and calls the converter"""
    print("Mtbconverter version {}.".format(__version__))
    if args is None:
        args = sys.argv
    if len(args) < 2:
        print(help_message())
        sys.exit(1)
    if "-h" in args[1] or "--help" in args[1]:
        print(help_message())
    if args[1] not in COMMANDS:
        print(help_message())
    if args[1] == 'convert':
        parser = conversion_parser()
        start_conversion(parser.parse_args(args[2:]))
    if args[1] == 'catalogue':
        build_catalogue()


def start_conversion(args):
    """Starts the file extraction, parsing and writes the
    output in XML files"""
    path_zipfile = args.i
    barcode = getbarcode(path_zipfile)
    converter = MtbConverter(ZipFile(path_zipfile), barcode)
    converter.convert()


def build_catalogue():
    """Builds the XML catalogue for CentraXX according to the 
    file header specifications"""
    cv = ControlledVocabulary()
    params = Parameters()
    xml_cv = cv.getXML()
    xml_params = params.getXML()
    with open('cv_centraxx.xml', 'w') as output:
        output.write(xml_cv.decode('utf-8'))
    with open('params_centraxx.xml', 'w') as output:
        output.write(xml_params.decode('utf-8'))
    

def help_message():
    """Builds the string for the help message"""
    msg = "Usage: mtbconverter.py [-h] [command]\n\n"\
    "command:\n"\
    "\tconvert\t\tConverts variant information into CentraXX XML.\n"\
    "\tpush\t\tPushes one ore more XML files to CentraXX.\n"\
    "\tcatalogue\tBuilds CentraXX catalogue XML files."
    return msg

if __name__ == "__main__":
    main()
