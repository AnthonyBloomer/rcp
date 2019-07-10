# -*- coding: utf-8 -*-

import os
import sys
from shutil import rmtree

from setuptools import setup, Command

with open("README.rst", "rb") as f:
    long_descr = f.read().decode("utf-8")
    
class PublishCommand(Command):
    """Support setup.py publish."""

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds…')
            rmtree(os.path.join(here, 'dist'))
        except:
            pass

        self.status('Building Source and Wheel (universal) distribution…')
        os.system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))

        self.status('Uploading the package to PyPi via Twine…')
        os.system('twine upload dist/*')

        sys.exit()

setup(
    name="realclearpolitics",
    packages=["rcp"],
    entry_points={
        "console_scripts": ['rcp = rcp.rcp:main']
    },
    version='1.0.0',
    description="Simple script to scrape polling data from RealClearPolitics and output as .csv",
    long_description=long_descr,
    keywords=['politics', 'polls', 'realclearpolitics', 'web scraping'],
    author="Anthony Bloomer",
    author_email="ant0@protonmail.ch",
    url="https://github.com/AnthonyBloomer/rcp",
    install_requires=[
        'beautifulsoup4',
        'requests'
    ],
    classifiers=[
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2.7'
    ],
    cmdclass={
        'publish': PublishCommand,
    },
)
