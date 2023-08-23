# coding: utf-8

"""
    DCS (Gitea) API.

    This documentation describes the DCS (Gitea) API.  # noqa: E501

    OpenAPI spec version: 1.20.3+dcs
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "dcs-api-client"
VERSION = "1.20.3"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "certifi>=2017.4.17",
    "python-dateutil>=2.1",
    "six>=1.10",
    "urllib3>=1.23"
]
    

setup(
    name=NAME,
    version=VERSION,
    description="DCS (Gitea) API.",
    author_email="",
    url="https://github.com/unfoldingWord/python-dcs-api-client",
    keywords=["Swagger", "DCS (Gitea) API."],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    This documentation describes the DCS (Gitea) API.  # noqa: E501
    """
)
