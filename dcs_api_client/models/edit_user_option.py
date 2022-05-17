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


class EditUserOption(object):
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
        'active': 'bool',
        'admin': 'bool',
        'allow_create_organization': 'bool',
        'allow_git_hook': 'bool',
        'allow_import_local': 'bool',
        'description': 'str',
        'email': 'str',
        'full_name': 'str',
        'location': 'str',
        'login_name': 'str',
        'max_repo_creation': 'int',
        'must_change_password': 'bool',
        'password': 'str',
        'prohibit_login': 'bool',
        'restricted': 'bool',
        'source_id': 'int',
        'visibility': 'str',
        'website': 'str'
    }

    attribute_map = {
        'active': 'active',
        'admin': 'admin',
        'allow_create_organization': 'allow_create_organization',
        'allow_git_hook': 'allow_git_hook',
        'allow_import_local': 'allow_import_local',
        'description': 'description',
        'email': 'email',
        'full_name': 'full_name',
        'location': 'location',
        'login_name': 'login_name',
        'max_repo_creation': 'max_repo_creation',
        'must_change_password': 'must_change_password',
        'password': 'password',
        'prohibit_login': 'prohibit_login',
        'restricted': 'restricted',
        'source_id': 'source_id',
        'visibility': 'visibility',
        'website': 'website'
    }

    def __init__(self, active=None, admin=None, allow_create_organization=None, allow_git_hook=None, allow_import_local=None, description=None, email=None, full_name=None, location=None, login_name=None, max_repo_creation=None, must_change_password=None, password=None, prohibit_login=None, restricted=None, source_id=None, visibility=None, website=None, _configuration=None):  # noqa: E501
        """EditUserOption - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._active = None
        self._admin = None
        self._allow_create_organization = None
        self._allow_git_hook = None
        self._allow_import_local = None
        self._description = None
        self._email = None
        self._full_name = None
        self._location = None
        self._login_name = None
        self._max_repo_creation = None
        self._must_change_password = None
        self._password = None
        self._prohibit_login = None
        self._restricted = None
        self._source_id = None
        self._visibility = None
        self._website = None
        self.discriminator = None

        if active is not None:
            self.active = active
        if admin is not None:
            self.admin = admin
        if allow_create_organization is not None:
            self.allow_create_organization = allow_create_organization
        if allow_git_hook is not None:
            self.allow_git_hook = allow_git_hook
        if allow_import_local is not None:
            self.allow_import_local = allow_import_local
        if description is not None:
            self.description = description
        if email is not None:
            self.email = email
        if full_name is not None:
            self.full_name = full_name
        if location is not None:
            self.location = location
        self.login_name = login_name
        if max_repo_creation is not None:
            self.max_repo_creation = max_repo_creation
        if must_change_password is not None:
            self.must_change_password = must_change_password
        if password is not None:
            self.password = password
        if prohibit_login is not None:
            self.prohibit_login = prohibit_login
        if restricted is not None:
            self.restricted = restricted
        self.source_id = source_id
        if visibility is not None:
            self.visibility = visibility
        if website is not None:
            self.website = website

    @property
    def active(self):
        """Gets the active of this EditUserOption.  # noqa: E501


        :return: The active of this EditUserOption.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this EditUserOption.


        :param active: The active of this EditUserOption.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def admin(self):
        """Gets the admin of this EditUserOption.  # noqa: E501


        :return: The admin of this EditUserOption.  # noqa: E501
        :rtype: bool
        """
        return self._admin

    @admin.setter
    def admin(self, admin):
        """Sets the admin of this EditUserOption.


        :param admin: The admin of this EditUserOption.  # noqa: E501
        :type: bool
        """

        self._admin = admin

    @property
    def allow_create_organization(self):
        """Gets the allow_create_organization of this EditUserOption.  # noqa: E501


        :return: The allow_create_organization of this EditUserOption.  # noqa: E501
        :rtype: bool
        """
        return self._allow_create_organization

    @allow_create_organization.setter
    def allow_create_organization(self, allow_create_organization):
        """Sets the allow_create_organization of this EditUserOption.


        :param allow_create_organization: The allow_create_organization of this EditUserOption.  # noqa: E501
        :type: bool
        """

        self._allow_create_organization = allow_create_organization

    @property
    def allow_git_hook(self):
        """Gets the allow_git_hook of this EditUserOption.  # noqa: E501


        :return: The allow_git_hook of this EditUserOption.  # noqa: E501
        :rtype: bool
        """
        return self._allow_git_hook

    @allow_git_hook.setter
    def allow_git_hook(self, allow_git_hook):
        """Sets the allow_git_hook of this EditUserOption.


        :param allow_git_hook: The allow_git_hook of this EditUserOption.  # noqa: E501
        :type: bool
        """

        self._allow_git_hook = allow_git_hook

    @property
    def allow_import_local(self):
        """Gets the allow_import_local of this EditUserOption.  # noqa: E501


        :return: The allow_import_local of this EditUserOption.  # noqa: E501
        :rtype: bool
        """
        return self._allow_import_local

    @allow_import_local.setter
    def allow_import_local(self, allow_import_local):
        """Sets the allow_import_local of this EditUserOption.


        :param allow_import_local: The allow_import_local of this EditUserOption.  # noqa: E501
        :type: bool
        """

        self._allow_import_local = allow_import_local

    @property
    def description(self):
        """Gets the description of this EditUserOption.  # noqa: E501


        :return: The description of this EditUserOption.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this EditUserOption.


        :param description: The description of this EditUserOption.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def email(self):
        """Gets the email of this EditUserOption.  # noqa: E501


        :return: The email of this EditUserOption.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this EditUserOption.


        :param email: The email of this EditUserOption.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def full_name(self):
        """Gets the full_name of this EditUserOption.  # noqa: E501


        :return: The full_name of this EditUserOption.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this EditUserOption.


        :param full_name: The full_name of this EditUserOption.  # noqa: E501
        :type: str
        """

        self._full_name = full_name

    @property
    def location(self):
        """Gets the location of this EditUserOption.  # noqa: E501


        :return: The location of this EditUserOption.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this EditUserOption.


        :param location: The location of this EditUserOption.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def login_name(self):
        """Gets the login_name of this EditUserOption.  # noqa: E501


        :return: The login_name of this EditUserOption.  # noqa: E501
        :rtype: str
        """
        return self._login_name

    @login_name.setter
    def login_name(self, login_name):
        """Sets the login_name of this EditUserOption.


        :param login_name: The login_name of this EditUserOption.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and login_name is None:
            raise ValueError("Invalid value for `login_name`, must not be `None`")  # noqa: E501

        self._login_name = login_name

    @property
    def max_repo_creation(self):
        """Gets the max_repo_creation of this EditUserOption.  # noqa: E501


        :return: The max_repo_creation of this EditUserOption.  # noqa: E501
        :rtype: int
        """
        return self._max_repo_creation

    @max_repo_creation.setter
    def max_repo_creation(self, max_repo_creation):
        """Sets the max_repo_creation of this EditUserOption.


        :param max_repo_creation: The max_repo_creation of this EditUserOption.  # noqa: E501
        :type: int
        """

        self._max_repo_creation = max_repo_creation

    @property
    def must_change_password(self):
        """Gets the must_change_password of this EditUserOption.  # noqa: E501


        :return: The must_change_password of this EditUserOption.  # noqa: E501
        :rtype: bool
        """
        return self._must_change_password

    @must_change_password.setter
    def must_change_password(self, must_change_password):
        """Sets the must_change_password of this EditUserOption.


        :param must_change_password: The must_change_password of this EditUserOption.  # noqa: E501
        :type: bool
        """

        self._must_change_password = must_change_password

    @property
    def password(self):
        """Gets the password of this EditUserOption.  # noqa: E501


        :return: The password of this EditUserOption.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this EditUserOption.


        :param password: The password of this EditUserOption.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def prohibit_login(self):
        """Gets the prohibit_login of this EditUserOption.  # noqa: E501


        :return: The prohibit_login of this EditUserOption.  # noqa: E501
        :rtype: bool
        """
        return self._prohibit_login

    @prohibit_login.setter
    def prohibit_login(self, prohibit_login):
        """Sets the prohibit_login of this EditUserOption.


        :param prohibit_login: The prohibit_login of this EditUserOption.  # noqa: E501
        :type: bool
        """

        self._prohibit_login = prohibit_login

    @property
    def restricted(self):
        """Gets the restricted of this EditUserOption.  # noqa: E501


        :return: The restricted of this EditUserOption.  # noqa: E501
        :rtype: bool
        """
        return self._restricted

    @restricted.setter
    def restricted(self, restricted):
        """Sets the restricted of this EditUserOption.


        :param restricted: The restricted of this EditUserOption.  # noqa: E501
        :type: bool
        """

        self._restricted = restricted

    @property
    def source_id(self):
        """Gets the source_id of this EditUserOption.  # noqa: E501


        :return: The source_id of this EditUserOption.  # noqa: E501
        :rtype: int
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """Sets the source_id of this EditUserOption.


        :param source_id: The source_id of this EditUserOption.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and source_id is None:
            raise ValueError("Invalid value for `source_id`, must not be `None`")  # noqa: E501

        self._source_id = source_id

    @property
    def visibility(self):
        """Gets the visibility of this EditUserOption.  # noqa: E501


        :return: The visibility of this EditUserOption.  # noqa: E501
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        """Sets the visibility of this EditUserOption.


        :param visibility: The visibility of this EditUserOption.  # noqa: E501
        :type: str
        """

        self._visibility = visibility

    @property
    def website(self):
        """Gets the website of this EditUserOption.  # noqa: E501


        :return: The website of this EditUserOption.  # noqa: E501
        :rtype: str
        """
        return self._website

    @website.setter
    def website(self, website):
        """Sets the website of this EditUserOption.


        :param website: The website of this EditUserOption.  # noqa: E501
        :type: str
        """

        self._website = website

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
        if issubclass(EditUserOption, dict):
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
        if not isinstance(other, EditUserOption):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EditUserOption):
            return True

        return self.to_dict() != other.to_dict()
