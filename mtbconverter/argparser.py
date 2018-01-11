"""Argument parser collection for conversion
and pushing to CentraXX"""

import argparse

def conversion_parser():
    parser = argparse.ArgumentParser(prog="convert", description="Conversion of "
    "variant information into CentraXX schema conform XML.")
    parser.add_argument('-i', metavar="archive.zip" , help='ZIP archive containing the variant information files.')
    return parser