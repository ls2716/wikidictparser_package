# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='wikidictparser',
    version='0.1.0',
    # description='Sample package for Python-Guide.org',
    long_description=readme,
    author='Lukasz Sliwinski',
    author_email='luki3141@gmail.com',
    url='https://github.com/ls2716/wikidictparser_package',
    license=license,
    install_requires=[
          'requests',
          'bs4',
          'pandas',
          'lxml',
      ],
    packages=find_packages(exclude=('tests', 'docs'))
)

