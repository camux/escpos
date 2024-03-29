#!/usr/bin/env python
import os
import sys
from setuptools import find_packages, setup


base_dir = os.path.dirname(__file__)
src_dir = os.path.join(base_dir, "src")

# When executing the setup.py, we need to be able to import ourselves, this
# means that we need to add the src/ directory to the sys.path.
sys.path.insert(0, src_dir)


def read(fname):
    """read file from same path as setup.py"""
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='escpos',
    version='2.0.3',
    platforms="any",
    author='Oscar Alvarez',
    author_email='oscar.alvarez.montero@gmail.com',
    url="https://github.com/camux/escpos",
    description="Python library to manipulate ESC/POS Printers",
    download_url="https://github.com/camux/escpos",
    package_dir={"": "src"},
    packages=find_packages(where="src", exclude=["tests", "tests.*"]),
    package_data={"escpos": ["capabilities.json", "capabilities_win.json"]},
    entry_points={"console_scripts": ["python-escpos = escpos.cli:main"]},
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Printing',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    license='LGPL',
)
