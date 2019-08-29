# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in t_report/__init__.py
from t_report import __version__ as version

setup(
	name='t_report',
	version=version,
	description='for report',
	author='sammish',
	author_email='sammish.thundiyil@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
