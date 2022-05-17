# coding: utf-8

"""
    DCS (Gitea) API.

    This documentation describes the DCS (Gitea) API.  # noqa: E501

    OpenAPI spec version: 1.16.8+dcs
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from dcs_api_client.configuration import Configuration


class ExternalWiki(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'external_wiki_url': 'str'
    }

    attribute_map = {
        'external_wiki_url': 'external_wiki_url'
    }

    def __init__(self, external_wiki_url=None, _configuration=None):  # noqa: E501
        """ExternalWiki - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._external_wiki_url = None
        self.discriminator = None

        if external_wiki_url is not None:
            self.external_wiki_url = external_wiki_url

    @property
    def external_wiki_url(self):
        """Gets the external_wiki_url of this ExternalWiki.  # noqa: E501

        URL of external wiki.  # noqa: E501

        :return: The external_wiki_url of this ExternalWiki.  # noqa: E501
        :rtype: str
        """
        return self._external_wiki_url

    @external_wiki_url.setter
    def external_wiki_url(self, external_wiki_url):
        """Sets the external_wiki_url of this ExternalWiki.

        URL of external wiki.  # noqa: E501

        :param external_wiki_url: The external_wiki_url of this ExternalWiki.  # noqa: E501
        :type: str
        """

        self._external_wiki_url = external_wiki_url

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ExternalWiki, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ExternalWiki):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ExternalWiki):
            return True

        return self.to_dict() != other.to_dict()
