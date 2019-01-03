# -*- coding: utf-8 -*-
import codecs
import os
import re
from setuptools import setup


with open('README.md') as f:
	long_description = f.read()


setup(name='cn2num',
		description='A Simple package transform Chinese numerals into Arabic numerals',
		long_description=long_description,
		long_description_content_type='text/markdown',
		version='0.1.1',
		author='anhenghuang',
		author_email='contact@huanganheng.com',
		url='http://github.com/anhenghuang/cn2num',
		license='MIT',
		packages=['cn2num'],
		zip_safe=False,
		classifiers=(
			"Programming Language :: Python :: 3",
			"License :: OSI Approved :: MIT License",
			"Operating System :: OS Independent",
		),
)
