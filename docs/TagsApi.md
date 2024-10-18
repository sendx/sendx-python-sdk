# sendx_python_sdk.TagsApi

All URIs are relative to *https://api.sendx.io/api/v1/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tag**](TagsApi.md#create_tag) | **POST** /tag | Create a Tag
[**delete_tag**](TagsApi.md#delete_tag) | **DELETE** /tag/{tagId} | Delete a Tag
[**get_all_tags**](TagsApi.md#get_all_tags) | **GET** /tag | Get All Tags
[**get_tag_by_id**](TagsApi.md#get_tag_by_id) | **GET** /tag/{tagId} | Get a Tag by ID
[**update_tag**](TagsApi.md#update_tag) | **PUT** /tag/{tagId} | Update a Tag


# **create_tag**
> CreateResponse create_tag(tag_request)

Create a Tag

Create a new tag for the account

### Example

* Api Key Authentication (apiKeyAuth):

```python
import sendx_python_sdk
from sendx_python_sdk.models.create_response import CreateResponse
from sendx_python_sdk.models.tag_request import TagRequest
from sendx_python_sdk.rest import ApiException
from pprint import pprint


configuration = sendx_python_sdk.Configuration()



# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.environ["API_KEY"]



# Enter a context with an instance of the API client
with sendx_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sendx_python_sdk.TagsApi(api_client)
    tag_request = sendx_python_sdk.TagRequest() # TagRequest | The tag content

    try:
        # Create a Tag
        api_response = api_instance.create_tag(tag_request)
        print("The response of TagsApi->create_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagsApi->create_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_request** | [**TagRequest**](TagRequest.md)| The tag content | 

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
**200** | Tag created successfully |  -  |
**401** | Not Authorized |  -  |
**403** | Forbidden - Tag with this name already exists |  -  |
**406** | Not Acceptable |  -  |
**422** | Request body is not in proper format |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tag**
> DeleteResponse delete_tag(tag_id)

Delete a Tag

Delete an existing tag by ID

### Example

* Api Key Authentication (apiKeyAuth):

```python
import sendx_python_sdk
from sendx_python_sdk.models.delete_response import DeleteResponse
from sendx_python_sdk.rest import ApiException
from pprint import pprint


configuration = sendx_python_sdk.Configuration()



# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.environ["API_KEY"]



# Enter a context with an instance of the API client
with sendx_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sendx_python_sdk.TagsApi(api_client)
    tag_id = 'tag_id_example' # str | ID of the tag to delete

    try:
        # Delete a Tag
        api_response = api_instance.delete_tag(tag_id)
        print("The response of TagsApi->delete_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagsApi->delete_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_id** | **str**| ID of the tag to delete | 

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
**200** | Tag deleted successfully |  -  |
**401** | Not Authorized |  -  |
**406** | Tag ID is empty |  -  |
**422** | Request body is not in proper format |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_tags**
> List[Tag] get_all_tags(offset=offset, limit=limit, search=search)

Get All Tags

Retrieve all tags for the account with optional pagination and search filters

### Example

* Api Key Authentication (apiKeyAuth):

```python
import sendx_python_sdk
from sendx_python_sdk.models.tag import Tag
from sendx_python_sdk.rest import ApiException
from pprint import pprint


configuration = sendx_python_sdk.Configuration()



# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.environ["API_KEY"]



# Enter a context with an instance of the API client
with sendx_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sendx_python_sdk.TagsApi(api_client)
    offset = 56 # int | Offset for pagination (optional)
    limit = 56 # int | Limit the number of results (optional)
    search = 'search_example' # str | Search term to filter tags (optional)

    try:
        # Get All Tags
        api_response = api_instance.get_all_tags(offset=offset, limit=limit, search=search)
        print("The response of TagsApi->get_all_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagsApi->get_all_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| Offset for pagination | [optional] 
 **limit** | **int**| Limit the number of results | [optional] 
 **search** | **str**| Search term to filter tags | [optional] 

### Return type

[**List[Tag]**](Tag.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieved all tags successfully |  -  |
**401** | Not Authorized |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tag_by_id**
> Tag get_tag_by_id(tag_id)

Get a Tag by ID

Retrieve a tag based on the provided tag ID

### Example

* Api Key Authentication (apiKeyAuth):

```python
import sendx_python_sdk
from sendx_python_sdk.models.tag import Tag
from sendx_python_sdk.rest import ApiException
from pprint import pprint


configuration = sendx_python_sdk.Configuration()



# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.environ["API_KEY"]



# Enter a context with an instance of the API client
with sendx_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sendx_python_sdk.TagsApi(api_client)
    tag_id = 'tag_id_example' # str | ID of the tag you want to fetch

    try:
        # Get a Tag by ID
        api_response = api_instance.get_tag_by_id(tag_id)
        print("The response of TagsApi->get_tag_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagsApi->get_tag_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_id** | **str**| ID of the tag you want to fetch | 

### Return type

[**Tag**](Tag.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response with the tag details |  -  |
**401** | Not Authorized |  -  |
**403** | Forbidden - Tag with the same name already exists |  -  |
**406** | Not Acceptable |  -  |
**422** | Request body is not in proper format |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tag**
> Response update_tag(tag_id, tag_request)

Update a Tag

Update an existing tag

### Example

* Api Key Authentication (apiKeyAuth):

```python
import sendx_python_sdk
from sendx_python_sdk.models.response import Response
from sendx_python_sdk.models.tag_request import TagRequest
from sendx_python_sdk.rest import ApiException
from pprint import pprint


configuration = sendx_python_sdk.Configuration()



# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.environ["API_KEY"]



# Enter a context with an instance of the API client
with sendx_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sendx_python_sdk.TagsApi(api_client)
    tag_id = 'tag_id_example' # str | ID of the tag to update
    tag_request = sendx_python_sdk.TagRequest() # TagRequest | The tag content

    try:
        # Update a Tag
        api_response = api_instance.update_tag(tag_id, tag_request)
        print("The response of TagsApi->update_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagsApi->update_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_id** | **str**| ID of the tag to update | 
 **tag_request** | [**TagRequest**](TagRequest.md)| The tag content | 

### Return type

[**Response**](Response.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tag updated successfully |  -  |
**401** | Not Authorized |  -  |
**403** | Forbidden - Tag with this name already exists |  -  |
**406** | Not Acceptable |  -  |
**422** | Request body is not in proper format |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

