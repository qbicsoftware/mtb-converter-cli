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
    @patch('zipfile.ZipInfo')
    @raises(MtbUnknownFileType)
    def test_unknown_file_type(self, MockZipFile, MockZipInfo):
        ziparchive = MockZipFile()
        zipinfo_1 = MockZipInfo()
        zipinfo_1.filename = "QUK17001AE_unvalid_name.tsv"
        ziparchive.infolist.return_value = [
            zipinfo_1
        ]
        MtbConverter(ziparchive, "QUK17001AE", "QUK17ENTITY-1")


    @patch('zipfile.ZipFile')
    @patch('zipfile.ZipInfo')
    @raises(MtbIncompleteArchive)
    def test_incomplete_archive(self, MockZipFile, MockZipInfo):
        ziparchive = MockZipFile()
        zipinfo_1 = MockZipInfo()
        zipinfo_1.filename = "QUK17001_somatic_snv.tsv"
        ziparchive.infolist.return_value = [
            zipinfo_1
        ]
        MtbConverter(ziparchive, "QUK17001", "QUK17ENTITY-1")

    @raises(MtbUnknownBarcode)
    @patch('zipfile.ZipFile')
    @patch('zipfile.ZipInfo')
    def test_different_barcode(self, MockZipFile, MockZipInfo):
        ziparchive = MockZipFile()
        zipinfo_1 = MockZipInfo()
        barcode = "QUK17002AE"
        ziparchive.infolist.return_value = [
            zipinfo_1
        ]
        MtbConverter(ziparchive, barcode, "QUK17ENTITY-1")
