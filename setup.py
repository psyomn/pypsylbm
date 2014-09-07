from setuptools import setup, find_packages

import pypsylbm

setup(
    name='pypsylbm',
    version=pypsylbm.__version__,
    url='http://www.github.com/psyomn/pypsylbm',
    license='GPLv3',
    author='Simon (psyomn) Symeonidis',
    author_email='lethaljellybean@gmail.com',
    tests_require=['pytest'],
    description='Interface to psylbm (light bookmarks)',
    long_description=open('README.rst').read(),
    packages=['pypsylbm'],
    include_package_data=True,
    platforms='any',
    classifiers = [
            'Programming Language :: Python 3',
            'Development Status :: 1 - Alpha',
            'Natural Language :: English',
            'Environment :: Desktop Application',
            'Intended Audience :: Users',
            'License :: GPLv3', 
            'Operating System :: OS Independent',
            'Topic :: Desktop Applications :: Bookmark Management'
        ],
    zip_safe=False,
    scripts=['bin/pypsylbm.py', 'bin/pypsylbm-gtk.py']
)
