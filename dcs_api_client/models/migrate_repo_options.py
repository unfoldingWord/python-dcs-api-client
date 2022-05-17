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


class MigrateRepoOptions(object):
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
        'auth_password': 'str',
        'auth_token': 'str',
        'auth_username': 'str',
        'clone_addr': 'str',
        'description': 'str',
        'issues': 'bool',
        'labels': 'bool',
        'lfs': 'bool',
        'lfs_endpoint': 'str',
        'milestones': 'bool',
        'mirror': 'bool',
        'mirror_interval': 'str',
        'private': 'bool',
        'pull_requests': 'bool',
        'releases': 'bool',
        'repo_name': 'str',
        'repo_owner': 'str',
        'service': 'str',
        'uid': 'int',
        'wiki': 'bool'
    }

    attribute_map = {
        'auth_password': 'auth_password',
        'auth_token': 'auth_token',
        'auth_username': 'auth_username',
        'clone_addr': 'clone_addr',
        'description': 'description',
        'issues': 'issues',
        'labels': 'labels',
        'lfs': 'lfs',
        'lfs_endpoint': 'lfs_endpoint',
        'milestones': 'milestones',
        'mirror': 'mirror',
        'mirror_interval': 'mirror_interval',
        'private': 'private',
        'pull_requests': 'pull_requests',
        'releases': 'releases',
        'repo_name': 'repo_name',
        'repo_owner': 'repo_owner',
        'service': 'service',
        'uid': 'uid',
        'wiki': 'wiki'
    }

    def __init__(self, auth_password=None, auth_token=None, auth_username=None, clone_addr=None, description=None, issues=None, labels=None, lfs=None, lfs_endpoint=None, milestones=None, mirror=None, mirror_interval=None, private=None, pull_requests=None, releases=None, repo_name=None, repo_owner=None, service=None, uid=None, wiki=None, _configuration=None):  # noqa: E501
        """MigrateRepoOptions - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._auth_password = None
        self._auth_token = None
        self._auth_username = None
        self._clone_addr = None
        self._description = None
        self._issues = None
        self._labels = None
        self._lfs = None
        self._lfs_endpoint = None
        self._milestones = None
        self._mirror = None
        self._mirror_interval = None
        self._private = None
        self._pull_requests = None
        self._releases = None
        self._repo_name = None
        self._repo_owner = None
        self._service = None
        self._uid = None
        self._wiki = None
        self.discriminator = None

        if auth_password is not None:
            self.auth_password = auth_password
        if auth_token is not None:
            self.auth_token = auth_token
        if auth_username is not None:
            self.auth_username = auth_username
        self.clone_addr = clone_addr
        if description is not None:
            self.description = description
        if issues is not None:
            self.issues = issues
        if labels is not None:
            self.labels = labels
        if lfs is not None:
            self.lfs = lfs
        if lfs_endpoint is not None:
            self.lfs_endpoint = lfs_endpoint
        if milestones is not None:
            self.milestones = milestones
        if mirror is not None:
            self.mirror = mirror
        if mirror_interval is not None:
            self.mirror_interval = mirror_interval
        if private is not None:
            self.private = private
        if pull_requests is not None:
            self.pull_requests = pull_requests
        if releases is not None:
            self.releases = releases
        self.repo_name = repo_name
        if repo_owner is not None:
            self.repo_owner = repo_owner
        if service is not None:
            self.service = service
        if uid is not None:
            self.uid = uid
        if wiki is not None:
            self.wiki = wiki

    @property
    def auth_password(self):
        """Gets the auth_password of this MigrateRepoOptions.  # noqa: E501


        :return: The auth_password of this MigrateRepoOptions.  # noqa: E501
        :rtype: str
        """
        return self._auth_password

    @auth_password.setter
    def auth_password(self, auth_password):
        """Sets the auth_password of this MigrateRepoOptions.


        :param auth_password: The auth_password of this MigrateRepoOptions.  # noqa: E501
        :type: str
        """

        self._auth_password = auth_password

    @property
    def auth_token(self):
        """Gets the auth_token of this MigrateRepoOptions.  # noqa: E501


        :return: The auth_token of this MigrateRepoOptions.  # noqa: E501
        :rtype: str
        """
        return self._auth_token

    @auth_token.setter
    def auth_token(self, auth_token):
        """Sets the auth_token of this MigrateRepoOptions.


        :param auth_token: The auth_token of this MigrateRepoOptions.  # noqa: E501
        :type: str
        """

        self._auth_token = auth_token

    @property
    def auth_username(self):
        """Gets the auth_username of this MigrateRepoOptions.  # noqa: E501


        :return: The auth_username of this MigrateRepoOptions.  # noqa: E501
        :rtype: str
        """
        return self._auth_username

    @auth_username.setter
    def auth_username(self, auth_username):
        """Sets the auth_username of this MigrateRepoOptions.


        :param auth_username: The auth_username of this MigrateRepoOptions.  # noqa: E501
        :type: str
        """

        self._auth_username = auth_username

    @property
    def clone_addr(self):
        """Gets the clone_addr of this MigrateRepoOptions.  # noqa: E501


        :return: The clone_addr of this MigrateRepoOptions.  # noqa: E501
        :rtype: str
        """
        return self._clone_addr

    @clone_addr.setter
    def clone_addr(self, clone_addr):
        """Sets the clone_addr of this MigrateRepoOptions.


        :param clone_addr: The clone_addr of this MigrateRepoOptions.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and clone_addr is None:
            raise ValueError("Invalid value for `clone_addr`, must not be `None`")  # noqa: E501

        self._clone_addr = clone_addr

    @property
    def description(self):
        """Gets the description of this MigrateRepoOptions.  # noqa: E501


        :return: The description of this MigrateRepoOptions.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this MigrateRepoOptions.


        :param description: The description of this MigrateRepoOptions.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def issues(self):
        """Gets the issues of this MigrateRepoOptions.  # noqa: E501


        :return: The issues of this MigrateRepoOptions.  # noqa: E501
        :rtype: bool
        """
        return self._issues

    @issues.setter
    def issues(self, issues):
        """Sets the issues of this MigrateRepoOptions.


        :param issues: The issues of this MigrateRepoOptions.  # noqa: E501
        :type: bool
        """

        self._issues = issues

    @property
    def labels(self):
        """Gets the labels of this MigrateRepoOptions.  # noqa: E501


        :return: The labels of this MigrateRepoOptions.  # noqa: E501
        :rtype: bool
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this MigrateRepoOptions.


        :param labels: The labels of this MigrateRepoOptions.  # noqa: E501
        :type: bool
        """

        self._labels = labels

    @property
    def lfs(self):
        """Gets the lfs of this MigrateRepoOptions.  # noqa: E501


        :return: The lfs of this MigrateRepoOptions.  # noqa: E501
        :rtype: bool
        """
        return self._lfs

    @lfs.setter
    def lfs(self, lfs):
        """Sets the lfs of this MigrateRepoOptions.


        :param lfs: The lfs of this MigrateRepoOptions.  # noqa: E501
        :type: bool
        """

        self._lfs = lfs

    @property
    def lfs_endpoint(self):
        """Gets the lfs_endpoint of this MigrateRepoOptions.  # noqa: E501


        :return: The lfs_endpoint of this MigrateRepoOptions.  # noqa: E501
        :rtype: str
        """
        return self._lfs_endpoint

    @lfs_endpoint.setter
    def lfs_endpoint(self, lfs_endpoint):
        """Sets the lfs_endpoint of this MigrateRepoOptions.


        :param lfs_endpoint: The lfs_endpoint of this MigrateRepoOptions.  # noqa: E501
        :type: str
        """

        self._lfs_endpoint = lfs_endpoint

    @property
    def milestones(self):
        """Gets the milestones of this MigrateRepoOptions.  # noqa: E501


        :return: The milestones of this MigrateRepoOptions.  # noqa: E501
        :rtype: bool
        """
        return self._milestones

    @milestones.setter
    def milestones(self, milestones):
        """Sets the milestones of this MigrateRepoOptions.


        :param milestones: The milestones of this MigrateRepoOptions.  # noqa: E501
        :type: bool
        """

        self._milestones = milestones

    @property
    def mirror(self):
        """Gets the mirror of this MigrateRepoOptions.  # noqa: E501


        :return: The mirror of this MigrateRepoOptions.  # noqa: E501
        :rtype: bool
        """
        return self._mirror

    @mirror.setter
    def mirror(self, mirror):
        """Sets the mirror of this MigrateRepoOptions.


        :param mirror: The mirror of this MigrateRepoOptions.  # noqa: E501
        :type: bool
        """

        self._mirror = mirror

    @property
    def mirror_interval(self):
        """Gets the mirror_interval of this MigrateRepoOptions.  # noqa: E501


        :return: The mirror_interval of this MigrateRepoOptions.  # noqa: E501
        :rtype: str
        """
        return self._mirror_interval

    @mirror_interval.setter
    def mirror_interval(self, mirror_interval):
        """Sets the mirror_interval of this MigrateRepoOptions.


        :param mirror_interval: The mirror_interval of this MigrateRepoOptions.  # noqa: E501
        :type: str
        """

        self._mirror_interval = mirror_interval

    @property
    def private(self):
        """Gets the private of this MigrateRepoOptions.  # noqa: E501


        :return: The private of this MigrateRepoOptions.  # noqa: E501
        :rtype: bool
        """
        return self._private

    @private.setter
    def private(self, private):
        """Sets the private of this MigrateRepoOptions.


        :param private: The private of this MigrateRepoOptions.  # noqa: E501
        :type: bool
        """

        self._private = private

    @property
    def pull_requests(self):
        """Gets the pull_requests of this MigrateRepoOptions.  # noqa: E501


        :return: The pull_requests of this MigrateRepoOptions.  # noqa: E501
        :rtype: bool
        """
        return self._pull_requests

    @pull_requests.setter
    def pull_requests(self, pull_requests):
        """Sets the pull_requests of this MigrateRepoOptions.


        :param pull_requests: The pull_requests of this MigrateRepoOptions.  # noqa: E501
        :type: bool
        """

        self._pull_requests = pull_requests

    @property
    def releases(self):
        """Gets the releases of this MigrateRepoOptions.  # noqa: E501


        :return: The releases of this MigrateRepoOptions.  # noqa: E501
        :rtype: bool
        """
        return self._releases

    @releases.setter
    def releases(self, releases):
        """Sets the releases of this MigrateRepoOptions.


        :param releases: The releases of this MigrateRepoOptions.  # noqa: E501
        :type: bool
        """

        self._releases = releases

    @property
    def repo_name(self):
        """Gets the repo_name of this MigrateRepoOptions.  # noqa: E501


        :return: The repo_name of this MigrateRepoOptions.  # noqa: E501
        :rtype: str
        """
        return self._repo_name

    @repo_name.setter
    def repo_name(self, repo_name):
        """Sets the repo_name of this MigrateRepoOptions.


        :param repo_name: The repo_name of this MigrateRepoOptions.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and repo_name is None:
            raise ValueError("Invalid value for `repo_name`, must not be `None`")  # noqa: E501

        self._repo_name = repo_name

    @property
    def repo_owner(self):
        """Gets the repo_owner of this MigrateRepoOptions.  # noqa: E501

        Name of User or Organisation who will own Repo after migration  # noqa: E501

        :return: The repo_owner of this MigrateRepoOptions.  # noqa: E501
        :rtype: str
        """
        return self._repo_owner

    @repo_owner.setter
    def repo_owner(self, repo_owner):
        """Sets the repo_owner of this MigrateRepoOptions.

        Name of User or Organisation who will own Repo after migration  # noqa: E501

        :param repo_owner: The repo_owner of this MigrateRepoOptions.  # noqa: E501
        :type: str
        """

        self._repo_owner = repo_owner

    @property
    def service(self):
        """Gets the service of this MigrateRepoOptions.  # noqa: E501


        :return: The service of this MigrateRepoOptions.  # noqa: E501
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this MigrateRepoOptions.


        :param service: The service of this MigrateRepoOptions.  # noqa: E501
        :type: str
        """
        allowed_values = ["git", "github", "gitea", "gitlab"]  # noqa: E501
        if (self._configuration.client_side_validation and
                service not in allowed_values):
            raise ValueError(
                "Invalid value for `service` ({0}), must be one of {1}"  # noqa: E501
                .format(service, allowed_values)
            )

        self._service = service

    @property
    def uid(self):
        """Gets the uid of this MigrateRepoOptions.  # noqa: E501

        deprecated (only for backwards compatibility)  # noqa: E501

        :return: The uid of this MigrateRepoOptions.  # noqa: E501
        :rtype: int
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this MigrateRepoOptions.

        deprecated (only for backwards compatibility)  # noqa: E501

        :param uid: The uid of this MigrateRepoOptions.  # noqa: E501
        :type: int
        """

        self._uid = uid

    @property
    def wiki(self):
        """Gets the wiki of this MigrateRepoOptions.  # noqa: E501


        :return: The wiki of this MigrateRepoOptions.  # noqa: E501
        :rtype: bool
        """
        return self._wiki

    @wiki.setter
    def wiki(self, wiki):
        """Sets the wiki of this MigrateRepoOptions.


        :param wiki: The wiki of this MigrateRepoOptions.  # noqa: E501
        :type: bool
        """

        self._wiki = wiki

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
        if issubclass(MigrateRepoOptions, dict):
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
        if not isinstance(other, MigrateRepoOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MigrateRepoOptions):
            return True

        return self.to_dict() != other.to_dict()
