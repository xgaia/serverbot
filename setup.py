from os import listdir
from setuptools import setup, find_packages


setup(
    name='serverbot',
    version='2.0',
    description='Telegram bot to manage a Linux server',
    author='Xavier Garnier',
    author_email='xgaia@gmx.com',
    url='https://github.com/xgaia/serverbot',
    install_requires='pipenv',
    packages=find_packages(),
    scripts=['serverbot'])
