# coding: utf-8

"""
    DCS (Gitea) API.

    This documentation describes the DCS (Gitea) API.  # noqa: E501

    OpenAPI spec version: 1.16.2+dcs
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from dcs_api_client.configuration import Configuration


class GitEntry(object):
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
        'mode': 'str',
        'path': 'str',
        'sha': 'str',
        'size': 'int',
        'type': 'str',
        'url': 'str'
    }

    attribute_map = {
        'mode': 'mode',
        'path': 'path',
        'sha': 'sha',
        'size': 'size',
        'type': 'type',
        'url': 'url'
    }

    def __init__(self, mode=None, path=None, sha=None, size=None, type=None, url=None, _configuration=None):  # noqa: E501
        """GitEntry - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._mode = None
        self._path = None
        self._sha = None
        self._size = None
        self._type = None
        self._url = None
        self.discriminator = None

        if mode is not None:
            self.mode = mode
        if path is not None:
            self.path = path
        if sha is not None:
            self.sha = sha
        if size is not None:
            self.size = size
        if type is not None:
            self.type = type
        if url is not None:
            self.url = url

    @property
    def mode(self):
        """Gets the mode of this GitEntry.  # noqa: E501


        :return: The mode of this GitEntry.  # noqa: E501
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this GitEntry.


        :param mode: The mode of this GitEntry.  # noqa: E501
        :type: str
        """

        self._mode = mode

    @property
    def path(self):
        """Gets the path of this GitEntry.  # noqa: E501


        :return: The path of this GitEntry.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this GitEntry.


        :param path: The path of this GitEntry.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def sha(self):
        """Gets the sha of this GitEntry.  # noqa: E501


        :return: The sha of this GitEntry.  # noqa: E501
        :rtype: str
        """
        return self._sha

    @sha.setter
    def sha(self, sha):
        """Sets the sha of this GitEntry.


        :param sha: The sha of this GitEntry.  # noqa: E501
        :type: str
        """

        self._sha = sha

    @property
    def size(self):
        """Gets the size of this GitEntry.  # noqa: E501


        :return: The size of this GitEntry.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this GitEntry.


        :param size: The size of this GitEntry.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def type(self):
        """Gets the type of this GitEntry.  # noqa: E501


        :return: The type of this GitEntry.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GitEntry.


        :param type: The type of this GitEntry.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def url(self):
        """Gets the url of this GitEntry.  # noqa: E501


        :return: The url of this GitEntry.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this GitEntry.


        :param url: The url of this GitEntry.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if issubclass(GitEntry, dict):
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
        if not isinstance(other, GitEntry):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GitEntry):
            return True

        return self.to_dict() != other.to_dict()
