"""
Tests for util methods
"""
import os
import unittest
from nose.tools import raises
from mtbconverter import utils

INVALID_BARCODE = "QLAUCH123AE"
VALID_BARCODE = "QAHJH006A4"
INVALID_PATH = "my/file/QLAUCH123AE_file.fastq.gz"
VALID_PATH = "my/file/QAHJH006A4_file.fastq.gz"
PATH_WITH_MULT_BARCODES = "my/file/QAHJH006A4_QDERS021AS_file.fastq.gz"

class ArchiveTests(unittest.TestCase):
    """Test suite for util methods check"""

    def test_barcode_integrity(self):
        self.assertTrue(utils.is_valid_barcode(VALID_BARCODE))
        self.assertFalse(utils.is_valid_barcode(INVALID_BARCODE))

    @raises(ValueError)
    def test_invalid_path_for_barcode(self):
        utils.getbarcode(INVALID_PATH)

    @raises(ValueError)
    def test_path_with_multiple_barcodes(self):
        utils.getbarcode(PATH_WITH_MULT_BARCODES)

    def test_valid_path_for_barcode(self):
        barcode = utils.getbarcode(VALID_PATH)
        self.assertEqual(barcode, VALID_BARCODE)