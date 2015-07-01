# -*- coding: UTF-8 -*-

from setuptools import setup, find_packages

setup(
    name = "tiva customers",
    version = "0.0.0",
    author = "Ângelo Nuffer",
    author_email = "angelonuffer@gmail.com",
    packages = find_packages(),
    entry_points = """
        [console_scripts]
        tivac = tiva_customers:main
    """,
)
