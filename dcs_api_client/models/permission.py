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


class Permission(object):
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
        'admin': 'bool',
        'pull': 'bool',
        'push': 'bool'
    }

    attribute_map = {
        'admin': 'admin',
        'pull': 'pull',
        'push': 'push'
    }

    def __init__(self, admin=None, pull=None, push=None, _configuration=None):  # noqa: E501
        """Permission - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._admin = None
        self._pull = None
        self._push = None
        self.discriminator = None

        if admin is not None:
            self.admin = admin
        if pull is not None:
            self.pull = pull
        if push is not None:
            self.push = push

    @property
    def admin(self):
        """Gets the admin of this Permission.  # noqa: E501


        :return: The admin of this Permission.  # noqa: E501
        :rtype: bool
        """
        return self._admin

    @admin.setter
    def admin(self, admin):
        """Sets the admin of this Permission.


        :param admin: The admin of this Permission.  # noqa: E501
        :type: bool
        """

        self._admin = admin

    @property
    def pull(self):
        """Gets the pull of this Permission.  # noqa: E501


        :return: The pull of this Permission.  # noqa: E501
        :rtype: bool
        """
        return self._pull

    @pull.setter
    def pull(self, pull):
        """Sets the pull of this Permission.


        :param pull: The pull of this Permission.  # noqa: E501
        :type: bool
        """

        self._pull = pull

    @property
    def push(self):
        """Gets the push of this Permission.  # noqa: E501


        :return: The push of this Permission.  # noqa: E501
        :rtype: bool
        """
        return self._push

    @push.setter
    def push(self, push):
        """Sets the push of this Permission.


        :param push: The push of this Permission.  # noqa: E501
        :type: bool
        """

        self._push = push

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
        if issubclass(Permission, dict):
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
        if not isinstance(other, Permission):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Permission):
            return True

        return self.to_dict() != other.to_dict()
