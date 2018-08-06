import re
import os

from setuptools import setup


with open(os.path.join(os.path.dirname(__file__), 'requirements.txt')) as f:
    INSTALL_REQUIRES = f.read().splitlines()

TEST_REQUIRES = [
    'mock==2.0.0'
]

with open('betfairlightweight/__init__.py', 'r') as f:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
        f.read(),
        re.MULTILINE
    ).group(1)

setup(
        name='betfairlightweight',
        version=version,
        packages=[
            'betfairlightweight',
            'betfairlightweight.endpoints',
            'betfairlightweight.resources',
            'betfairlightweight.streaming',
        ],
        package_dir={
            'betfairlightweight': 'betfairlightweight'
        },
        install_requires=INSTALL_REQUIRES,
        url='https://github.com/liampauling/betfair',
        license='MIT',
        author='liampauling',
        author_email='',
        description='Lightweight python wrapper for Betfair API-NG',
        classifiers=[
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
        ],
        test_suite='tests'
)
