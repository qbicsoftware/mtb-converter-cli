"""Argument parser collection for conversion
and pushing to CentraXX"""

import argparse

def conversion_parser():
    parser = argparse.ArgumentParser(prog="convert", description="Conversion of "
    "variant information into CentraXX schema conform XML.")
    parser.add_argument('archive' , help='ZIP archive containing the variant information files.')
    parser.add_argument('patientID' , help='A QBiC patient ID.')
    return parser

def push_parser():
    parser = argparse.ArgumentParser(prog="push", description="Import a converted XML file "
    "into CentraXX.")
    parser.add_argument('-c', metavar="config", default="/etc/centraxx.config", help='Configuration file with settings for the remote CentraXX system. (Default: /etc/centraxx.config)')
    parser.add_argument('data.xml', help='Converted XML file from ZIP archive with the variant information.')
    return parser