mtbconverter
==============

|travis| |codecov|

A Python command line tool that parses and converts diagnostic variant data for the Molecular Tumor Board at UKT Tübingen.

.. |travis| image:: https://travis-ci.org/qbicsoftware/qbic.mtbconverter.svg?branch=master
    :target: https://travis-ci.org/qbicsoftware/qbic.mtbconverter
.. |codecov| image:: https://codecov.io/gh/qbicsoftware/qbic.mtbconverter/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/qbicsoftware/qbic.mtbconverter

Commands
---------

If you provide the ``-h`` argument, you get the command overview:

.. code-block:: bash
  
  Mtbconverter version 0.1
  Usage: mtbconverter.py [-h] [command]

  command:
          convert         Converts variant information into CentraXX XML.
          push            Pushes one ore more XML files to CentraXX.
          catalogue       Builds CentraXX catalogue XML files.

The mtbconverter currently supports three commands: ``convert, push`` and ``catalogue``.

convert
~~~~~~~
The ``convert`` command tells the mtbconverter to parse the necessary MTB information from a given zip archive. The archive needs to contain several TSV files. which follow the format specification_ and naming convention described in the ``mtbparser`` module, which is implemented in mtbconverter.

.. _specification: https://github.com/qbicsoftware/qbic.mtbparser/blob/master/README.md

.. code-block:: bash

  Mtbconverter version 0.1
  usage: convert [-h] [-i archive.zip]

  Conversion of variant information into CentraXX schema conform XML.

  optional arguments:
    -h, --help      show this help message and exit
    -i archive.zip  ZIP archive containing the variant information files.

**Archive format specification**
The ZIP archive name needs to carry the QBIC barcode, and the same needs to present in all files within the archive. This is just to make sure, that the files indeed belong to the same sample.

.. code-block:: bash
  
  Archive name:
  <QBIC-barcode>_*.zip
  
  Archive content:
  <QBiC-Barcode>_somatic_snv.tsv
  <QBiC-Barcode>_somatic_cnv.tsv
  <QBiC-Barcode>_germline_snv.tsv
  <QBiC-Barcode>_germline_cnv.tsv
  <QBiC-Barcode>_somatic_sv.tsv
  <QBiC-Barcode>_metadata.tsv

The information is encoded in the six TSV files, following the specification described in detail in the ``mtbparser`` library_.

push
~~~~
*This section needs to be filled with information.*

catalogue
~~~~~~~~~
The ``catalogue`` command creates XML files for CentraXX controlled vocabulary, parameters definition and profiles. This needs to be done only once every time a specification changes, so CentraXX knows how to connect the incoming data, once it gets imported.

After executing ``catalogue``, mtbconverter will create 8 XML files:

1. cv_centraxx.xml: The controlled vobaculary for CentraXX.
2. params_centraxx.xml: The parameters and the expected data type for CentraXX.
3. ssnv_profiles_centraxx.xml: The profile for somatic SNVs.
4. scnv_profiles_centraxx.xml: The profile for somatic CNVs.
5. gsnv_profiles_centraxx.xml: The profile for germline SNVs.
6. gcnv_profiles_centraxx.xml: The profile for germline CNVs.
7. sv_profiles_centraxx.xml: The profile for somatic structural variants.
8. metadata_profiles_centraxx.xml: The profile for metadata, containing the diagnosis.


.. _library: https://github.com/qbicsoftware/qbic.mtbparser/blob/master/README.md
  
