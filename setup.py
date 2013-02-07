#!/usr/bin/env python

"""
Distutils setup script for vizoozie module.
"""

from distutils.core import setup
import sys

sys.path.insert(0, 'vizoozie')
import vizoozie

setup(name='vizoozie',
      version=vizoozie.VERSION,
      author='Ivan Provalov',
      author_email='iprovalo@yahoo.com',
      description='Oozie dot generation module.',
      package_dir={'': 'vizoozie'},
      py_modules=['vizoozie'],
      provides=['vizoozie'],
     )
