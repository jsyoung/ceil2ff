#!/usr/bin/env python

from distutils.core import setup

setup(name='ceil2ff',
      version='3.0',
      description='Ceilometer Data Reader',
      author='Joe Young',
      author_email='joe.young@utah.edu',
      url='http://www.jsyoung.us/code/',
      packages=['ceil2ff','ceil2ff.telnet','ceil2ff.formats'],
     )

