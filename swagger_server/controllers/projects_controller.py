import connexion
import six

from swagger_server.models.comments import Comments  # noqa: E501
from swagger_server.models.projects import Projects  # noqa: E501
from swagger_server.models.tasks import Tasks  # noqa: E501
from swagger_server.models.team_members import TeamMembers  # noqa: E501
from swagger_server import util


def add_project(body):  # noqa: E501
    """Add new project

    Adds new project and returns assigned ID # noqa: E501

    :param body: Create new project
    :type body: dict | bytes

    :rtype: int
    """
    if connexion.request.is_json:
        body = Projects.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def add_task(body, project_id):  # noqa: E501
    """Add new task

    Adds new task and returns assigned ID # noqa: E501

    :param body: Create new task
    :type body: dict | bytes
    :param project_id: ID of project to add task to
    :type project_id: int

    :rtype: int
    """
    if connexion.request.is_json:
        body = Tasks.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def add_task_comments(body, project_id, task_id):  # noqa: E501
    """Add task comment

    Adds task comment and returns created id # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param project_id: ID of project
    :type project_id: int
    :param task_id: ID of task
    :type task_id: int

    :rtype: int
    """
    if connexion.request.is_json:
        body = Tasks.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


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


def delete_project_by_id(project_id):  # noqa: E501
    """Delete project with specified ID

    Delete a single project # noqa: E501

    :param project_id: ID of project to delete
    :type project_id: int

    :rtype: None
    """
    return 'do some magic!'


def delete_task_by_id(project_id, task_id):  # noqa: E501
    """Delete task with specified ID

    Delete a single task # noqa: E501

    :param project_id: ID of project to delete task from
    :type project_id: int
    :param task_id: ID of task to delete
    :type task_id: int

    :rtype: None
    """
    return 'do some magic!'


def get_project_by_id(project_id):  # noqa: E501
    """List project

    Return a single project # noqa: E501

    :param project_id: ID of project to return
    :type project_id: int

    :rtype: Projects
    """
    return 'do some magic!'


def get_project_tasks(project_id):  # noqa: E501
    """List project tasks

    Return project tasks # noqa: E501

    :param project_id: ID of project to return tasklist from
    :type project_id: int

    :rtype: List[Tasks]
    """
    return 'do some magic!'


def get_project_team_members(project_id):  # noqa: E501
    """List project team members

    Return project team members # noqa: E501

    :param project_id: ID of project to return team members from
    :type project_id: int

    :rtype: List[TeamMembers]
    """
    return 'do some magic!'


def get_task_by_id(project_id, task_id):  # noqa: E501
    """List task

    Return a single task # noqa: E501

    :param project_id: ID of project to get task from
    :type project_id: int
    :param task_id: ID of task to return
    :type task_id: int

    :rtype: Tasks
    """
    return 'do some magic!'


def get_task_comments(project_id, task_id):  # noqa: E501
    """List task comments

    Return task comments # noqa: E501

    :param project_id: ID of project
    :type project_id: int
    :param task_id: ID of task
    :type task_id: int

    :rtype: List[Comments]
    """
    return 'do some magic!'


def overwrite_project_by_id(body, project_id):  # noqa: E501
    """Overwrite project with specified ID

    Fully overwrite project with specified ID # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param project_id: ID of project to update
    :type project_id: int

    :rtype: Projects
    """
    if connexion.request.is_json:
        body = Projects.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def overwrite_task_by_id(body, project_id, task_id):  # noqa: E501
    """Overwrite task with specified ID

    Fully overwrite task with specified ID # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param project_id: ID of project to overvrite task
    :type project_id: int
    :param task_id: ID of task to update
    :type task_id: int

    :rtype: Tasks
    """
    if connexion.request.is_json:
        body = Tasks.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def projects_get():  # noqa: E501
    """List all projects

    Returns all projects # noqa: E501


    :rtype: List[Projects]
    """
    return 'do some magic!'


def remove_task_comments(project_id, task_id, comment_id):  # noqa: E501
    """Delete task comment

    Deletes task comment # noqa: E501

    :param project_id: ID of project
    :type project_id: int
    :param task_id: ID of task
    :type task_id: int
    :param comment_id: ID of comment
    :type comment_id: int

    :rtype: None
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
