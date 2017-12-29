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

CURRENT_WD = os.path.dirname(__file__)

class ArchiveTests(unittest.TestCase):
    """Test suite for archive integrity checks"""

    @patch('zipfile.ZipFile')
    def setUp(self, MockZipFile ):
        self.ziparchive_wrong_type = MockZipFile()
        self.ziparchive_wrong_type.infolist.return_value = [
                'QUK170001AE_germline_snv.tsv',
                'QUK170001AE_noclue_snv.tsv',
            ]
        

    @raises(MtbUnknownFileType)
    def test_unknown_file_type(self):
        converter = MtbConverter(self.ziparchive_wrong_type)

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