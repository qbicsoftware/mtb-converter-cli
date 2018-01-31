mtbconverter
=================

A Python command line tool that parses and converts diagnostic variant data for the Molecular Tumor Board at UKT Tübingen.

Commands
---------

If you provide the ``-h`` argument, you get the command overview:

.. code-block:: bash
  
  Mtbconverter version 0.1.0.
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

  Mtbconverter version 0.1.0.
  usage: convert [-h] [-i archive.zip]

  Conversion of variant information into CentraXX schema conform XML.

  optional arguments:
    -h, --help      show this help message and exit
    -i archive.zip  ZIP archive containing the variant information files.

**Archive format specification**
 
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

  
 
 
