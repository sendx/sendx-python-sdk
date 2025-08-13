# sendx_python_sdk.TeamMemberApi

All URIs are relative to *https://api.sendx.io/api/v1/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_team_members**](TeamMemberApi.md#get_all_team_members) | **GET** /team/member | Get all team members
[**get_team_member**](TeamMemberApi.md#get_team_member) | **GET** /team/member/{identifier} | Get a team member by ID


# **get_all_team_members**
> List[RestRMember] get_all_team_members()

Get all team members

Retrieves all team members.

### Example

* Api Key Authentication (TeamApiKey):

```python
import sendx_python_sdk
from sendx_python_sdk.models.rest_r_member import RestRMember
from sendx_python_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.sendx.io/api/v1/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = sendx_python_sdk.Configuration(
    host = "https://api.sendx.io/api/v1/rest"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TeamApiKey
configuration.api_key['TeamApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TeamApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with sendx_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sendx_python_sdk.TeamMemberApi(api_client)

    try:
        # Get all team members
        api_response = api_instance.get_all_team_members()
        print("The response of TeamMemberApi->get_all_team_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamMemberApi->get_all_team_members: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[RestRMember]**](RestRMember.md)

### Authorization

[TeamApiKey](../README.md#TeamApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ✅ Tags retrieved successfully |  -  |
**401** | ❌ Unauthorized - Invalid or missing API key |  -  |
**404** | ❌ Not Found - Resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team_member**
> RestRMember get_team_member(identifier)

Get a team member by ID

Retrieves a single team member by their unique identifier.

### Example

* Api Key Authentication (TeamApiKey):

```python
import sendx_python_sdk
from sendx_python_sdk.models.rest_r_member import RestRMember
from sendx_python_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.sendx.io/api/v1/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = sendx_python_sdk.Configuration(
    host = "https://api.sendx.io/api/v1/rest"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TeamApiKey
configuration.api_key['TeamApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TeamApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with sendx_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sendx_python_sdk.TeamMemberApi(api_client)
    identifier = 'contact_BnKjkbBBS500CoBCP0oChQ' # str | Resource identifier with prefix (e.g., `contact_BnKjkbBBS500CoBCP0oChQ`)  **Format:** `<prefix>_<22-character-id>` 

    try:
        # Get a team member by ID
        api_response = api_instance.get_team_member(identifier)
        print("The response of TeamMemberApi->get_team_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamMemberApi->get_team_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Resource identifier with prefix (e.g., &#x60;contact_BnKjkbBBS500CoBCP0oChQ&#x60;)  **Format:** &#x60;&lt;prefix&gt;_&lt;22-character-id&gt;&#x60;  | 

### Return type

[**RestRMember**](RestRMember.md)

### Authorization

[TeamApiKey](../README.md#TeamApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ✅ Team member retrieved successfully |  -  |
**401** | ❌ Unauthorized - Invalid or missing API key |  -  |
**404** | ❌ Not Found - Resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

