"""
A converter class, able to verify, extract and submit
important tumor diagnostic information from a ZIP archive
to CentraXX.
"""
from zipfile import ZipFile
from mtbparser.snv_utils import *
from .mtbfiletype import MtbFileType
from .mtbconverter_exceptions import MtbUnknownFileType

class MtbConverter():

    FILETYPE_HEADER = {
        MtbFileType.GERM_SNV: GSnvHeader,
        MtbFileType.SOM_SNV: SSnvHeader,
        MtbFileType.GERM_CNV: CnvHeader,
        MtbFileType.SOM_CNV: CnvHeader,
        MtbFileType.SOM_SV: SsvHeader,
        MtbFileType.META: MetaData
    }

    def __init__(self, zip_file):
        self._zip_file = zip_file
        self._snvlists = {}
        self._verify()
    
    def _verify(self):
        for filename in self._zip_file.infolist():
            assigned_type = self._getfiletype(filename)
            if not assigned_type:
                raise MtbUnknownFileType("Could not determine filetype "
                "according to the naming convention."
                " {} was probably not defined.".format(filename))
            
        
    def _getfiletype(self, filename):
        for filetype in MtbFileType:
            if filetype.value in filename:
                return filetype
        return ""
