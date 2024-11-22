# setup.py

from setuptools import setup, find_packages

setup(
    name='my_elasticsearch_fdw',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'multicorn',
        'elasticsearch',
    ],
    entry_points={
        'multicorn.foreign_data_wrapper': [
            'elasticsearch_fdw = my_elasticsearch_fdw.elasticsearch_fdw:ElasticsearchFDW',
        ]
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A PostgreSQL FDW for Elasticsearch using Multicorn',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
