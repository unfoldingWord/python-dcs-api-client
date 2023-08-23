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


class FileLinksResponse(object):
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
        'git': 'str',
        'html': 'str',
        '_self': 'str'
    }

    attribute_map = {
        'git': 'git',
        'html': 'html',
        '_self': 'self'
    }

    def __init__(self, git=None, html=None, _self=None, _configuration=None):  # noqa: E501
        """FileLinksResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._git = None
        self._html = None
        self.__self = None
        self.discriminator = None

        if git is not None:
            self.git = git
        if html is not None:
            self.html = html
        if _self is not None:
            self._self = _self

    @property
    def git(self):
        """Gets the git of this FileLinksResponse.  # noqa: E501


        :return: The git of this FileLinksResponse.  # noqa: E501
        :rtype: str
        """
        return self._git

    @git.setter
    def git(self, git):
        """Sets the git of this FileLinksResponse.


        :param git: The git of this FileLinksResponse.  # noqa: E501
        :type: str
        """

        self._git = git

    @property
    def html(self):
        """Gets the html of this FileLinksResponse.  # noqa: E501


        :return: The html of this FileLinksResponse.  # noqa: E501
        :rtype: str
        """
        return self._html

    @html.setter
    def html(self, html):
        """Sets the html of this FileLinksResponse.


        :param html: The html of this FileLinksResponse.  # noqa: E501
        :type: str
        """

        self._html = html

    @property
    def _self(self):
        """Gets the _self of this FileLinksResponse.  # noqa: E501


        :return: The _self of this FileLinksResponse.  # noqa: E501
        :rtype: str
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """Sets the _self of this FileLinksResponse.


        :param _self: The _self of this FileLinksResponse.  # noqa: E501
        :type: str
        """

        self.__self = _self

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
        if issubclass(FileLinksResponse, dict):
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
        if not isinstance(other, FileLinksResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FileLinksResponse):
            return True

        return self.to_dict() != other.to_dict()
