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

CURRENT_WD = os.path.dirname(__file__)

class ArchiveTests(unittest.TestCase):
    """Test suite for archive integrity checks"""

    @patch('zipfile.ZipFile')
    @raises(MtbUnknownFileType)
    def test_unknown_file_type(self, MockZipFile):
        ziparchive = MockZipFile()
        ziparchive.infolist.return_value = [
            'QUK170001AE_germline_snv.tsv',
            'QUK170001AE_noclue_snv.tsv'
            ]
        MtbConverter(ziparchive)


    @patch('zipfile.ZipFile')
    @raises(MtbIncompleteArchive)
    def test_incomplete_archive(self, MockZipFile):
        ziparchive = MockZipFile()
        ziparchive.infolist.return_value = [
            'QUK170001AE_germline_snv.tsv'
        ]
        MtbConverter(ziparchive)

    @patch('zipfile.ZipFile')
    def test_complete_archive(self, MockZipFile):
        ziparchive = MockZipFile()
        ziparchive.infolist.return_value = [
            'QUK170001AE_germline_snv.tsv',
            'QUK170001AE_germline_cnv.tsv',
            'QUK170001AE_somatic_snv.tsv',
            'QUK170001AE_somatic_cnv.tsv',
            'QUK170001AE_somatic_sv.tsv',
            'QUK170001AE_metadata.tsv'
        ]
        MtbConverter(ziparchive)
    # Check: The Archive must contain 6 tsv files

    # Check: The tsv files must follow a naming scheme
    # <barcode>_somatic_snv.tsv
    # <barcode>_somatic_cnv.tsv
    # <barcode>_germline_snv.tsv
    # <barcode>_germline_cnv.tsv
    # <barcode>_sv.tsv
    # <barcode>_metadata.tsv

    # Check: Barcode must be the same for archive and ALL
    # tsv files