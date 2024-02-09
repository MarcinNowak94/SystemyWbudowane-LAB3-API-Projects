# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.team_members import TeamMembers  # noqa: E501
from swagger_server.test import BaseTestCase


class TestTeamMembersController(BaseTestCase):
    """TeamMembersController integration test stubs"""

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

    def test_get_project_team_members(self):
        """Test case for get_project_team_members

        List project team members
        """
        response = self.client.open(
            '/projects/{projectID}/team-members'.format(project_id=789),
            method='GET')
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
