# swagger_client.CommentsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_task_comments**](CommentsApi.md#add_task_comments) | **POST** /projects/{projectID}/tasks/{taskID}/comments | Add task comment
[**get_task_comments**](CommentsApi.md#get_task_comments) | **GET** /projects/{projectID}/tasks/{taskID}/comments | List task comments
[**remove_task_comments**](CommentsApi.md#remove_task_comments) | **DELETE** /projects/{projectID}/tasks/{taskID}/comments/{commentID} | Delete task comment

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
api_instance = swagger_client.CommentsApi()
body = swagger_client.Tasks() # Tasks | 
project_id = 789 # int | ID of project
task_id = 789 # int | ID of task

try:
    # Add task comment
    api_response = api_instance.add_task_comments(body, project_id, task_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommentsApi->add_task_comments: %s\n" % e)
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
api_instance = swagger_client.CommentsApi()
project_id = 789 # int | ID of project
task_id = 789 # int | ID of task

try:
    # List task comments
    api_response = api_instance.get_task_comments(project_id, task_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommentsApi->get_task_comments: %s\n" % e)
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
api_instance = swagger_client.CommentsApi()
project_id = 789 # int | ID of project
task_id = 789 # int | ID of task
comment_id = 789 # int | ID of comment

try:
    # Delete task comment
    api_instance.remove_task_comments(project_id, task_id, comment_id)
except ApiException as e:
    print("Exception when calling CommentsApi->remove_task_comments: %s\n" % e)
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

