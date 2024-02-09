# swagger_client.TasksApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_task**](TasksApi.md#add_task) | **POST** /projects/{projectID}/tasks | Add new task
[**add_task_comments**](TasksApi.md#add_task_comments) | **POST** /projects/{projectID}/tasks/{taskID}/comments | Add task comment
[**delete_task_by_id**](TasksApi.md#delete_task_by_id) | **DELETE** /projects/{projectID}/tasks/{taskID} | Delete task with specified ID
[**get_project_tasks**](TasksApi.md#get_project_tasks) | **GET** /projects/{projectID}/tasks | List project tasks
[**get_task_by_id**](TasksApi.md#get_task_by_id) | **GET** /projects/{projectID}/tasks/{taskID} | List task
[**get_task_comments**](TasksApi.md#get_task_comments) | **GET** /projects/{projectID}/tasks/{taskID}/comments | List task comments
[**overwrite_task_by_id**](TasksApi.md#overwrite_task_by_id) | **PUT** /projects/{projectID}/tasks/{taskID} | Overwrite task with specified ID
[**remove_task_comments**](TasksApi.md#remove_task_comments) | **DELETE** /projects/{projectID}/tasks/{taskID}/comments/{commentID} | Delete task comment

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
api_instance = swagger_client.TasksApi()
body = swagger_client.Tasks() # Tasks | Create new task
project_id = 789 # int | ID of project to add task to

try:
    # Add new task
    api_response = api_instance.add_task(body, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->add_task: %s\n" % e)
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
api_instance = swagger_client.TasksApi()
body = swagger_client.Tasks() # Tasks | 
project_id = 789 # int | ID of project
task_id = 789 # int | ID of task

try:
    # Add task comment
    api_response = api_instance.add_task_comments(body, project_id, task_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->add_task_comments: %s\n" % e)
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
api_instance = swagger_client.TasksApi()
project_id = 789 # int | ID of project to delete task from
task_id = 789 # int | ID of task to delete

try:
    # Delete task with specified ID
    api_instance.delete_task_by_id(project_id, task_id)
except ApiException as e:
    print("Exception when calling TasksApi->delete_task_by_id: %s\n" % e)
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
api_instance = swagger_client.TasksApi()
project_id = 789 # int | ID of project to return tasklist from

try:
    # List project tasks
    api_response = api_instance.get_project_tasks(project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->get_project_tasks: %s\n" % e)
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
api_instance = swagger_client.TasksApi()
project_id = 789 # int | ID of project to get task from
task_id = 789 # int | ID of task to return

try:
    # List task
    api_response = api_instance.get_task_by_id(project_id, task_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->get_task_by_id: %s\n" % e)
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
api_instance = swagger_client.TasksApi()
project_id = 789 # int | ID of project
task_id = 789 # int | ID of task

try:
    # List task comments
    api_response = api_instance.get_task_comments(project_id, task_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->get_task_comments: %s\n" % e)
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
api_instance = swagger_client.TasksApi()
body = swagger_client.Tasks() # Tasks | 
project_id = 789 # int | ID of project to overvrite task
task_id = 789 # int | ID of task to update

try:
    # Overwrite task with specified ID
    api_response = api_instance.overwrite_task_by_id(body, project_id, task_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->overwrite_task_by_id: %s\n" % e)
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
api_instance = swagger_client.TasksApi()
project_id = 789 # int | ID of project
task_id = 789 # int | ID of task
comment_id = 789 # int | ID of comment

try:
    # Delete task comment
    api_instance.remove_task_comments(project_id, task_id, comment_id)
except ApiException as e:
    print("Exception when calling TasksApi->remove_task_comments: %s\n" % e)
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

