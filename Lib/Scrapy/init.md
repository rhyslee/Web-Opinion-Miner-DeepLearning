Installation guide
Installing Scrapy
Scrapy runs on Python 2.7 and Python 3.4 or above under CPython (default Python implementation) and PyPy (starting with PyPy 5.9).

If you’re using Anaconda or Miniconda, you can install the package from the conda-forge channel, which has up-to-date packages for Linux, Windows and OS X.

To install Scrapy using conda, run:
```
conda install -c conda-forge scrapy
```
Alternatively, if you’re already familiar with installation of Python packages, you can install Scrapy and its dependencies from PyPI with:
```
pip install Scrapy
```
Note that sometimes this may require solving compilation issues for some Scrapy dependencies depending on your operating system, so be sure to check the Platform specific installation notes.

We strongly recommend that you install Scrapy in a dedicated virtualenv, to avoid conflicting with your system packages.

For more detailed and platform specifics instructions, read on.