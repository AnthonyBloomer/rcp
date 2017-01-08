# -*- coding: utf-8 -*-

from setuptools import setup

with open("README.md", "rb") as f:
    long_descr = f.read().decode("utf-8")

setup(
    name="realclearpolitics",
    packages=["rcp"],
    entry_points={
        "console_scripts": ['rcp = rcp.rcp:main']
    },
    version='0.0.2',
    description="Simple script to scrape polling data from RealClearPolitics and output as .csv",
    long_description=long_descr,
    author="Anthony Bloomer",
    author_email="ant0@protonmail.ch",
    url="https://github.com/AnthonyBloomer/rcp",
    install_requires=[
        'beautifulsoup4',
        'requests'
    ],
)