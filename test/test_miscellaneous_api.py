# coding: utf-8

"""
    DCS (Gitea) API.

    This documentation describes the DCS (Gitea) API.  # noqa: E501

    OpenAPI spec version: 1.15.9+dcs
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import dcs_api_client
from dcs_api_client.api.miscellaneous_api import MiscellaneousApi  # noqa: E501
from dcs_api_client.rest import ApiException


class TestMiscellaneousApi(unittest.TestCase):
    """MiscellaneousApi unit test stubs"""

    def setUp(self):
        self.api = dcs_api_client.api.miscellaneous_api.MiscellaneousApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_signing_key(self):
        """Test case for get_signing_key

        Get default signing-key.gpg  # noqa: E501
        """
        pass

    def test_get_version(self):
        """Test case for get_version

        Returns the version of the Gitea application  # noqa: E501
        """
        pass

    def test_render_markdown(self):
        """Test case for render_markdown

        Render a markdown document as HTML  # noqa: E501
        """
        pass

    def test_render_markdown_raw(self):
        """Test case for render_markdown_raw

        Render raw markdown as HTML  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
