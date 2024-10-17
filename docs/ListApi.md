# sendx_python_sdk.ListApi

All URIs are relative to *https://api.sendx.io/api/v1/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_list**](ListApi.md#create_list) | **POST** /list | Create List
[**delete_list**](ListApi.md#delete_list) | **DELETE** /list/{listId} | Delete List
[**get_all_lists**](ListApi.md#get_all_lists) | **GET** /list | Get All Lists
[**get_list_by_id**](ListApi.md#get_list_by_id) | **GET** /list/{listId} | Get List
[**update_list**](ListApi.md#update_list) | **PUT** /list/{listId} | Update List


# **create_list**
> CreateResponse create_list(list_request)

Create List

Create a new list.

### Example

* Api Key Authentication (apiKeyAuth):

```python
import sendx_python_sdk
from sendx_python_sdk.models.create_response import CreateResponse
from sendx_python_sdk.models.list_request import ListRequest
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

# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with sendx_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sendx_python_sdk.ListApi(api_client)
    list_request = sendx_python_sdk.ListRequest() # ListRequest | 

    try:
        # Create List
        api_response = api_instance.create_list(list_request)
        print("The response of ListApi->create_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListApi->create_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_request** | [**ListRequest**](ListRequest.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List Created Successfully |  -  |
**401** | Not Authorized |  -  |
**403** | Forbidden - Tag with name already exists |  -  |
**406** | Not Acceptable |  -  |
**422** | Request body is not in proper format |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_list**
> DeleteResponse delete_list(list_id)

Delete List

Deletes a specific list by its ID.

### Example

* Api Key Authentication (apiKeyAuth):

```python
import sendx_python_sdk
from sendx_python_sdk.models.delete_response import DeleteResponse
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

# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with sendx_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sendx_python_sdk.ListApi(api_client)
    list_id = 'sendx123' # str | The ID of the list you want to delete

    try:
        # Delete List
        api_response = api_instance.delete_list(list_id)
        print("The response of ListApi->delete_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListApi->delete_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **str**| The ID of the list you want to delete | 

### Return type

[**DeleteResponse**](DeleteResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List deleted successfully |  -  |
**401** | Not Authorized |  -  |
**406** | listId is empty |  -  |
**422** | Request body is not in proper format |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_lists**
> List[ListModel] get_all_lists(offset=offset, limit=limit, search=search)

Get All Lists

Retrieve all lists for the account.

### Example

* Api Key Authentication (apiKeyAuth):

```python
import sendx_python_sdk
from sendx_python_sdk.models.list_model import ListModel
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

# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with sendx_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sendx_python_sdk.ListApi(api_client)
    offset = 0 # int | Offset for pagination. (optional)
    limit = 10 # int | Limit the number of results returned. (optional)
    search = 'Marketing' # str | Search term to filter lists. (optional)

    try:
        # Get All Lists
        api_response = api_instance.get_all_lists(offset=offset, limit=limit, search=search)
        print("The response of ListApi->get_all_lists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListApi->get_all_lists: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| Offset for pagination. | [optional] 
 **limit** | **int**| Limit the number of results returned. | [optional] 
 **search** | **str**| Search term to filter lists. | [optional] 

### Return type

[**List[ListModel]**](ListModel.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieved all Lists for account successfully |  -  |
**401** | Not Authorized |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_by_id**
> ListModel get_list_by_id(list_id)

Get List

Retrieve a specific list by its ID.

### Example

* Api Key Authentication (apiKeyAuth):

```python
import sendx_python_sdk
from sendx_python_sdk.models.list_model import ListModel
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

# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with sendx_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sendx_python_sdk.ListApi(api_client)
    list_id = 'sendx123' # str | The ID of the list you want to retrieve

    try:
        # Get List
        api_response = api_instance.get_list_by_id(list_id)
        print("The response of ListApi->get_list_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListApi->get_list_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **str**| The ID of the list you want to retrieve | 

### Return type

[**ListModel**](ListModel.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved the list |  -  |
**401** | Not Authorized |  -  |
**406** | Not Acceptable |  -  |
**403** | Forbidden Tag with name already exists |  -  |
**422** | Request body is not in proper format |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_list**
> ListModel update_list(list_id, list_request)

Update List

Update an existing list by its ID.

### Example

* Api Key Authentication (apiKeyAuth):

```python
import sendx_python_sdk
from sendx_python_sdk.models.list_model import ListModel
from sendx_python_sdk.models.list_request import ListRequest
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

# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with sendx_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sendx_python_sdk.ListApi(api_client)
    list_id = 'list_id_example' # str | The ID of the list to be updated.
    list_request = sendx_python_sdk.ListRequest() # ListRequest | 

    try:
        # Update List
        api_response = api_instance.update_list(list_id, list_request)
        print("The response of ListApi->update_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ListApi->update_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **str**| The ID of the list to be updated. | 
 **list_request** | [**ListRequest**](ListRequest.md)|  | 

### Return type

[**ListModel**](ListModel.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List Updated Successfully |  -  |
**401** | Not Authorized |  -  |
**403** | Forbidden - Tag with name already exists |  -  |
**406** | Not Acceptable |  -  |
**422** | Request body is not in proper format |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

