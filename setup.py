#!/usr/bin/env python
# coding=utf-8


from setuptools import setup, find_packages


setup(
    name="tgcode",
    version="0.3.2",
    author="jkmiao",
    author_email="miaoweihong@tungee.com",
    description= "verify code of most types",
    url = "http://gitlab.tangees.com/miaoweihong/tgcode",
    package_data = {
        '': ['*.txt', '*.model']
    },
    lisense = 'MIT',
    install_requires=[
        "sklearn",
        "numpy",
        "scipy",
        "pillow",
        "tornado",
        "pillow",
        "keras",
        "h5py",
        "tensorflow"
        ],
    packages=find_packages(),
)
