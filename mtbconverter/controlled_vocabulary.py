"""Builder for controlled vocabulary XML as part of the preparation
for the CentraXX import"""

import pyxb.utils.domutils
import xml.dom.minidom
from pyxb.namespace import XMLSchema_instance as xsi
from pyxb.namespace import XMLNamespaces as xmlns
import mtbconverter.cxxpy as cx
from mtbparser.snv_utils import SSnvHeader

CV_VERSION = '0.1'

CV_PREFIX = 'QBIC_'

CV_EFFECT_SSNV = ['activating','inactivating','function_changed','probably_activating',
                    'probably_inactivating','probable_function_change','ambigious','benign','NA']

CV_BASES = ['C','A','T','G']

CV_CHROMOSOMES = [list(range(1,24)) + ['X', 'Y']]

class ControlledVocabulary:
    
    def __init__(self):
        pyxb.utils.domutils.BindingDOMSupport.DeclareNamespace(cx.Namespace, 'cxx')
        self._root = cx.CentraXXDataExchange()
        self._source = 'XML-IMPORT'
        self._prefix = 'QBIC_'
        self._catalogue_data = cx.CatalogueDataType()
        self._cvforssnv()
    
    def _cvforssnv(self):
        """Create the XML entries for the
        somatic SNVs information"""

        # create an index for all human chromosomes      
        index_list = list(range(1,24)) + ['X', 'Y']

        # register the chromosomes (de, en)
        for chr_index in index_list:
            multi_entry_type_de = cx.MultilingualEntryType(Lang='de', Value='Chromosome {}'.format(chr_index))
            multi_entry_type_en = cx.MultilingualEntryType(Lang='en', Value='Chromosome {}'.format(chr_index))
            item = cx.UsageEntryType()
            item.NameMultilingualEntries = [multi_entry_type_de, multi_entry_type_en]
            item.Code = '{}{}'.format(CV_PREFIX, chr_index)
            item.Category = "false"
            self._catalogue_data.append(item)
        
        # create vc for sSNV effects
        for effect in CV_EFFECT_SSNV:
            multi_entry_type_de = cx.MultilingualEntryType(Lang='de', Value='{}'.format(effect))
            multi_entry_type_en = cx.MultilingualEntryType(Lang='en', Value='{}'.format(effect))
            item = cx.UsageEntryType()
            item.NameMultilingualEntries = [multi_entry_type_de, multi_entry_type_en]
            item.Code = '{}{}'.format(CV_PREFIX, effect)
            item.Category = "false"
            self._catalogue_data.append(item)
        
        # create cv for bases
        for base in CV_BASES:
            multi_entry_type_de = cx.MultilingualEntryType(Lang='de', Value='{}'.format(base))
            multi_entry_type_en = cx.MultilingualEntryType(Lang='en', Value='{}'.format(base))
            item = cx.UsageEntryType()
            item.NameMultilingualEntries = [multi_entry_type_de, multi_entry_type_en]
            item.Code = '{}{}'.format(CV_PREFIX, base)
            item.Category = "false"
            self._catalogue_data.append(item)

    
    def getXML(self):
        """Write the XML object into an XML
        file"""
        self._root.Source = self._source
        self._root.CatalogueData = self._catalogue_data
        root_dom = self._root.toDOM()
        root_dom.documentElement.setAttributeNS(
            xsi.uri(), 'xsi:schemaLocation',
            'http://www.kairos-med.de ../CentraXXExchange.xsd')
        root_dom.documentElement.setAttributeNS(
            xmlns.uri(), 'xmlns:xsi', xsi.uri())
        return root_dom.toprettyxml(encoding='utf-8')

