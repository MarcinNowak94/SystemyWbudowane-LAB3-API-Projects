# swagger_client.TeamMembersApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_team_member_to_project**](TeamMembersApi.md#add_team_member_to_project) | **POST** /projects/{projectID}/team-members | Add new teammember to project
[**get_project_team_members**](TeamMembersApi.md#get_project_team_members) | **GET** /projects/{projectID}/team-members | List project team members
[**remove_team_member_from_project**](TeamMembersApi.md#remove_team_member_from_project) | **DELETE** /projects/{projectID}/team-members/{teammemberID} | Delete teammember from project

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
api_instance = swagger_client.TeamMembersApi()
body = swagger_client.TeamMembers() # TeamMembers | Create new teammember
project_id = 789 # int | ID of project to add team members to

try:
    # Add new teammember to project
    api_response = api_instance.add_team_member_to_project(body, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMembersApi->add_team_member_to_project: %s\n" % e)
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
api_instance = swagger_client.TeamMembersApi()
project_id = 789 # int | ID of project to return team members from

try:
    # List project team members
    api_response = api_instance.get_project_team_members(project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamMembersApi->get_project_team_members: %s\n" % e)
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
api_instance = swagger_client.TeamMembersApi()
project_id = 789 # int | ID of project to remove team member from
teammember_id = 789 # int | ID of project team member to remove

try:
    # Delete teammember from project
    api_instance.remove_team_member_from_project(project_id, teammember_id)
except ApiException as e:
    print("Exception when calling TeamMembersApi->remove_team_member_from_project: %s\n" % e)
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

