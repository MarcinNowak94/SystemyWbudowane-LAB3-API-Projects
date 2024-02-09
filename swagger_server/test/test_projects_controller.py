# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.comments import Comments  # noqa: E501
from swagger_server.models.projects import Projects  # noqa: E501
from swagger_server.models.tasks import Tasks  # noqa: E501
from swagger_server.models.team_members import TeamMembers  # noqa: E501
from swagger_server.test import BaseTestCase


class TestProjectsController(BaseTestCase):
    """ProjectsController integration test stubs"""

    def test_add_project(self):
        """Test case for add_project

        Add new project
        """
        body = Projects()
        response = self.client.open(
            '/projects',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_add_task(self):
        """Test case for add_task

        Add new task
        """
        body = Tasks()
        response = self.client.open(
            '/projects/{projectID}/tasks'.format(project_id=789),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

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

    def test_add_team_member_to_project(self):
        """Test case for add_team_member_to_project

        Add new teammember to project
        """
        body = TeamMembers()
        response = self.client.open(
            '/projects/{projectID}/team-members'.format(project_id=789),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_project_by_id(self):
        """Test case for delete_project_by_id

        Delete project with specified ID
        """
        response = self.client.open(
            '/projects/{projectID}'.format(project_id=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_task_by_id(self):
        """Test case for delete_task_by_id

        Delete task with specified ID
        """
        response = self.client.open(
            '/projects/{projectID}/tasks/{taskID}'.format(project_id=789, task_id=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_project_by_id(self):
        """Test case for get_project_by_id

        List project
        """
        response = self.client.open(
            '/projects/{projectID}'.format(project_id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_project_tasks(self):
        """Test case for get_project_tasks

        List project tasks
        """
        response = self.client.open(
            '/projects/{projectID}/tasks'.format(project_id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_project_team_members(self):
        """Test case for get_project_team_members

        List project team members
        """
        response = self.client.open(
            '/projects/{projectID}/team-members'.format(project_id=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_task_by_id(self):
        """Test case for get_task_by_id

        List task
        """
        response = self.client.open(
            '/projects/{projectID}/tasks/{taskID}'.format(project_id=789, task_id=789),
            method='GET')
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

    def test_overwrite_project_by_id(self):
        """Test case for overwrite_project_by_id

        Overwrite project with specified ID
        """
        body = Projects()
        response = self.client.open(
            '/projects/{projectID}'.format(project_id=789),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_overwrite_task_by_id(self):
        """Test case for overwrite_task_by_id

        Overwrite task with specified ID
        """
        body = Tasks()
        response = self.client.open(
            '/projects/{projectID}/tasks/{taskID}'.format(project_id=789, task_id=789),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_projects_get(self):
        """Test case for projects_get

        List all projects
        """
        response = self.client.open(
            '/projects',
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

    def test_remove_team_member_from_project(self):
        """Test case for remove_team_member_from_project

        Delete teammember from project
        """
        response = self.client.open(
            '/projects/{projectID}/team-members/{teammemberID}'.format(project_id=789, teammember_id=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
