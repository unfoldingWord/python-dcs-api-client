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


class CommitMeta(object):
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
        'created': 'datetime',
        'sha': 'str',
        'url': 'str'
    }

    attribute_map = {
        'created': 'created',
        'sha': 'sha',
        'url': 'url'
    }

    def __init__(self, created=None, sha=None, url=None, _configuration=None):  # noqa: E501
        """CommitMeta - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._created = None
        self._sha = None
        self._url = None
        self.discriminator = None

        if created is not None:
            self.created = created
        if sha is not None:
            self.sha = sha
        if url is not None:
            self.url = url

    @property
    def created(self):
        """Gets the created of this CommitMeta.  # noqa: E501


        :return: The created of this CommitMeta.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this CommitMeta.


        :param created: The created of this CommitMeta.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def sha(self):
        """Gets the sha of this CommitMeta.  # noqa: E501


        :return: The sha of this CommitMeta.  # noqa: E501
        :rtype: str
        """
        return self._sha

    @sha.setter
    def sha(self, sha):
        """Sets the sha of this CommitMeta.


        :param sha: The sha of this CommitMeta.  # noqa: E501
        :type: str
        """

        self._sha = sha

    @property
    def url(self):
        """Gets the url of this CommitMeta.  # noqa: E501


        :return: The url of this CommitMeta.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this CommitMeta.


        :param url: The url of this CommitMeta.  # noqa: E501
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
        if issubclass(CommitMeta, dict):
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
        if not isinstance(other, CommitMeta):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CommitMeta):
            return True

        return self.to_dict() != other.to_dict()
