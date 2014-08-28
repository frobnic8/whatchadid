#!/usr/bin/env python

from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup

setup(name='whatchadid',
      version='0.5.0',
      description='Perform the CSV export for WhatchaDoing but actually work',
      author='Erskin Cherry',
      author_email='erskin.cherry@opower.com',
      url='https://github.va.opower.it/erskin-cherry/whatchadid',
      download_url='https://github.va.opower.it/erskin-cherry/whatchadid/tree/master/dist',
      py_modules=['whatchadid'],
      scripts=['bin/whatchadid'],
      long_description=open('README.md').read(),
      install_requires=[
          'BeautifulSoup4 >= 4.0.0',
      ],
      provides=[
          'whatchadid',
      ],
      )
