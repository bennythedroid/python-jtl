#!/usr/bin/env python

from distutils.core import setup
import os

def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()

setup(name='python-jtl',
      version='0.1.0',
      description='Python module for parsing JMeter test results',
      long_description=read('README.txt'),
      keywords='jmeter jtl',
      author='Victor Klepikovskiy',
      author_email='vklepikovskiy@gmail.com',
      url='http://code.google.com/p/python-jtl/',
      license='GPLv3',
      packages=['tests'],
      py_modules=['jtl'],
      classifiers=[
          'Topic :: Internet :: Log Analysis',
          'Topic :: Software Development :: Testing',
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
      ],
     )
