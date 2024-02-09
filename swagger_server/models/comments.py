# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Comments(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: int=None, content: str=None):  # noqa: E501
        """Comments - a model defined in Swagger

        :param id: The id of this Comments.  # noqa: E501
        :type id: int
        :param content: The content of this Comments.  # noqa: E501
        :type content: str
        """
        self.swagger_types = {
            'id': int,
            'content': str
        }

        self.attribute_map = {
            'id': 'id',
            'content': 'content'
        }
        self._id = id
        self._content = content

    @classmethod
    def from_dict(cls, dikt) -> 'Comments':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Comments of this Comments.  # noqa: E501
        :rtype: Comments
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this Comments.

        Comment identifier assigned by application  # noqa: E501

        :return: The id of this Comments.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this Comments.

        Comment identifier assigned by application  # noqa: E501

        :param id: The id of this Comments.
        :type id: int
        """

        self._id = id

    @property
    def content(self) -> str:
        """Gets the content of this Comments.

        Comment  # noqa: E501

        :return: The content of this Comments.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content: str):
        """Sets the content of this Comments.

        Comment  # noqa: E501

        :param content: The content of this Comments.
        :type content: str
        """
        if content is None:
            raise ValueError("Invalid value for `content`, must not be `None`")  # noqa: E501

        self._content = content
