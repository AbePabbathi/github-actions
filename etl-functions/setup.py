import setuptools
from setuptools import find_packages


setuptools.setup(
    name='etl-functions',
    version='0.0.1',
    author='Abe Pabbathi',
    author_email='abraham.pabbathi@databricks.com',
    description='common etl functions',
    long_description='commonly used etl tasks',
    long_description_content_type='text/markdown',
    url='https://github.com/AbePabbathi/github-actions',
    packages=find_packages(where=".", include=["auditFields"]),
    install_requires=[
     'ipython',
     'pandas'
    ],
    extras_require=dict(tests=["pytest"]),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        ],
    )
