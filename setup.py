# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


version = __import__('userviews').__version__
with open('README.rst', 'rb') as f:
    long_description = f.read().decode('utf-8')


setup(
    name='django-userviews',
    version=version,
    packages=find_packages(),

    install_requires=[
        'Django',
    ],

    author='Eduardo Augusto Klosowski',
    author_email='eduardo_klosowski@yahoo.com',

    description='Views baseadas em classes do Django para usuários',
    long_description=long_description,
    license='MIT',
    url='https://github.com/eduardoklosowski/django-userviews',

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Portuguese (Brazilian)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
