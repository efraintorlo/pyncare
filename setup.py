""" setup.py - Script to install package using distutils

For help options run:
$ python setup.py help

"""
# Author: Efrain Torres


from setuptools import setup
import pyncare

#  ##############
VERSION = pyncare.__version__
NAME = pyncare.__name__
AUTHOR = pyncare.__author__


setup_args = dict(name=NAME,
                  version=VERSION,
                  author=AUTHOR,
                  author_email='efraazul@gmail.com',
                  url='https://bitbucket.org/elchinot7/pyncare',
                  packages=['pyncare'],
                  # scripts=[],
                  package_data={},
                  license="Modified BSD license",
                  description="""A generic Solver and Ploter for Dynamical\
                  Systems Projected over the Poincare sphere.""",
                  long_description=open('Readme.rst').read(),
                  classifiers=["Topic :: Utilities",
                               "Intended Audience :: Science/Research",
                               "License :: OSI Approved :: BSD License",
                               "Operating System :: OS Independent",
                               "Programming Language :: Python",
                               "Programming Language :: Python :: 2.7",
                               ],
                  install_requires=[],
                  )

if __name__ == "__main__":
    setup(**setup_args)
