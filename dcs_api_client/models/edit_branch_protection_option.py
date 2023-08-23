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


class EditBranchProtectionOption(object):
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
        'approvals_whitelist_teams': 'list[str]',
        'approvals_whitelist_username': 'list[str]',
        'block_on_official_review_requests': 'bool',
        'block_on_outdated_branch': 'bool',
        'block_on_rejected_reviews': 'bool',
        'dismiss_stale_approvals': 'bool',
        'enable_approvals_whitelist': 'bool',
        'enable_merge_whitelist': 'bool',
        'enable_push': 'bool',
        'enable_push_whitelist': 'bool',
        'enable_status_check': 'bool',
        'merge_whitelist_teams': 'list[str]',
        'merge_whitelist_usernames': 'list[str]',
        'protected_file_patterns': 'str',
        'push_whitelist_deploy_keys': 'bool',
        'push_whitelist_teams': 'list[str]',
        'push_whitelist_usernames': 'list[str]',
        'require_signed_commits': 'bool',
        'required_approvals': 'int',
        'status_check_contexts': 'list[str]',
        'unprotected_file_patterns': 'str'
    }

    attribute_map = {
        'approvals_whitelist_teams': 'approvals_whitelist_teams',
        'approvals_whitelist_username': 'approvals_whitelist_username',
        'block_on_official_review_requests': 'block_on_official_review_requests',
        'block_on_outdated_branch': 'block_on_outdated_branch',
        'block_on_rejected_reviews': 'block_on_rejected_reviews',
        'dismiss_stale_approvals': 'dismiss_stale_approvals',
        'enable_approvals_whitelist': 'enable_approvals_whitelist',
        'enable_merge_whitelist': 'enable_merge_whitelist',
        'enable_push': 'enable_push',
        'enable_push_whitelist': 'enable_push_whitelist',
        'enable_status_check': 'enable_status_check',
        'merge_whitelist_teams': 'merge_whitelist_teams',
        'merge_whitelist_usernames': 'merge_whitelist_usernames',
        'protected_file_patterns': 'protected_file_patterns',
        'push_whitelist_deploy_keys': 'push_whitelist_deploy_keys',
        'push_whitelist_teams': 'push_whitelist_teams',
        'push_whitelist_usernames': 'push_whitelist_usernames',
        'require_signed_commits': 'require_signed_commits',
        'required_approvals': 'required_approvals',
        'status_check_contexts': 'status_check_contexts',
        'unprotected_file_patterns': 'unprotected_file_patterns'
    }

    def __init__(self, approvals_whitelist_teams=None, approvals_whitelist_username=None, block_on_official_review_requests=None, block_on_outdated_branch=None, block_on_rejected_reviews=None, dismiss_stale_approvals=None, enable_approvals_whitelist=None, enable_merge_whitelist=None, enable_push=None, enable_push_whitelist=None, enable_status_check=None, merge_whitelist_teams=None, merge_whitelist_usernames=None, protected_file_patterns=None, push_whitelist_deploy_keys=None, push_whitelist_teams=None, push_whitelist_usernames=None, require_signed_commits=None, required_approvals=None, status_check_contexts=None, unprotected_file_patterns=None, _configuration=None):  # noqa: E501
        """EditBranchProtectionOption - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._approvals_whitelist_teams = None
        self._approvals_whitelist_username = None
        self._block_on_official_review_requests = None
        self._block_on_outdated_branch = None
        self._block_on_rejected_reviews = None
        self._dismiss_stale_approvals = None
        self._enable_approvals_whitelist = None
        self._enable_merge_whitelist = None
        self._enable_push = None
        self._enable_push_whitelist = None
        self._enable_status_check = None
        self._merge_whitelist_teams = None
        self._merge_whitelist_usernames = None
        self._protected_file_patterns = None
        self._push_whitelist_deploy_keys = None
        self._push_whitelist_teams = None
        self._push_whitelist_usernames = None
        self._require_signed_commits = None
        self._required_approvals = None
        self._status_check_contexts = None
        self._unprotected_file_patterns = None
        self.discriminator = None

        if approvals_whitelist_teams is not None:
            self.approvals_whitelist_teams = approvals_whitelist_teams
        if approvals_whitelist_username is not None:
            self.approvals_whitelist_username = approvals_whitelist_username
        if block_on_official_review_requests is not None:
            self.block_on_official_review_requests = block_on_official_review_requests
        if block_on_outdated_branch is not None:
            self.block_on_outdated_branch = block_on_outdated_branch
        if block_on_rejected_reviews is not None:
            self.block_on_rejected_reviews = block_on_rejected_reviews
        if dismiss_stale_approvals is not None:
            self.dismiss_stale_approvals = dismiss_stale_approvals
        if enable_approvals_whitelist is not None:
            self.enable_approvals_whitelist = enable_approvals_whitelist
        if enable_merge_whitelist is not None:
            self.enable_merge_whitelist = enable_merge_whitelist
        if enable_push is not None:
            self.enable_push = enable_push
        if enable_push_whitelist is not None:
            self.enable_push_whitelist = enable_push_whitelist
        if enable_status_check is not None:
            self.enable_status_check = enable_status_check
        if merge_whitelist_teams is not None:
            self.merge_whitelist_teams = merge_whitelist_teams
        if merge_whitelist_usernames is not None:
            self.merge_whitelist_usernames = merge_whitelist_usernames
        if protected_file_patterns is not None:
            self.protected_file_patterns = protected_file_patterns
        if push_whitelist_deploy_keys is not None:
            self.push_whitelist_deploy_keys = push_whitelist_deploy_keys
        if push_whitelist_teams is not None:
            self.push_whitelist_teams = push_whitelist_teams
        if push_whitelist_usernames is not None:
            self.push_whitelist_usernames = push_whitelist_usernames
        if require_signed_commits is not None:
            self.require_signed_commits = require_signed_commits
        if required_approvals is not None:
            self.required_approvals = required_approvals
        if status_check_contexts is not None:
            self.status_check_contexts = status_check_contexts
        if unprotected_file_patterns is not None:
            self.unprotected_file_patterns = unprotected_file_patterns

    @property
    def approvals_whitelist_teams(self):
        """Gets the approvals_whitelist_teams of this EditBranchProtectionOption.  # noqa: E501


        :return: The approvals_whitelist_teams of this EditBranchProtectionOption.  # noqa: E501
        :rtype: list[str]
        """
        return self._approvals_whitelist_teams

    @approvals_whitelist_teams.setter
    def approvals_whitelist_teams(self, approvals_whitelist_teams):
        """Sets the approvals_whitelist_teams of this EditBranchProtectionOption.


        :param approvals_whitelist_teams: The approvals_whitelist_teams of this EditBranchProtectionOption.  # noqa: E501
        :type: list[str]
        """

        self._approvals_whitelist_teams = approvals_whitelist_teams

    @property
    def approvals_whitelist_username(self):
        """Gets the approvals_whitelist_username of this EditBranchProtectionOption.  # noqa: E501


        :return: The approvals_whitelist_username of this EditBranchProtectionOption.  # noqa: E501
        :rtype: list[str]
        """
        return self._approvals_whitelist_username

    @approvals_whitelist_username.setter
    def approvals_whitelist_username(self, approvals_whitelist_username):
        """Sets the approvals_whitelist_username of this EditBranchProtectionOption.


        :param approvals_whitelist_username: The approvals_whitelist_username of this EditBranchProtectionOption.  # noqa: E501
        :type: list[str]
        """

        self._approvals_whitelist_username = approvals_whitelist_username

    @property
    def block_on_official_review_requests(self):
        """Gets the block_on_official_review_requests of this EditBranchProtectionOption.  # noqa: E501


        :return: The block_on_official_review_requests of this EditBranchProtectionOption.  # noqa: E501
        :rtype: bool
        """
        return self._block_on_official_review_requests

    @block_on_official_review_requests.setter
    def block_on_official_review_requests(self, block_on_official_review_requests):
        """Sets the block_on_official_review_requests of this EditBranchProtectionOption.


        :param block_on_official_review_requests: The block_on_official_review_requests of this EditBranchProtectionOption.  # noqa: E501
        :type: bool
        """

        self._block_on_official_review_requests = block_on_official_review_requests

    @property
    def block_on_outdated_branch(self):
        """Gets the block_on_outdated_branch of this EditBranchProtectionOption.  # noqa: E501


        :return: The block_on_outdated_branch of this EditBranchProtectionOption.  # noqa: E501
        :rtype: bool
        """
        return self._block_on_outdated_branch

    @block_on_outdated_branch.setter
    def block_on_outdated_branch(self, block_on_outdated_branch):
        """Sets the block_on_outdated_branch of this EditBranchProtectionOption.


        :param block_on_outdated_branch: The block_on_outdated_branch of this EditBranchProtectionOption.  # noqa: E501
        :type: bool
        """

        self._block_on_outdated_branch = block_on_outdated_branch

    @property
    def block_on_rejected_reviews(self):
        """Gets the block_on_rejected_reviews of this EditBranchProtectionOption.  # noqa: E501


        :return: The block_on_rejected_reviews of this EditBranchProtectionOption.  # noqa: E501
        :rtype: bool
        """
        return self._block_on_rejected_reviews

    @block_on_rejected_reviews.setter
    def block_on_rejected_reviews(self, block_on_rejected_reviews):
        """Sets the block_on_rejected_reviews of this EditBranchProtectionOption.


        :param block_on_rejected_reviews: The block_on_rejected_reviews of this EditBranchProtectionOption.  # noqa: E501
        :type: bool
        """

        self._block_on_rejected_reviews = block_on_rejected_reviews

    @property
    def dismiss_stale_approvals(self):
        """Gets the dismiss_stale_approvals of this EditBranchProtectionOption.  # noqa: E501


        :return: The dismiss_stale_approvals of this EditBranchProtectionOption.  # noqa: E501
        :rtype: bool
        """
        return self._dismiss_stale_approvals

    @dismiss_stale_approvals.setter
    def dismiss_stale_approvals(self, dismiss_stale_approvals):
        """Sets the dismiss_stale_approvals of this EditBranchProtectionOption.


        :param dismiss_stale_approvals: The dismiss_stale_approvals of this EditBranchProtectionOption.  # noqa: E501
        :type: bool
        """

        self._dismiss_stale_approvals = dismiss_stale_approvals

    @property
    def enable_approvals_whitelist(self):
        """Gets the enable_approvals_whitelist of this EditBranchProtectionOption.  # noqa: E501


        :return: The enable_approvals_whitelist of this EditBranchProtectionOption.  # noqa: E501
        :rtype: bool
        """
        return self._enable_approvals_whitelist

    @enable_approvals_whitelist.setter
    def enable_approvals_whitelist(self, enable_approvals_whitelist):
        """Sets the enable_approvals_whitelist of this EditBranchProtectionOption.


        :param enable_approvals_whitelist: The enable_approvals_whitelist of this EditBranchProtectionOption.  # noqa: E501
        :type: bool
        """

        self._enable_approvals_whitelist = enable_approvals_whitelist

    @property
    def enable_merge_whitelist(self):
        """Gets the enable_merge_whitelist of this EditBranchProtectionOption.  # noqa: E501


        :return: The enable_merge_whitelist of this EditBranchProtectionOption.  # noqa: E501
        :rtype: bool
        """
        return self._enable_merge_whitelist

    @enable_merge_whitelist.setter
    def enable_merge_whitelist(self, enable_merge_whitelist):
        """Sets the enable_merge_whitelist of this EditBranchProtectionOption.


        :param enable_merge_whitelist: The enable_merge_whitelist of this EditBranchProtectionOption.  # noqa: E501
        :type: bool
        """

        self._enable_merge_whitelist = enable_merge_whitelist

    @property
    def enable_push(self):
        """Gets the enable_push of this EditBranchProtectionOption.  # noqa: E501


        :return: The enable_push of this EditBranchProtectionOption.  # noqa: E501
        :rtype: bool
        """
        return self._enable_push

    @enable_push.setter
    def enable_push(self, enable_push):
        """Sets the enable_push of this EditBranchProtectionOption.


        :param enable_push: The enable_push of this EditBranchProtectionOption.  # noqa: E501
        :type: bool
        """

        self._enable_push = enable_push

    @property
    def enable_push_whitelist(self):
        """Gets the enable_push_whitelist of this EditBranchProtectionOption.  # noqa: E501


        :return: The enable_push_whitelist of this EditBranchProtectionOption.  # noqa: E501
        :rtype: bool
        """
        return self._enable_push_whitelist

    @enable_push_whitelist.setter
    def enable_push_whitelist(self, enable_push_whitelist):
        """Sets the enable_push_whitelist of this EditBranchProtectionOption.


        :param enable_push_whitelist: The enable_push_whitelist of this EditBranchProtectionOption.  # noqa: E501
        :type: bool
        """

        self._enable_push_whitelist = enable_push_whitelist

    @property
    def enable_status_check(self):
        """Gets the enable_status_check of this EditBranchProtectionOption.  # noqa: E501


        :return: The enable_status_check of this EditBranchProtectionOption.  # noqa: E501
        :rtype: bool
        """
        return self._enable_status_check

    @enable_status_check.setter
    def enable_status_check(self, enable_status_check):
        """Sets the enable_status_check of this EditBranchProtectionOption.


        :param enable_status_check: The enable_status_check of this EditBranchProtectionOption.  # noqa: E501
        :type: bool
        """

        self._enable_status_check = enable_status_check

    @property
    def merge_whitelist_teams(self):
        """Gets the merge_whitelist_teams of this EditBranchProtectionOption.  # noqa: E501


        :return: The merge_whitelist_teams of this EditBranchProtectionOption.  # noqa: E501
        :rtype: list[str]
        """
        return self._merge_whitelist_teams

    @merge_whitelist_teams.setter
    def merge_whitelist_teams(self, merge_whitelist_teams):
        """Sets the merge_whitelist_teams of this EditBranchProtectionOption.


        :param merge_whitelist_teams: The merge_whitelist_teams of this EditBranchProtectionOption.  # noqa: E501
        :type: list[str]
        """

        self._merge_whitelist_teams = merge_whitelist_teams

    @property
    def merge_whitelist_usernames(self):
        """Gets the merge_whitelist_usernames of this EditBranchProtectionOption.  # noqa: E501


        :return: The merge_whitelist_usernames of this EditBranchProtectionOption.  # noqa: E501
        :rtype: list[str]
        """
        return self._merge_whitelist_usernames

    @merge_whitelist_usernames.setter
    def merge_whitelist_usernames(self, merge_whitelist_usernames):
        """Sets the merge_whitelist_usernames of this EditBranchProtectionOption.


        :param merge_whitelist_usernames: The merge_whitelist_usernames of this EditBranchProtectionOption.  # noqa: E501
        :type: list[str]
        """

        self._merge_whitelist_usernames = merge_whitelist_usernames

    @property
    def protected_file_patterns(self):
        """Gets the protected_file_patterns of this EditBranchProtectionOption.  # noqa: E501


        :return: The protected_file_patterns of this EditBranchProtectionOption.  # noqa: E501
        :rtype: str
        """
        return self._protected_file_patterns

    @protected_file_patterns.setter
    def protected_file_patterns(self, protected_file_patterns):
        """Sets the protected_file_patterns of this EditBranchProtectionOption.


        :param protected_file_patterns: The protected_file_patterns of this EditBranchProtectionOption.  # noqa: E501
        :type: str
        """

        self._protected_file_patterns = protected_file_patterns

    @property
    def push_whitelist_deploy_keys(self):
        """Gets the push_whitelist_deploy_keys of this EditBranchProtectionOption.  # noqa: E501


        :return: The push_whitelist_deploy_keys of this EditBranchProtectionOption.  # noqa: E501
        :rtype: bool
        """
        return self._push_whitelist_deploy_keys

    @push_whitelist_deploy_keys.setter
    def push_whitelist_deploy_keys(self, push_whitelist_deploy_keys):
        """Sets the push_whitelist_deploy_keys of this EditBranchProtectionOption.


        :param push_whitelist_deploy_keys: The push_whitelist_deploy_keys of this EditBranchProtectionOption.  # noqa: E501
        :type: bool
        """

        self._push_whitelist_deploy_keys = push_whitelist_deploy_keys

    @property
    def push_whitelist_teams(self):
        """Gets the push_whitelist_teams of this EditBranchProtectionOption.  # noqa: E501


        :return: The push_whitelist_teams of this EditBranchProtectionOption.  # noqa: E501
        :rtype: list[str]
        """
        return self._push_whitelist_teams

    @push_whitelist_teams.setter
    def push_whitelist_teams(self, push_whitelist_teams):
        """Sets the push_whitelist_teams of this EditBranchProtectionOption.


        :param push_whitelist_teams: The push_whitelist_teams of this EditBranchProtectionOption.  # noqa: E501
        :type: list[str]
        """

        self._push_whitelist_teams = push_whitelist_teams

    @property
    def push_whitelist_usernames(self):
        """Gets the push_whitelist_usernames of this EditBranchProtectionOption.  # noqa: E501


        :return: The push_whitelist_usernames of this EditBranchProtectionOption.  # noqa: E501
        :rtype: list[str]
        """
        return self._push_whitelist_usernames

    @push_whitelist_usernames.setter
    def push_whitelist_usernames(self, push_whitelist_usernames):
        """Sets the push_whitelist_usernames of this EditBranchProtectionOption.


        :param push_whitelist_usernames: The push_whitelist_usernames of this EditBranchProtectionOption.  # noqa: E501
        :type: list[str]
        """

        self._push_whitelist_usernames = push_whitelist_usernames

    @property
    def require_signed_commits(self):
        """Gets the require_signed_commits of this EditBranchProtectionOption.  # noqa: E501


        :return: The require_signed_commits of this EditBranchProtectionOption.  # noqa: E501
        :rtype: bool
        """
        return self._require_signed_commits

    @require_signed_commits.setter
    def require_signed_commits(self, require_signed_commits):
        """Sets the require_signed_commits of this EditBranchProtectionOption.


        :param require_signed_commits: The require_signed_commits of this EditBranchProtectionOption.  # noqa: E501
        :type: bool
        """

        self._require_signed_commits = require_signed_commits

    @property
    def required_approvals(self):
        """Gets the required_approvals of this EditBranchProtectionOption.  # noqa: E501


        :return: The required_approvals of this EditBranchProtectionOption.  # noqa: E501
        :rtype: int
        """
        return self._required_approvals

    @required_approvals.setter
    def required_approvals(self, required_approvals):
        """Sets the required_approvals of this EditBranchProtectionOption.


        :param required_approvals: The required_approvals of this EditBranchProtectionOption.  # noqa: E501
        :type: int
        """

        self._required_approvals = required_approvals

    @property
    def status_check_contexts(self):
        """Gets the status_check_contexts of this EditBranchProtectionOption.  # noqa: E501


        :return: The status_check_contexts of this EditBranchProtectionOption.  # noqa: E501
        :rtype: list[str]
        """
        return self._status_check_contexts

    @status_check_contexts.setter
    def status_check_contexts(self, status_check_contexts):
        """Sets the status_check_contexts of this EditBranchProtectionOption.


        :param status_check_contexts: The status_check_contexts of this EditBranchProtectionOption.  # noqa: E501
        :type: list[str]
        """

        self._status_check_contexts = status_check_contexts

    @property
    def unprotected_file_patterns(self):
        """Gets the unprotected_file_patterns of this EditBranchProtectionOption.  # noqa: E501


        :return: The unprotected_file_patterns of this EditBranchProtectionOption.  # noqa: E501
        :rtype: str
        """
        return self._unprotected_file_patterns

    @unprotected_file_patterns.setter
    def unprotected_file_patterns(self, unprotected_file_patterns):
        """Sets the unprotected_file_patterns of this EditBranchProtectionOption.


        :param unprotected_file_patterns: The unprotected_file_patterns of this EditBranchProtectionOption.  # noqa: E501
        :type: str
        """

        self._unprotected_file_patterns = unprotected_file_patterns

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
        if issubclass(EditBranchProtectionOption, dict):
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
        if not isinstance(other, EditBranchProtectionOption):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EditBranchProtectionOption):
            return True

        return self.to_dict() != other.to_dict()
