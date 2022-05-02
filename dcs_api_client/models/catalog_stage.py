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


class CatalogStage(object):
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
        'branch_or_tag_name': 'str',
        'contents_url': 'str',
        'git_trees_url': 'str',
        'release_url': 'str',
        'released': 'datetime',
        'tarball_url': 'str',
        'zipball_url': 'str'
    }

    attribute_map = {
        'branch_or_tag_name': 'branch_or_tag_name',
        'contents_url': 'contents_url',
        'git_trees_url': 'git_trees_url',
        'release_url': 'release_url',
        'released': 'released',
        'tarball_url': 'tarball_url',
        'zipball_url': 'zipball_url'
    }

    def __init__(self, branch_or_tag_name=None, contents_url=None, git_trees_url=None, release_url=None, released=None, tarball_url=None, zipball_url=None, _configuration=None):  # noqa: E501
        """CatalogStage - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._branch_or_tag_name = None
        self._contents_url = None
        self._git_trees_url = None
        self._release_url = None
        self._released = None
        self._tarball_url = None
        self._zipball_url = None
        self.discriminator = None

        if branch_or_tag_name is not None:
            self.branch_or_tag_name = branch_or_tag_name
        if contents_url is not None:
            self.contents_url = contents_url
        if git_trees_url is not None:
            self.git_trees_url = git_trees_url
        if release_url is not None:
            self.release_url = release_url
        if released is not None:
            self.released = released
        if tarball_url is not None:
            self.tarball_url = tarball_url
        if zipball_url is not None:
            self.zipball_url = zipball_url

    @property
    def branch_or_tag_name(self):
        """Gets the branch_or_tag_name of this CatalogStage.  # noqa: E501


        :return: The branch_or_tag_name of this CatalogStage.  # noqa: E501
        :rtype: str
        """
        return self._branch_or_tag_name

    @branch_or_tag_name.setter
    def branch_or_tag_name(self, branch_or_tag_name):
        """Sets the branch_or_tag_name of this CatalogStage.


        :param branch_or_tag_name: The branch_or_tag_name of this CatalogStage.  # noqa: E501
        :type: str
        """

        self._branch_or_tag_name = branch_or_tag_name

    @property
    def contents_url(self):
        """Gets the contents_url of this CatalogStage.  # noqa: E501


        :return: The contents_url of this CatalogStage.  # noqa: E501
        :rtype: str
        """
        return self._contents_url

    @contents_url.setter
    def contents_url(self, contents_url):
        """Sets the contents_url of this CatalogStage.


        :param contents_url: The contents_url of this CatalogStage.  # noqa: E501
        :type: str
        """

        self._contents_url = contents_url

    @property
    def git_trees_url(self):
        """Gets the git_trees_url of this CatalogStage.  # noqa: E501


        :return: The git_trees_url of this CatalogStage.  # noqa: E501
        :rtype: str
        """
        return self._git_trees_url

    @git_trees_url.setter
    def git_trees_url(self, git_trees_url):
        """Sets the git_trees_url of this CatalogStage.


        :param git_trees_url: The git_trees_url of this CatalogStage.  # noqa: E501
        :type: str
        """

        self._git_trees_url = git_trees_url

    @property
    def release_url(self):
        """Gets the release_url of this CatalogStage.  # noqa: E501


        :return: The release_url of this CatalogStage.  # noqa: E501
        :rtype: str
        """
        return self._release_url

    @release_url.setter
    def release_url(self, release_url):
        """Sets the release_url of this CatalogStage.


        :param release_url: The release_url of this CatalogStage.  # noqa: E501
        :type: str
        """

        self._release_url = release_url

    @property
    def released(self):
        """Gets the released of this CatalogStage.  # noqa: E501


        :return: The released of this CatalogStage.  # noqa: E501
        :rtype: datetime
        """
        return self._released

    @released.setter
    def released(self, released):
        """Sets the released of this CatalogStage.


        :param released: The released of this CatalogStage.  # noqa: E501
        :type: datetime
        """

        self._released = released

    @property
    def tarball_url(self):
        """Gets the tarball_url of this CatalogStage.  # noqa: E501


        :return: The tarball_url of this CatalogStage.  # noqa: E501
        :rtype: str
        """
        return self._tarball_url

    @tarball_url.setter
    def tarball_url(self, tarball_url):
        """Sets the tarball_url of this CatalogStage.


        :param tarball_url: The tarball_url of this CatalogStage.  # noqa: E501
        :type: str
        """

        self._tarball_url = tarball_url

    @property
    def zipball_url(self):
        """Gets the zipball_url of this CatalogStage.  # noqa: E501


        :return: The zipball_url of this CatalogStage.  # noqa: E501
        :rtype: str
        """
        return self._zipball_url

    @zipball_url.setter
    def zipball_url(self, zipball_url):
        """Sets the zipball_url of this CatalogStage.


        :param zipball_url: The zipball_url of this CatalogStage.  # noqa: E501
        :type: str
        """

        self._zipball_url = zipball_url

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
        if issubclass(CatalogStage, dict):
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
        if not isinstance(other, CatalogStage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CatalogStage):
            return True

        return self.to_dict() != other.to_dict()
