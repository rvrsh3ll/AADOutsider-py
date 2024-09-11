from os import path
from setuptools import setup

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    requirements = [line.strip() for line in f.readlines()]

with open(path.join(here, 'version.txt'), encoding='utf-8') as f:
    version = f.read().strip()

setup(
    name='aadoutsider',
    version='1.0',
    description='AADOutsider-py',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/synacktiv/AADOutsider-py',
    author='Synacktiv',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Information Technology',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='aadoutsider-py aadoutsider aadinternals azure',
    python_requires='>=3.5, <4',
    install_requires=requirements,
    entry_points={
        'console_scripts': ['aadoutsider = aadoutsider:main'],
    },
    project_urls={
        'Apply!': 'https://www.synacktiv.com',
        'Source': 'https://github.com/synacktiv/AADOutsider-py',
    },
)
