# coding: utf-8

"""
    DCS (Gitea) API.

    This documentation describes the DCS (Gitea) API.  # noqa: E501

    OpenAPI spec version: 1.16.7+dcs
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from dcs_api_client.configuration import Configuration


class CreateForkOption(object):
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
        'name': 'str',
        'organization': 'str'
    }

    attribute_map = {
        'name': 'name',
        'organization': 'organization'
    }

    def __init__(self, name=None, organization=None, _configuration=None):  # noqa: E501
        """CreateForkOption - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._organization = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if organization is not None:
            self.organization = organization

    @property
    def name(self):
        """Gets the name of this CreateForkOption.  # noqa: E501

        name of the forked repository  # noqa: E501

        :return: The name of this CreateForkOption.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateForkOption.

        name of the forked repository  # noqa: E501

        :param name: The name of this CreateForkOption.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def organization(self):
        """Gets the organization of this CreateForkOption.  # noqa: E501

        organization name, if forking into an organization  # noqa: E501

        :return: The organization of this CreateForkOption.  # noqa: E501
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this CreateForkOption.

        organization name, if forking into an organization  # noqa: E501

        :param organization: The organization of this CreateForkOption.  # noqa: E501
        :type: str
        """

        self._organization = organization

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
        if issubclass(CreateForkOption, dict):
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
        if not isinstance(other, CreateForkOption):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateForkOption):
            return True

        return self.to_dict() != other.to_dict()
