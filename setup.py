# -*- coding: utf-8 -*-
import codecs

from setuptools import setup, find_packages

with codecs.open('README.md', encoding='utf-8') as f:
    README = f.read()

setup(
    name='ocrd_typegroups_classifier',
    version='0.0.1',
    description='Typegroups classifier for OCR',
    long_description=README,
    author='Matthias Seuret, Konstantin Baierer',
    author_email='seuretm@users.noreply.github.com',
    url='https://github.com/seuretm/ocrd_typegroups_classifier',
    license='Apache License 2.0',
    packages=find_packages(exclude=('tests', 'docs')),
    include_package_data=True,
    install_requires=[
        'click',
        'ocrd >= 0.11.0',
        'pandas',
        'Pillow >= 5.3.0',
        'scikit-image',
        'torch',
        'torchvision',
    ],
    package_data={
        '': ['*.json', '*.tgc'],
    },
    entry_points={
        'console_scripts': [
            'typegroups-classifier=ocrd_typegroups_classifier.cli.simple:cli',
            'ocrd-typegroups-classifier=ocrd_typegroups_classifier.cli.ocrd_cli:cli',
        ]
    },
)
