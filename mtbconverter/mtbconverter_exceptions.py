"""
Collection of mtbparser exceptions.
"""
class MtbUnknownFileType(Exception):
    """Raise, if the MTB file type could not be determined"""

class MtbIncompleteArchive(Exception):
    """Raise, if the MTB archive is missing files"""
