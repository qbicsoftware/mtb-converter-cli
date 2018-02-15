"""Class that handles the interaction with the CentraXX
REST API and XML import"""

import os
import codecs
import requests
from requests.auth import HTTPBasicAuth

class CXXConnectException(Exception):
    """Exception class for raising CentraXX connection
    related exceptions"""

class CXXConnect():

    def __init__(self, authuser, password, **kwargs):
        self._authuser = authuser
        self._password = password
        self._infopath = kwargs['infopath'] if 'infopath' in kwargs else ""
        self._importqueue = kwargs['importqueue'] if 'importqueue' in kwargs else ""
        self._timeout = int(kwargs['timeout']) if 'timeout' in kwargs else 60
    
    def check(self):
        """Access the info path of CentraXX's API"""
        print('Trying to connect to CentraXX server...')
        print(self._infopath)
        response = requests.get(self._infopath, verify=False, timeout=self._timeout)
        return response
    
    def push(self, xmlfile):
        """Pushes a XML to CentraXX and raises an API Error
        if the import fails"""
        resp = self._tocxx(xmlfile)
        print(resp)
        resp = self._triggerimport(xmlfile)
        print(resp)
    
    def _tocxx(self, xmlfile):
        filename = os.path.basename(xmlfile.strip())
        importUrl = self._importqueue + "/" + filename
        restAuth = HTTPBasicAuth(self._authuser, self._password)
        headers = {'Content-Type': 'application/xml'}
        #files = {'file': io.open(filepath, 'r', encoding='utf8')}
        xmlContent = codecs.open(xmlfile, encoding='utf-8')
        #xmlContent = open(filepath, 'rb')
        response = requests.post(importUrl, data=xmlContent, auth=restAuth, headers=headers, verify=True)
        return response
    
    def _triggerimport(self, xmlfile):
        filename = os.path.basename(xmlfile.strip())
        importUrl = self._importqueue + '/' + filename + '/start'
        restAuth = HTTPBasicAuth(self._authuser, self._password)
        headers = {}
        response = requests.post(importUrl, headers=headers, auth=restAuth, verify=True)
        return response

    
    def _getimports(self):
        filename = os.path.basename(filepath.strip())
        importUrl = authData['serveraddr'] + '/centraxx/rest/import/successful/' + filename
        restAuth = HTTPBasicAuth(authData['authuser'], authData['password'])
        response = requests.get(importUrl, auth=restAuth, verify=False)
        return response
    
    def _cxximport_queue(self):
        pass
    
    def _delete_sucessful_imports(self):
        pass
