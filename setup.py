#!/usr/bin/env python

import sys

from setuptools import setup, find_packages


if sys.version_info.major == 3 and sys.version_info.minor < 3:
    print('Unfortunately, your python version is not supported!\n Please upgrade at least to python 3.3!')
    sys.exit(1)

# read the contents of your README file
from pathlib import Path
pwd = Path(__file__).parent
long_description = (pwd / "README.md").read_text()

install_requires = [
    'requests==2.29.0'
]

setup(
    name='scarlet-shark-client',
    version='1.0.5',
    description='Scarlet Shark REST API Python client',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='U+039b',
    author_email='esther@pts-project.org',
    url='https://github.com/PiRogueToolSuite/scarlet-shark-python',
    packages=find_packages(exclude=['*.tests', '*.tests.*', 'test*', 'tests']),
    install_requires=install_requires,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Natural Language :: English',
        'Topic :: Security',
        'Topic :: Utilities',
    ]
)
