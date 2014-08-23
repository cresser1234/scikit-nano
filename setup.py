#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Python toolkit for generating and analyzing nanostructure data"""

from __future__ import absolute_import, division, print_function
__docformat__ = 'restructuredtext en'

import os
import sys
import subprocess
from setuptools import find_packages, setup

if sys.version_info[:2] < (2, 7):
    raise RuntimeError("Python version 2.7 required.")

if sys.version_info[0] < 3:
    import __builtin__ as builtins
else:
    import builtins

DISTNAME = 'scikit-nano'
DESCRIPTION = __doc__
LONG_DESCRIPTION = open('README.rst').read()
AUTHOR = 'Andrew Merrill'
AUTHOR_EMAIL = 'androomerrill@gmail.com'
MAINTAINER = AUTHOR
MAINTAINER_EMAIL = AUTHOR_EMAIL
URL = 'http://projects.geekcode.io/scikit-nano/doc'
DOWNLOAD_URL = 'http://github.com/androomerrill/scikit-nano'
KEYWORDS = 'nano nano-structures nanostructures nanotubes graphene LAMMPS XYZ'
LICENSE = 'BSD 2-Clause'
CLASSIFIERS = """\
Development Status :: 4 - Beta
Intended Audience :: Science/Research
Intended Audience :: Developers
License :: OSI Approved :: BSD License
Operating System :: MacOS :: MacOS X
Operating System :: Microsoft :: Windows
Operating System :: POSIX
Operating System :: Unix
Programming Language :: Python
Programming Language :: Python :: 2.7
Topic :: Scientific/Engineering
Topic :: Scientific/Engineering :: Chemistry
Topic :: Scientific/Engineering :: Physics
Topic :: Scientific/Engineering :: Visualization
Topic :: Software Development
Topic :: Software Development :: Libraries :: Python Modules

"""

MAJOR = 0
MINOR = 2
MICRO = 26
ISRELEASED = False
VERSION = '%d.%d.%d' % (MAJOR, MINOR, MICRO)


# Return the GIT version as a string
def git_version():
    def _minimal_ext_cmd(cmd):
        # construct minimal environment
        env = {}
        for k in ['SYSTEMROOT', 'PATH']:
            v = os.environ.get(k)
            if v is not None:
                env[k] = v
        # LANGUAGE is used on win32
        env['LANGUAGE'] = 'C'
        env['LANG'] = 'C'
        env['LC_ALL'] = 'C'
        out = subprocess.Popen(
            cmd, stdout=subprocess.PIPE, env=env).communicate()[0]
        return out

    try:
        out = _minimal_ext_cmd(['git', 'rev-parse', 'HEAD'])
        GIT_REVISION = out.strip().decode('ascii')
    except OSError:
        GIT_REVISION = "Unknown"

    return GIT_REVISION

# BEFORE importing distutils, remove MANIFEST. distutils doesn't properly
# update it when the contents of directories change.
if os.path.exists('MANIFEST'):
    os.remove('MANIFEST')

# This is a bit (!) hackish: we are setting a global variable so that the main
# sknano __init__ can detect if it is being loaded by the setup routine, to
# avoid attempting to load components that aren't built yet.
builtins.__SKNANO_SETUP__ = True


def get_version_info():
    # Adding the git rev number needs to be done inside
    # write_version_py(), otherwise the import of sknano.version messes
    # up the build under Python 3.
    FULLVERSION = VERSION
    if os.path.exists('.git'):
        GIT_REVISION = git_version()
    elif os.path.exists('sknano/version.py'):
        # must be a source distribution, use existing version file
        # load it as a separate module to not load sknano/__init__.py
        import imp
        version = imp.load_source('sknano.version', 'sknano/version.py')
        GIT_REVISION = version.git_revision
    else:
        GIT_REVISION = "Unknown"

    if not ISRELEASED:
        FULLVERSION += '.dev-' + GIT_REVISION[:7]

    return FULLVERSION, GIT_REVISION


def write_version_py(filename='sknano/version.py'):
    cnt = """
# THIS FILE IS GENERATED FROM SCIKIT-NANO SETUP.PY
short_version = '%(version)s'
version = '%(version)s'
full_version = '%(full_version)s'
git_revision = '%(git_revision)s'
release = %(isrelease)s

if not release:
    version = full_version
"""
    FULLVERSION, GIT_REVISION = get_version_info()

    a = open(filename, 'w')
    try:
        a.write(cnt % {'version': VERSION,
                       'full_version': FULLVERSION,
                       'git_revision': GIT_REVISION,
                       'isrelease': str(ISRELEASED)})
    finally:
        a.close()


def configuration(parent_package='', top_path=None):
    from numpy.distutils.misc_util import Configuration
    config = Configuration(None, parent_package, top_path)
    config.set_options(ignore_setup_xxx_py=True,
                       assume_default_configuration=True,
                       delegate_options_to_subpackages=True,
                       quiet=True)

    config.add_subpackage('sknano')
    config.add_data_dir('sknano/data')
    config.get_version('sknano/version.py')

    return config


def setup_package():

    # Rewrite the version file everytime
    write_version_py()

    # Figure out whether to add ``*_requires = ['numpy>=`min version`',
    # 'scipy>=`min version`']``. We don't want to do that unconditionally,
    # because we risk updating an installed numpy/scipy which fails too often.
    # Just if the minimum version is not installed, we may give it a try.
    install_requires = []
    try:
        import numpy
        numpy_version = \
            tuple(map(int, numpy.version.short_version.split('.'))[:2])
        if numpy_version < (1, 8):
            raise RuntimeError
    except (AttributeError, ImportError, RuntimeError):
        install_requires += ['numpy>=1.8']

    try:
        import scipy
        scipy_version = \
            tuple(map(int, scipy.version.short_version.split('.'))[:2])
        if scipy_version < (0, 14):
            raise RuntimeError
    except (AttributeError, ImportError, RuntimeError):
        install_requires += ['scipy>=0.14']

    metadata = dict(
        name=DISTNAME,
        author=AUTHOR,
        author_email=AUTHOR_EMAIL,
        maintainer=MAINTAINER,
        maintainer_email=MAINTAINER_EMAIL,
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        url=URL,
        download_url=DOWNLOAD_URL,
        license=LICENSE,
        keywords=KEYWORDS,
        classifiers=[_f for _f in CLASSIFIERS.split('\n') if _f],
        platforms=["Windows", "Linux", "Solaris", "Mac OS-X", "Unix"],
        test_suite='nose.collector',
        install_requires=install_requires,
        entry_points={
            'console_scripts': ['nanogen = sknano.scripts.nanogen:main',
                                'nanogenui = sknano.scripts.nanogenui:main'],
        },
        packages=find_packages(),
        include_package_data=True,
    )

    if len(sys.argv) >= 2 and ('--help' in sys.argv[1:] or
                               sys.argv[1] in ('--help-commands', 'egg_info',
                                               '--version', 'clean')):

        # For these actions, NumPy/SciPy are not required.
        # They are required to succeed without them when, for example,
        # pip is used to install Scipy when Numpy is not yet present in
        # the system.
        #try:
        #    from setuptools import setup
        #except ImportError:
        #    from distutils.core import setup

        FULLVERSION, GIT_REVISION = get_version_info()
        metadata['version'] = FULLVERSION
    else:
        FULLVERSION, GIT_REVISION = get_version_info()
        metadata['version'] = FULLVERSION
        #import setuptools
        #from numpy.distutils.core import setup

        #metadata['configuration'] = configuration

    setup(**metadata)

if __name__ == '__main__':
    setup_package()
