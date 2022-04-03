.. image:: https://readthedocs.org/projects/patricesorter/badge/?version=latest
   :target: https://patricesorter.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status
.. image:: https://github.com/PatriceJada/patricesorter/actions/workflows/python-package.yml/badge.svg?branch=master
   :alt: Python Workflow
   :target: https://github.com/PatriceJada/patricesorter/actions/workflows/python-package.yml


=============
patricesorter
=============


Patricesorter is a sample Python packaging structure.

Installation
============

pip install -e .

or

pip install patricesorter


Usage
=====

::

   PS C:\Users\PMusoke\Documents\GitHub\myproto\patricesorter> patricesorter -h
   usage: patricesorter [-h] [-v] [-q] [--nargs NARGS [NARGS ...]] {} ...

   positional arguments:
     {}                    sub command help

   optional arguments:
     -h, --help            show this help message and exit
     -v, --version         show program's version number and exit
     -q, --quiet           suppress output
     --nargs NARGS [NARGS ...]


Command Line
============

::

   PS C:\Users\PMusoke\Documents\GitHub\myproto\patricesorter> patricesorter --nargs 60 20 50 1 4
   The ['60', '20', '50', '1', '4'] sorted to  ['1', '20', '4', '50', '60']  , the first price is 1 last price 60

Interface
=========

::

   PS C:\Users\PMusoke\Documents\GitHub\myproto\patricesorter> python
   Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
   Type "help", "copyright", "credits" or "license" for more information.
   >>> import patricesorter as ps
   >>> ps.sort_prices(['60', '20', '50', '1', '4'])
   (['1', '20', '4', '50', '60'], (First 1, Last 60))




.. _pyscaffold-notes:

Note
====

This project has been set up using PyScaffold 4.2.1. For details and usage
information on PyScaffold see https://pyscaffold.org/.
