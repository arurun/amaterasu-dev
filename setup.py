import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "amaterasu_kai",
    version = "0.2",
    author = "Erik Walinda",
    author_email = "walinda.erik.6e@kyoto-u.ac.jp",
    description = (""),
    license = "BSD",
    keywords = "NMR relaxation dispersion analysis",
    url = "",
    packages=['amaterasux'],
    long_description=read('README.txt'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
