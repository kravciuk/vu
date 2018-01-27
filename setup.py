from setuptools import setup, find_packages
import sys

setup(
    # Basic package information.
    name = 'vu',
    version = '1.0.0',
    packages = find_packages(),
    include_package_data = True,
    install_requires = [],
    url = 'https://github.com/kravciuk/vu',
    keywords = 'vu',
    description = 'utils',
    classifiers = [
        'Development Status :: 1 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet',
        'Programming Language :: Python :: 3',
    ],
)

