# Thanks `https://github.com/pypa/sampleproject`!!

from setuptools import setup, find_packages
from os import path
here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'VERSION'), 'r', encoding='utf-8') as f:
  version = f.read().strip()
with open(path.join(here, 'README.md'), 'r', encoding='utf-8') as f:
  long_description = f.read()

setup(
  name              = 'brutelogger',
  version           = version,
  description       = 'A brutish file logger for when you just need to `tee` your screen.',
  long_description  = long_description,
  long_description_content_type='text/markdown',
  url               = 'https://github.com/giuse/brutelogger',
  author            = 'Giuseppe Cuccu',
  author_email      = 'giuseppe.cuccu@gmail.com',
  license           = 'MIT',
  classifiers       = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3 :: Only',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
  keywords         = 'logging tee',
  packages         = find_packages(exclude=['contrib', 'docs', 'tests']),  # Required
  python_requires  = '>=3.6, <4',
  install_requires = [],
  project_urls={
      'Bug Reports' : 'https://github.com/giuse/brutelogger/issues',
      'Source'      : 'https://github.com/giuse/brutelogger/',
  },
  download_url      = f"https://github.com/giuse/brutelogger/archive/{version}.tar.gz",
)
