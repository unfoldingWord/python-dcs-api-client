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


class CreateWikiPageOptions(object):
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
        'content_base64': 'str',
        'message': 'str',
        'title': 'str'
    }

    attribute_map = {
        'content_base64': 'content_base64',
        'message': 'message',
        'title': 'title'
    }

    def __init__(self, content_base64=None, message=None, title=None, _configuration=None):  # noqa: E501
        """CreateWikiPageOptions - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._content_base64 = None
        self._message = None
        self._title = None
        self.discriminator = None

        if content_base64 is not None:
            self.content_base64 = content_base64
        if message is not None:
            self.message = message
        if title is not None:
            self.title = title

    @property
    def content_base64(self):
        """Gets the content_base64 of this CreateWikiPageOptions.  # noqa: E501

        content must be base64 encoded  # noqa: E501

        :return: The content_base64 of this CreateWikiPageOptions.  # noqa: E501
        :rtype: str
        """
        return self._content_base64

    @content_base64.setter
    def content_base64(self, content_base64):
        """Sets the content_base64 of this CreateWikiPageOptions.

        content must be base64 encoded  # noqa: E501

        :param content_base64: The content_base64 of this CreateWikiPageOptions.  # noqa: E501
        :type: str
        """

        self._content_base64 = content_base64

    @property
    def message(self):
        """Gets the message of this CreateWikiPageOptions.  # noqa: E501

        optional commit message summarizing the change  # noqa: E501

        :return: The message of this CreateWikiPageOptions.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this CreateWikiPageOptions.

        optional commit message summarizing the change  # noqa: E501

        :param message: The message of this CreateWikiPageOptions.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def title(self):
        """Gets the title of this CreateWikiPageOptions.  # noqa: E501

        page title. leave empty to keep unchanged  # noqa: E501

        :return: The title of this CreateWikiPageOptions.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this CreateWikiPageOptions.

        page title. leave empty to keep unchanged  # noqa: E501

        :param title: The title of this CreateWikiPageOptions.  # noqa: E501
        :type: str
        """

        self._title = title

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
        if issubclass(CreateWikiPageOptions, dict):
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
        if not isinstance(other, CreateWikiPageOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateWikiPageOptions):
            return True

        return self.to_dict() != other.to_dict()
