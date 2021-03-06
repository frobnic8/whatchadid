#!/usr/bin/env python

from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup

setup(name='whatchadid',
      version='0.5.1',
      description='Perform the CSV export for WhatchaDoing but actually work',
      author='Erskin Cherry',
      author_email='erskin@eldritch.org',
      url='https://github.com/frobnic8/whatchadid',
      download_url='https://github.com/frobnic8/whatchadid/tree/master/dist',
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
