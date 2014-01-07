# -*- coding: utf-8 -*-
"""scikit-nano: python toolkit for generating nano-structures.

A python toolkit for nano-science. Currently, its primary use is for
generating nano-structure data for the following nano-materials:

    * Graphene, both single layer graphene and N-layer graphene.
    * Single-walled nanotubes (SWNTs), both single SWNTs and SWNT bundles.
    * Multi-walled nanotubes (MWNTs), both single MWNTs and MWNT bundles.

It supports saving structure data in the following formats:

    * `xyz`
    * LAMMPS `data`

"""

DOCLINES = __doc__.split("\n")

from setuptools import setup, find_packages
import os
import sys
import subprocess


if sys.version_info[:2] < (2, 7):
    raise RuntimeError("Python version 2.7 required.")

CLASSIFIERS = """\
Development Status :: 4 - Beta
Intended Audience :: Science/Research
License :: OSI Approved :: BSD License
Operating System :: MacOS :: MacOS X
Operating System :: Microsoft :: Windows
Operating System :: POSIX
Operating System :: Unix
Programming Language :: Python
Programming Language :: Python :: 2.7
Topic :: Software Development
Topic :: Scientific/Engineering

"""

MAJOR = 0
MINOR = 2
MICRO = 11
ISRELEASED = False
VERSION = '%d.%d.%d' % (MAJOR, MINOR, MICRO)


def git_version():
    """Return the GIT version as a string."""
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
        out = \
            subprocess.Popen(cmd,
                             stdout=subprocess.PIPE, env=env).communicate()[0]
        return out

    try:
        out = _minimal_ext_cmd(['git', 'rev-parse', 'HEAD'])
        GIT_REVISION = out.strip().decode('ascii')
    except OSError:
        GIT_REVISION = "Unknown"

    return GIT_REVISION


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
# THIS FILE IS GENERATED FROM SKNANO SETUP.PY
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


def setup_package():

    # Rewrite the version file everytime
    write_version_py()

    FULLVERSION, GIT_REVISION = get_version_info()

    setup_options = dict(
        name='sknano',
        version=FULLVERSION,
        author='Andrew Merrill',
        author_email='androomerrill@gmail.com',
        description=DOCLINES[0],
        long_description="\n".join(DOCLINES[2:]),
        url='https://github.com/androomerrill/scikit-nano',
        license='BSD 2-Clause',
        classifiers=[_f for _f in CLASSIFIERS.split('\n') if _f],
        platforms=["Windows", "Linux", "OS-X", "Unix"],
        test_suite='nose.collector',
        packages=find_packages(exclude=['doc', 'ez_setup',
                                        'examples', 'tests']),
        #package_data={'sknano': []},
        #package_dir = {'': 'sknano'},
        include_package_data=True,
        exclude_package_data={'':
            ['README', 'README.rst', '*.gif', '*.html', '*.ui']},
        zip_safe=False,
        install_requires=['numpy>=1.8', 'scipy>=0.13',
                          'pkshared>=0.1.8', 'pksci>=0.1.5'],
        entry_points={
            'sphinx_themes': [
                'path = sknano:get_path',
            ],
            'console_scripts': [
                'nanogen = sknano.scripts.nanogen:main',
            ]
        }
    )

    setup(**setup_options)

if __name__ == '__main__':
    setup_package()
