# coding: utf-8

"""
    DCS (Gitea) API.

    This documentation describes the DCS (Gitea) API.  # noqa: E501

    OpenAPI spec version: 1.16.3+dcs
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from dcs_api_client.configuration import Configuration


class RepoTransfer(object):
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
        'doer': 'User',
        'recipient': 'User',
        'teams': 'list[Team]'
    }

    attribute_map = {
        'doer': 'doer',
        'recipient': 'recipient',
        'teams': 'teams'
    }

    def __init__(self, doer=None, recipient=None, teams=None, _configuration=None):  # noqa: E501
        """RepoTransfer - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._doer = None
        self._recipient = None
        self._teams = None
        self.discriminator = None

        if doer is not None:
            self.doer = doer
        if recipient is not None:
            self.recipient = recipient
        if teams is not None:
            self.teams = teams

    @property
    def doer(self):
        """Gets the doer of this RepoTransfer.  # noqa: E501


        :return: The doer of this RepoTransfer.  # noqa: E501
        :rtype: User
        """
        return self._doer

    @doer.setter
    def doer(self, doer):
        """Sets the doer of this RepoTransfer.


        :param doer: The doer of this RepoTransfer.  # noqa: E501
        :type: User
        """

        self._doer = doer

    @property
    def recipient(self):
        """Gets the recipient of this RepoTransfer.  # noqa: E501


        :return: The recipient of this RepoTransfer.  # noqa: E501
        :rtype: User
        """
        return self._recipient

    @recipient.setter
    def recipient(self, recipient):
        """Sets the recipient of this RepoTransfer.


        :param recipient: The recipient of this RepoTransfer.  # noqa: E501
        :type: User
        """

        self._recipient = recipient

    @property
    def teams(self):
        """Gets the teams of this RepoTransfer.  # noqa: E501


        :return: The teams of this RepoTransfer.  # noqa: E501
        :rtype: list[Team]
        """
        return self._teams

    @teams.setter
    def teams(self, teams):
        """Sets the teams of this RepoTransfer.


        :param teams: The teams of this RepoTransfer.  # noqa: E501
        :type: list[Team]
        """

        self._teams = teams

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
        if issubclass(RepoTransfer, dict):
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
        if not isinstance(other, RepoTransfer):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RepoTransfer):
            return True

        return self.to_dict() != other.to_dict()
