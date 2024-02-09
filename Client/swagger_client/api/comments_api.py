# coding: utf-8

"""
    Systemy Wielowarstwowe Lab2 API

    _08255 Nowak Marcin 7ION_  Opis API API powinno być spełniać wszystkie reguły REST (za wyjątkiem kodu na żądanie) oraz implementować HATEOAS. Będzie się ono składać się z następujących zasobów: projekty, zadania, komentarze do zadań oraz członkowie zespołu. Dla uproszczenia zakładamy, że API dostępne jest tylko wewnątrz prywatnej sieci i nie wymaga uwierzytelniania ani autoryzacji użytkowników.  Funkcjonalność do zaimplementowania Funkcjonalność, która powinna być udostępniona przez API została podzielona wg. zasobów w systemie. - Projekty   - Tworzenie nowego projektu. Podczas tworzenia nowego projektu użytkownik powinien podać podstawowe dane (jak np. nazwa, opis, data rozpoczęcia czy też planowana data zakończenia). W odpowiedzi klient powinien otrzymać identyfikator nowego projektu.   - Pobieranie listy wszystkich projektów.   - Pobieranie szczegółów na temat danego projektu.   - Aktualizacja szczegółów danego projektu.   - Usuwanie konkretnego projektu. - Zadania   - Dodawanie nowego zadania w ramach konkretnego projektu. Zadanie powinno zawierać takie informacje jak nazwa, opis, priorytet oraz szacowany termin wykonania.   - Listowanie zadań w ramach konkretnego projektu.   - Pobieranie szczegółów konkretnego zadania.   - Aktualizacja szczegółów konkretnego zadania.   - Usuwanie konkretnego zadania. - Członkowie zespołu   - Dodawanie nowego użytkownika do zespołu projektowego.   - Pobieranie listy członków zespołu danego projektu.   - Usuwanie użytkownika z zespołu. - Komentarze   - Możliwość dodawania nowego komentarza do konkretnego zadania.   - Możliwość pobierania listy komentarzy do konkretnego zadania.   - Usuwanie konkretnego komentarza.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: marcin.nowak1@edu.wsti.pl
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class CommentsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_task_comments(self, body, project_id, task_id, **kwargs):  # noqa: E501
        """Add task comment  # noqa: E501

        Adds task comment and returns created id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_task_comments(body, project_id, task_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Tasks body: (required)
        :param int project_id: ID of project (required)
        :param int task_id: ID of task (required)
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_task_comments_with_http_info(body, project_id, task_id, **kwargs)  # noqa: E501
        else:
            (data) = self.add_task_comments_with_http_info(body, project_id, task_id, **kwargs)  # noqa: E501
            return data

    def add_task_comments_with_http_info(self, body, project_id, task_id, **kwargs):  # noqa: E501
        """Add task comment  # noqa: E501

        Adds task comment and returns created id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_task_comments_with_http_info(body, project_id, task_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Tasks body: (required)
        :param int project_id: ID of project (required)
        :param int task_id: ID of task (required)
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'project_id', 'task_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_task_comments" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `add_task_comments`")  # noqa: E501
        # verify the required parameter 'project_id' is set
        if ('project_id' not in params or
                params['project_id'] is None):
            raise ValueError("Missing the required parameter `project_id` when calling `add_task_comments`")  # noqa: E501
        # verify the required parameter 'task_id' is set
        if ('task_id' not in params or
                params['task_id'] is None):
            raise ValueError("Missing the required parameter `task_id` when calling `add_task_comments`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_id' in params:
            path_params['projectID'] = params['project_id']  # noqa: E501
        if 'task_id' in params:
            path_params['taskID'] = params['task_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/projects/{projectID}/tasks/{taskID}/comments', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='int',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_task_comments(self, project_id, task_id, **kwargs):  # noqa: E501
        """List task comments  # noqa: E501

        Return task comments  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_task_comments(project_id, task_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int project_id: ID of project (required)
        :param int task_id: ID of task (required)
        :return: list[Comments]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_task_comments_with_http_info(project_id, task_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_task_comments_with_http_info(project_id, task_id, **kwargs)  # noqa: E501
            return data

    def get_task_comments_with_http_info(self, project_id, task_id, **kwargs):  # noqa: E501
        """List task comments  # noqa: E501

        Return task comments  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_task_comments_with_http_info(project_id, task_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int project_id: ID of project (required)
        :param int task_id: ID of task (required)
        :return: list[Comments]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_id', 'task_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_task_comments" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_id' is set
        if ('project_id' not in params or
                params['project_id'] is None):
            raise ValueError("Missing the required parameter `project_id` when calling `get_task_comments`")  # noqa: E501
        # verify the required parameter 'task_id' is set
        if ('task_id' not in params or
                params['task_id'] is None):
            raise ValueError("Missing the required parameter `task_id` when calling `get_task_comments`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_id' in params:
            path_params['projectID'] = params['project_id']  # noqa: E501
        if 'task_id' in params:
            path_params['taskID'] = params['task_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/projects/{projectID}/tasks/{taskID}/comments', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Comments]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def remove_task_comments(self, project_id, task_id, comment_id, **kwargs):  # noqa: E501
        """Delete task comment  # noqa: E501

        Deletes task comment  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_task_comments(project_id, task_id, comment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int project_id: ID of project (required)
        :param int task_id: ID of task (required)
        :param int comment_id: ID of comment (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.remove_task_comments_with_http_info(project_id, task_id, comment_id, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_task_comments_with_http_info(project_id, task_id, comment_id, **kwargs)  # noqa: E501
            return data

    def remove_task_comments_with_http_info(self, project_id, task_id, comment_id, **kwargs):  # noqa: E501
        """Delete task comment  # noqa: E501

        Deletes task comment  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_task_comments_with_http_info(project_id, task_id, comment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int project_id: ID of project (required)
        :param int task_id: ID of task (required)
        :param int comment_id: ID of comment (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_id', 'task_id', 'comment_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_task_comments" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_id' is set
        if ('project_id' not in params or
                params['project_id'] is None):
            raise ValueError("Missing the required parameter `project_id` when calling `remove_task_comments`")  # noqa: E501
        # verify the required parameter 'task_id' is set
        if ('task_id' not in params or
                params['task_id'] is None):
            raise ValueError("Missing the required parameter `task_id` when calling `remove_task_comments`")  # noqa: E501
        # verify the required parameter 'comment_id' is set
        if ('comment_id' not in params or
                params['comment_id'] is None):
            raise ValueError("Missing the required parameter `comment_id` when calling `remove_task_comments`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_id' in params:
            path_params['projectID'] = params['project_id']  # noqa: E501
        if 'task_id' in params:
            path_params['taskID'] = params['task_id']  # noqa: E501
        if 'comment_id' in params:
            path_params['commentID'] = params['comment_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/projects/{projectID}/tasks/{taskID}/comments/{commentID}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)