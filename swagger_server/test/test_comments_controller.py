# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.comments import Comments  # noqa: E501
from swagger_server.models.tasks import Tasks  # noqa: E501
from swagger_server.test import BaseTestCase


class TestCommentsController(BaseTestCase):
    """CommentsController integration test stubs"""

    def test_add_task_comments(self):
        """Test case for add_task_comments

        Add task comment
        """
        body = Tasks()
        response = self.client.open(
            '/projects/{projectID}/tasks/{taskID}/comments'.format(project_id=789, task_id=789),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_task_comments(self):
        """Test case for get_task_comments

        List task comments
        """
        response = self.client.open(
            '/projects/{projectID}/tasks/{taskID}/comments'.format(project_id=789, task_id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_remove_task_comments(self):
        """Test case for remove_task_comments

        Delete task comment
        """
        response = self.client.open(
            '/projects/{projectID}/tasks/{taskID}/comments/{commentID}'.format(project_id=789, task_id=789, comment_id=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
