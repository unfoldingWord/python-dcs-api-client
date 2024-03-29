# coding: utf-8

"""
    DCS (Gitea) API.

    This documentation describes the DCS (Gitea) API.  # noqa: E501

    OpenAPI spec version: 1.20.3+dcs
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from dcs_api_client.configuration import Configuration


class CatalogSearchResults(object):
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
        'data': 'list[CatalogEntry]',
        'last_updated': 'datetime',
        'ok': 'bool'
    }

    attribute_map = {
        'data': 'data',
        'last_updated': 'last_updated',
        'ok': 'ok'
    }

    def __init__(self, data=None, last_updated=None, ok=None, _configuration=None):  # noqa: E501
        """CatalogSearchResults - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._data = None
        self._last_updated = None
        self._ok = None
        self.discriminator = None

        if data is not None:
            self.data = data
        if last_updated is not None:
            self.last_updated = last_updated
        if ok is not None:
            self.ok = ok

    @property
    def data(self):
        """Gets the data of this CatalogSearchResults.  # noqa: E501


        :return: The data of this CatalogSearchResults.  # noqa: E501
        :rtype: list[CatalogEntry]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this CatalogSearchResults.


        :param data: The data of this CatalogSearchResults.  # noqa: E501
        :type: list[CatalogEntry]
        """

        self._data = data

    @property
    def last_updated(self):
        """Gets the last_updated of this CatalogSearchResults.  # noqa: E501


        :return: The last_updated of this CatalogSearchResults.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this CatalogSearchResults.


        :param last_updated: The last_updated of this CatalogSearchResults.  # noqa: E501
        :type: datetime
        """

        self._last_updated = last_updated

    @property
    def ok(self):
        """Gets the ok of this CatalogSearchResults.  # noqa: E501


        :return: The ok of this CatalogSearchResults.  # noqa: E501
        :rtype: bool
        """
        return self._ok

    @ok.setter
    def ok(self, ok):
        """Sets the ok of this CatalogSearchResults.


        :param ok: The ok of this CatalogSearchResults.  # noqa: E501
        :type: bool
        """

        self._ok = ok

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
        if issubclass(CatalogSearchResults, dict):
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
        if not isinstance(other, CatalogSearchResults):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CatalogSearchResults):
            return True

        return self.to_dict() != other.to_dict()
