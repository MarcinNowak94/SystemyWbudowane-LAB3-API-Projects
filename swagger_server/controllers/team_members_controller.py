import connexion
import six

from swagger_server.models.team_members import TeamMembers  # noqa: E501
from swagger_server import util


def add_team_member_to_project(body, project_id):  # noqa: E501
    """Add new teammember to project

    Adds new teammember and returns assigned ID # noqa: E501

    :param body: Create new teammember
    :type body: dict | bytes
    :param project_id: ID of project to add team members to
    :type project_id: int

    :rtype: int
    """
    if connexion.request.is_json:
        body = TeamMembers.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_project_team_members(project_id):  # noqa: E501
    """List project team members

    Return project team members # noqa: E501

    :param project_id: ID of project to return team members from
    :type project_id: int

    :rtype: List[TeamMembers]
    """
    return 'do some magic!'


def remove_team_member_from_project(project_id, teammember_id):  # noqa: E501
    """Delete teammember from project

    Adds new teammember and returns assigned ID # noqa: E501

    :param project_id: ID of project to remove team member from
    :type project_id: int
    :param teammember_id: ID of project team member to remove
    :type teammember_id: int

    :rtype: None
    """
    return 'do some magic!'
