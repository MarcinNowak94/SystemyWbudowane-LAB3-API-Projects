import connexion
import six

from swagger_server.models.comments import Comments  # noqa: E501
from swagger_server.models.tasks import Tasks  # noqa: E501
from swagger_server import util


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
