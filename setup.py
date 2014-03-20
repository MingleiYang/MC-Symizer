import os
import sys

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()

requires = []
test_requires = requires


setup(name='MC-Symizer',
      description='MC-Symizer',
      long_description=README,
      classifiers=[
        "Programming Language :: Python"
        ],
      author='Stephen Leong Koan',
      author_email='stephen.leong.koan@umontreal.ca',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='MC-Symizer',
      install_requires = requires,
      tests_require=test_requires
      )