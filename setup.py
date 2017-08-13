# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='crude-user-updater',
    version='1.0.0',
    description='Package to update the program of your users to the latest version using a simple archive and an ignore list.',
    long_description=readme,
    author='Sebastien Mathieu',
    author_email='s.mathieu.1989@gmail.com',
    url='https://github.com/sebMathieu/crude-user-updater',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

