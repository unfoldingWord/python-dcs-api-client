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


class Cron(object):
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
        'exec_times': 'int',
        'name': 'str',
        'next': 'datetime',
        'prev': 'datetime',
        'schedule': 'str'
    }

    attribute_map = {
        'exec_times': 'exec_times',
        'name': 'name',
        'next': 'next',
        'prev': 'prev',
        'schedule': 'schedule'
    }

    def __init__(self, exec_times=None, name=None, next=None, prev=None, schedule=None, _configuration=None):  # noqa: E501
        """Cron - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._exec_times = None
        self._name = None
        self._next = None
        self._prev = None
        self._schedule = None
        self.discriminator = None

        if exec_times is not None:
            self.exec_times = exec_times
        if name is not None:
            self.name = name
        if next is not None:
            self.next = next
        if prev is not None:
            self.prev = prev
        if schedule is not None:
            self.schedule = schedule

    @property
    def exec_times(self):
        """Gets the exec_times of this Cron.  # noqa: E501


        :return: The exec_times of this Cron.  # noqa: E501
        :rtype: int
        """
        return self._exec_times

    @exec_times.setter
    def exec_times(self, exec_times):
        """Sets the exec_times of this Cron.


        :param exec_times: The exec_times of this Cron.  # noqa: E501
        :type: int
        """

        self._exec_times = exec_times

    @property
    def name(self):
        """Gets the name of this Cron.  # noqa: E501


        :return: The name of this Cron.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Cron.


        :param name: The name of this Cron.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def next(self):
        """Gets the next of this Cron.  # noqa: E501


        :return: The next of this Cron.  # noqa: E501
        :rtype: datetime
        """
        return self._next

    @next.setter
    def next(self, next):
        """Sets the next of this Cron.


        :param next: The next of this Cron.  # noqa: E501
        :type: datetime
        """

        self._next = next

    @property
    def prev(self):
        """Gets the prev of this Cron.  # noqa: E501


        :return: The prev of this Cron.  # noqa: E501
        :rtype: datetime
        """
        return self._prev

    @prev.setter
    def prev(self, prev):
        """Sets the prev of this Cron.


        :param prev: The prev of this Cron.  # noqa: E501
        :type: datetime
        """

        self._prev = prev

    @property
    def schedule(self):
        """Gets the schedule of this Cron.  # noqa: E501


        :return: The schedule of this Cron.  # noqa: E501
        :rtype: str
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this Cron.


        :param schedule: The schedule of this Cron.  # noqa: E501
        :type: str
        """

        self._schedule = schedule

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
        if issubclass(Cron, dict):
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
        if not isinstance(other, Cron):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Cron):
            return True

        return self.to_dict() != other.to_dict()
