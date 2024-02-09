# swagger_client.ProjectsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_project**](ProjectsApi.md#add_project) | **POST** /projects | Add new project
[**add_task**](ProjectsApi.md#add_task) | **POST** /projects/{projectID}/tasks | Add new task
[**add_task_comments**](ProjectsApi.md#add_task_comments) | **POST** /projects/{projectID}/tasks/{taskID}/comments | Add task comment
[**add_team_member_to_project**](ProjectsApi.md#add_team_member_to_project) | **POST** /projects/{projectID}/team-members | Add new teammember to project
[**delete_project_by_id**](ProjectsApi.md#delete_project_by_id) | **DELETE** /projects/{projectID} | Delete project with specified ID
[**delete_task_by_id**](ProjectsApi.md#delete_task_by_id) | **DELETE** /projects/{projectID}/tasks/{taskID} | Delete task with specified ID
[**get_project_by_id**](ProjectsApi.md#get_project_by_id) | **GET** /projects/{projectID} | List project
[**get_project_tasks**](ProjectsApi.md#get_project_tasks) | **GET** /projects/{projectID}/tasks | List project tasks
[**get_project_team_members**](ProjectsApi.md#get_project_team_members) | **GET** /projects/{projectID}/team-members | List project team members
[**get_task_by_id**](ProjectsApi.md#get_task_by_id) | **GET** /projects/{projectID}/tasks/{taskID} | List task
[**get_task_comments**](ProjectsApi.md#get_task_comments) | **GET** /projects/{projectID}/tasks/{taskID}/comments | List task comments
[**overwrite_project_by_id**](ProjectsApi.md#overwrite_project_by_id) | **PUT** /projects/{projectID} | Overwrite project with specified ID
[**overwrite_task_by_id**](ProjectsApi.md#overwrite_task_by_id) | **PUT** /projects/{projectID}/tasks/{taskID} | Overwrite task with specified ID
[**projects_get**](ProjectsApi.md#projects_get) | **GET** /projects | List all projects
[**remove_task_comments**](ProjectsApi.md#remove_task_comments) | **DELETE** /projects/{projectID}/tasks/{taskID}/comments/{commentID} | Delete task comment
[**remove_team_member_from_project**](ProjectsApi.md#remove_team_member_from_project) | **DELETE** /projects/{projectID}/team-members/{teammemberID} | Delete teammember from project

# **add_project**
> int add_project(body)

Add new project

Adds new project and returns assigned ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectsApi()
body = swagger_client.Projects() # Projects | Create new project

try:
    # Add new project
    api_response = api_instance.add_project(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->add_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Projects**](Projects.md)| Create new project | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_task**
> int add_task(body, project_id)

Add new task

Adds new task and returns assigned ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectsApi()
body = swagger_client.Tasks() # Tasks | Create new task
project_id = 789 # int | ID of project to add task to

try:
    # Add new task
    api_response = api_instance.add_task(body, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->add_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Tasks**](Tasks.md)| Create new task | 
 **project_id** | **int**| ID of project to add task to | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_task_comments**
> int add_task_comments(body, project_id, task_id)

Add task comment

Adds task comment and returns created id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectsApi()
body = swagger_client.Tasks() # Tasks | 
project_id = 789 # int | ID of project
task_id = 789 # int | ID of task

try:
    # Add task comment
    api_response = api_instance.add_task_comments(body, project_id, task_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->add_task_comments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Tasks**](Tasks.md)|  | 
 **project_id** | **int**| ID of project | 
 **task_id** | **int**| ID of task | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_team_member_to_project**
> int add_team_member_to_project(body, project_id)

Add new teammember to project

Adds new teammember and returns assigned ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectsApi()
body = swagger_client.TeamMembers() # TeamMembers | Create new teammember
project_id = 789 # int | ID of project to add team members to

try:
    # Add new teammember to project
    api_response = api_instance.add_team_member_to_project(body, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->add_team_member_to_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TeamMembers**](TeamMembers.md)| Create new teammember | 
 **project_id** | **int**| ID of project to add team members to | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project_by_id**
> delete_project_by_id(project_id)

Delete project with specified ID

Delete a single project

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectsApi()
project_id = 789 # int | ID of project to delete

try:
    # Delete project with specified ID
    api_instance.delete_project_by_id(project_id)
except ApiException as e:
    print("Exception when calling ProjectsApi->delete_project_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of project to delete | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_task_by_id**
> delete_task_by_id(project_id, task_id)

Delete task with specified ID

Delete a single task

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectsApi()
project_id = 789 # int | ID of project to delete task from
task_id = 789 # int | ID of task to delete

try:
    # Delete task with specified ID
    api_instance.delete_task_by_id(project_id, task_id)
except ApiException as e:
    print("Exception when calling ProjectsApi->delete_task_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of project to delete task from | 
 **task_id** | **int**| ID of task to delete | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_by_id**
> Projects get_project_by_id(project_id)

List project

Return a single project

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectsApi()
project_id = 789 # int | ID of project to return

try:
    # List project
    api_response = api_instance.get_project_by_id(project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_project_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of project to return | 

### Return type

[**Projects**](Projects.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_tasks**
> list[Tasks] get_project_tasks(project_id)

List project tasks

Return project tasks

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectsApi()
project_id = 789 # int | ID of project to return tasklist from

try:
    # List project tasks
    api_response = api_instance.get_project_tasks(project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_project_tasks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of project to return tasklist from | 

### Return type

[**list[Tasks]**](Tasks.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_team_members**
> list[TeamMembers] get_project_team_members(project_id)

List project team members

Return project team members

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectsApi()
project_id = 789 # int | ID of project to return team members from

try:
    # List project team members
    api_response = api_instance.get_project_team_members(project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_project_team_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of project to return team members from | 

### Return type

[**list[TeamMembers]**](TeamMembers.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_by_id**
> Tasks get_task_by_id(project_id, task_id)

List task

Return a single task

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectsApi()
project_id = 789 # int | ID of project to get task from
task_id = 789 # int | ID of task to return

try:
    # List task
    api_response = api_instance.get_task_by_id(project_id, task_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_task_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of project to get task from | 
 **task_id** | **int**| ID of task to return | 

### Return type

[**Tasks**](Tasks.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_comments**
> list[Comments] get_task_comments(project_id, task_id)

List task comments

Return task comments

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectsApi()
project_id = 789 # int | ID of project
task_id = 789 # int | ID of task

try:
    # List task comments
    api_response = api_instance.get_task_comments(project_id, task_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_task_comments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of project | 
 **task_id** | **int**| ID of task | 

### Return type

[**list[Comments]**](Comments.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **overwrite_project_by_id**
> Projects overwrite_project_by_id(body, project_id)

Overwrite project with specified ID

Fully overwrite project with specified ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectsApi()
body = swagger_client.Projects() # Projects | 
project_id = 789 # int | ID of project to update

try:
    # Overwrite project with specified ID
    api_response = api_instance.overwrite_project_by_id(body, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->overwrite_project_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Projects**](Projects.md)|  | 
 **project_id** | **int**| ID of project to update | 

### Return type

[**Projects**](Projects.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **overwrite_task_by_id**
> Tasks overwrite_task_by_id(body, project_id, task_id)

Overwrite task with specified ID

Fully overwrite task with specified ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectsApi()
body = swagger_client.Tasks() # Tasks | 
project_id = 789 # int | ID of project to overvrite task
task_id = 789 # int | ID of task to update

try:
    # Overwrite task with specified ID
    api_response = api_instance.overwrite_task_by_id(body, project_id, task_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->overwrite_task_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Tasks**](Tasks.md)|  | 
 **project_id** | **int**| ID of project to overvrite task | 
 **task_id** | **int**| ID of task to update | 

### Return type

[**Tasks**](Tasks.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_get**
> list[Projects] projects_get()

List all projects

Returns all projects

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectsApi()

try:
    # List all projects
    api_response = api_instance.projects_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->projects_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Projects]**](Projects.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_task_comments**
> remove_task_comments(project_id, task_id, comment_id)

Delete task comment

Deletes task comment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectsApi()
project_id = 789 # int | ID of project
task_id = 789 # int | ID of task
comment_id = 789 # int | ID of comment

try:
    # Delete task comment
    api_instance.remove_task_comments(project_id, task_id, comment_id)
except ApiException as e:
    print("Exception when calling ProjectsApi->remove_task_comments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of project | 
 **task_id** | **int**| ID of task | 
 **comment_id** | **int**| ID of comment | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_team_member_from_project**
> remove_team_member_from_project(project_id, teammember_id)

Delete teammember from project

Adds new teammember and returns assigned ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProjectsApi()
project_id = 789 # int | ID of project to remove team member from
teammember_id = 789 # int | ID of project team member to remove

try:
    # Delete teammember from project
    api_instance.remove_team_member_from_project(project_id, teammember_id)
except ApiException as e:
    print("Exception when calling ProjectsApi->remove_team_member_from_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| ID of project to remove team member from | 
 **teammember_id** | **int**| ID of project team member to remove | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

