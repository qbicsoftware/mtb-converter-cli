"""
A converter class, able to verify, extract and submit
important tumor diagnostic information from a ZIP archive
to CentraXX.
"""
import os
import sys
import uuid
from zipfile import ZipFile
from mtbparser.snv_utils import *
from .mtbfiletype import MtbFileType
from .mtbconverter_exceptions import MtbUnknownFileType
from .mtbconverter_exceptions import MtbIncompleteArchive
from .mtbconverter_exceptions import MtbUnknownBarcode
from mtbparser.snv_parser import SnvParser
from mtbparser.snv_utils import SSnvHeader

TEMP_BASE_PATH = "/tmp"

FILETYPE_HEADER = {
    MtbFileType.GERM_SNV: GSnvHeader,
    MtbFileType.SOM_SNV: SSnvHeader,
    MtbFileType.GERM_CNV: CnvHeader,
    MtbFileType.SOM_CNV: CnvHeader,
    MtbFileType.SOM_SV: SsvHeader,
    MtbFileType.META: MetaData
    }


class MtbConverter():

    
    def __init__(self, zip_file, barcode):
        self._zip_file = zip_file
        self._barcode = barcode
        self._filelist = {}
        self._snvlists = {}
        self._tmp_dir = TEMP_BASE_PATH + os.path.sep + "tmp_uktdiagnostics_" + uuid.uuid4().hex
        os.mkdir(self._tmp_dir)
        self._verify()
        self._extract()
        #self._cleanup()

    def _extract(self):
        try:
            self._zip_file.extractall(path=self._tmp_dir)
        except Exception as exc:
            print(exc)
            self._cleanup()
            sys.exit(1)
   
    def convert(self):
        print("Conersion started")
        for variant_file, mtb_filetype in self._filelist.items():
            file_path = self._tmp_dir + os.path.sep + variant_file
            print(file_path)
            print(mtb_filetype)
            print(SnvParser(file_path, FILETYPE_HEADER[mtb_filetype]).getSNVs())

        #for filetype, filename in snvlists: 

    def _verify(self):
        for zipinfo in self._zip_file.infolist():
            filename = zipinfo.filename
            assigned_type = self._getfiletype(filename)
            if self._barcode not in filename:
                raise MtbUnknownBarcode("Could not find barcode {} in file '{}'. All"
                " files need to contain the same "
                "barcode as the zip archive.".format(self._barcode, filename))

            if not assigned_type:
                raise MtbUnknownFileType("Could not determine filetype "
                "according to the naming convention."
                " {} was probably not defined.".format(filename))
            self._filelist[filename] = assigned_type
        
        if len(self._filelist) != len(MtbFileType):
            raise MtbIncompleteArchive("The archive did not contain all necessary files."
            " Only found: {}".format(self._filelist.values()))
        
    def _cleanup(self):
        print(self._tmp_dir)
        os.removedirs(self._tmp_dir)

    def _getfiletype(self, filename):
        for filetype in MtbFileType:
            if filetype.value in filename:
                return filetype
        return ""
