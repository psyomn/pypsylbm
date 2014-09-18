from setuptools import setup, find_packages

import pypsylbm

setup(
    name='pypsylbm',
    version=pypsylbm.__version__,
    
    description='Interface to psylbm (light bookmarks)',
    long_description=open('README.rst').read(),
    url='http://www.github.com/psyomn/pypsylbm',
    license='GPLv3',

    author='Simon (psyomn) Symeonidis',
    author_email='lethaljellybean@gmail.com',

    packages=['pypsylbm', 'pypsylbm.cli'],
    zip_safe=False,
    scripts=['pypsylbm/bin/pypsylbm', 'pypsylbm/bin/pypsylbm-gtk']
)
