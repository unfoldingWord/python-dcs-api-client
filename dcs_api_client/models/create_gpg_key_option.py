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


class CreateGPGKeyOption(object):
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
        'armored_public_key': 'str',
        'armored_signature': 'str'
    }

    attribute_map = {
        'armored_public_key': 'armored_public_key',
        'armored_signature': 'armored_signature'
    }

    def __init__(self, armored_public_key=None, armored_signature=None, _configuration=None):  # noqa: E501
        """CreateGPGKeyOption - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._armored_public_key = None
        self._armored_signature = None
        self.discriminator = None

        self.armored_public_key = armored_public_key
        if armored_signature is not None:
            self.armored_signature = armored_signature

    @property
    def armored_public_key(self):
        """Gets the armored_public_key of this CreateGPGKeyOption.  # noqa: E501

        An armored GPG key to add  # noqa: E501

        :return: The armored_public_key of this CreateGPGKeyOption.  # noqa: E501
        :rtype: str
        """
        return self._armored_public_key

    @armored_public_key.setter
    def armored_public_key(self, armored_public_key):
        """Sets the armored_public_key of this CreateGPGKeyOption.

        An armored GPG key to add  # noqa: E501

        :param armored_public_key: The armored_public_key of this CreateGPGKeyOption.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and armored_public_key is None:
            raise ValueError("Invalid value for `armored_public_key`, must not be `None`")  # noqa: E501

        self._armored_public_key = armored_public_key

    @property
    def armored_signature(self):
        """Gets the armored_signature of this CreateGPGKeyOption.  # noqa: E501


        :return: The armored_signature of this CreateGPGKeyOption.  # noqa: E501
        :rtype: str
        """
        return self._armored_signature

    @armored_signature.setter
    def armored_signature(self, armored_signature):
        """Sets the armored_signature of this CreateGPGKeyOption.


        :param armored_signature: The armored_signature of this CreateGPGKeyOption.  # noqa: E501
        :type: str
        """

        self._armored_signature = armored_signature

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
        if issubclass(CreateGPGKeyOption, dict):
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
        if not isinstance(other, CreateGPGKeyOption):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateGPGKeyOption):
            return True

        return self.to_dict() != other.to_dict()
