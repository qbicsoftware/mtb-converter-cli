"""
Tests for zip archive integrity check
"""
import os
import unittest
from unittest.mock import patch, Mock
from nose.tools import raises
from zipfile import ZipFile

from mtbconverter.mtbconverter import MtbConverter
from mtbconverter.mtbconverter_exceptions import MtbUnknownFileType
from mtbconverter.mtbconverter_exceptions import MtbIncompleteArchive
from mtbconverter.mtbconverter_exceptions import MtbUnknownBarcode

CURRENT_WD = os.path.dirname(__file__)

class ArchiveTests(unittest.TestCase):
    """Test suite for archive integrity checks"""

    @patch('zipfile.ZipFile')
    @raises(MtbUnknownFileType)
    def test_unknown_file_type(self, MockZipFile):
        ziparchive = MockZipFile()
        ziparchive.infolist.return_value = [
            'QUK17001AE_germline_snv.tsv',
            'QUK17001AE_noclue_snv.tsv'
            ]
        MtbConverter(ziparchive, "")


    @patch('zipfile.ZipFile')
    @raises(MtbIncompleteArchive)
    def test_incomplete_archive(self, MockZipFile):
        ziparchive = MockZipFile()
        ziparchive.infolist.return_value = [
            'QUK17001AE_germline_snv.tsv'
        ]
        MtbConverter(ziparchive, "")


    @patch('zipfile.ZipFile')
    def test_complete_archive(self, MockZipFile):
        ziparchive = MockZipFile()
        ziparchive.infolist.return_value = [
            'QUK17001AE_germline_snv.tsv',
            'QUK17001AE_germline_cnv.tsv',
            'QUK17001AE_somatic_snv.tsv',
            'QUK17001AE_somatic_cnv.tsv',
            'QUK17001AE_somatic_sv.tsv',
            'QUK17001AE_metadata.tsv'
        ]
        MtbConverter(ziparchive, "")


    @raises(MtbUnknownBarcode)
    @patch('zipfile.ZipFile')
    def test_different_barcode(self, MockZipFile):
        ziparchive = MockZipFile()
        barcode = "QUK17002AE"
        ziparchive.infolist.return_value = [
            'QUK17002AE_germline_snv.tsv',
            'QUK17002AE_germline_cnv.tsv',
            'QUK17001AE_somatic_snv.tsv',
            'QUK17002AE_somatic_cnv.tsv',
            'QUK17001AE_somatic_sv.tsv',
            'QUK17002AE_metadata.tsv'
        ]
        MtbConverter(ziparchive, barcode)

    @patch('zipfile.ZipFile')
    def test_common_barcode(self, MockZipFile):
        ziparchive = MockZipFile()
        barcode = "QUK17002AE"
        ziparchive.infolist.return_value = [
            'QUK17002AE_germline_snv.tsv',
            'QUK17002AE_germline_cnv.tsv',
            'QUK17002AE_somatic_snv.tsv',
            'QUK17002AE_somatic_cnv.tsv',
            'QUK17002AE_somatic_sv.tsv',
            'QUK17002AE_metadata.tsv'
        ]
        MtbConverter(ziparchive, barcode)
    # Check: The tsv files must follow a naming scheme
    # <barcode>_somatic_snv.tsv
    # <barcode>_somatic_cnv.tsv
    # <barcode>_germline_snv.tsv
    # <barcode>_germline_cnv.tsv
    # <barcode>_sv.tsv
    # <barcode>_metadata.tsv

    # Check: Barcode must be the same for archive and ALL
    # tsv files