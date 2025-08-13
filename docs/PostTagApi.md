# sendx_python_sdk.PostTagApi

All URIs are relative to *https://api.sendx.io/api/v1/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_post_tag**](PostTagApi.md#create_post_tag) | **POST** /post/tag | Create post tag
[**delete_post_tag**](PostTagApi.md#delete_post_tag) | **DELETE** /post/tag/{identifier} | Delete post tag
[**get_all_post_tags**](PostTagApi.md#get_all_post_tags) | **GET** /post/tag | Get all post tags
[**get_post_tag**](PostTagApi.md#get_post_tag) | **GET** /post/tag/{identifier} | Get post tag by ID
[**update_post_tag**](PostTagApi.md#update_post_tag) | **PUT** /post/tag/{identifier} | Update post tag


# **create_post_tag**
> RestRPostTag create_post_tag(rest_e_post_tag)

Create post tag

Creates a new tag for blog posts.


### Example

* Api Key Authentication (TeamApiKey):

```python
import sendx_python_sdk
from sendx_python_sdk.models.rest_e_post_tag import RestEPostTag
from sendx_python_sdk.models.rest_r_post_tag import RestRPostTag
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
    api_instance = sendx_python_sdk.PostTagApi(api_client)
    rest_e_post_tag = sendx_python_sdk.RestEPostTag() # RestEPostTag | 

    try:
        # Create post tag
        api_response = api_instance.create_post_tag(rest_e_post_tag)
        print("The response of PostTagApi->create_post_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostTagApi->create_post_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rest_e_post_tag** | [**RestEPostTag**](RestEPostTag.md)|  | 

### Return type

[**RestRPostTag**](RestRPostTag.md)

### Authorization

[TeamApiKey](../README.md#TeamApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | ✅ Tag created successfully |  -  |
**400** | ❌ Bad Request - Invalid input data |  -  |
**401** | ❌ Unauthorized - Invalid or missing API key |  -  |
**403** | ❌ Forbidden - Resource name already exists |  -  |
**422** | ❌ Unprocessable Entity - Invalid request format |  -  |
**500** | ❌ Internal Server Error - System error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_post_tag**
> MessageResponse delete_post_tag(identifier)

Delete post tag

Soft deletes a post tag.


### Example

* Api Key Authentication (TeamApiKey):

```python
import sendx_python_sdk
from sendx_python_sdk.models.message_response import MessageResponse
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
    api_instance = sendx_python_sdk.PostTagApi(api_client)
    identifier = 'post_tag_leBDiFdrUnRmRz4nfopSrv' # str | The unique post tag identifier to retrieve. - `post_tag_leBDiFdrUnRmRz4nfopSrv` 

    try:
        # Delete post tag
        api_response = api_instance.delete_post_tag(identifier)
        print("The response of PostTagApi->delete_post_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostTagApi->delete_post_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| The unique post tag identifier to retrieve. - &#x60;post_tag_leBDiFdrUnRmRz4nfopSrv&#x60;  | 

### Return type

[**MessageResponse**](MessageResponse.md)

### Authorization

[TeamApiKey](../README.md#TeamApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ✅ Tag deleted successfully |  -  |
**401** | ❌ Unauthorized - Invalid or missing API key |  -  |
**404** | ❌ Not Found - Resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_post_tags**
> List[RestRPostTag] get_all_post_tags()

Get all post tags

Retrieves all blog post tags.


### Example

* Api Key Authentication (TeamApiKey):

```python
import sendx_python_sdk
from sendx_python_sdk.models.rest_r_post_tag import RestRPostTag
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
    api_instance = sendx_python_sdk.PostTagApi(api_client)

    try:
        # Get all post tags
        api_response = api_instance.get_all_post_tags()
        print("The response of PostTagApi->get_all_post_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostTagApi->get_all_post_tags: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[RestRPostTag]**](RestRPostTag.md)

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
**500** | ❌ Internal Server Error - System error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_post_tag**
> RestRPostTag get_post_tag(identifier)

Get post tag by ID

Retrieves a specific post tag.


### Example

* Api Key Authentication (TeamApiKey):

```python
import sendx_python_sdk
from sendx_python_sdk.models.rest_r_post_tag import RestRPostTag
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
    api_instance = sendx_python_sdk.PostTagApi(api_client)
    identifier = 'post_tag_leBDiFdrUnRmRz4nfopSrv' # str | The unique post tag identifier to retrieve. - `post_tag_leBDiFdrUnRmRz4nfopSrv` 

    try:
        # Get post tag by ID
        api_response = api_instance.get_post_tag(identifier)
        print("The response of PostTagApi->get_post_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostTagApi->get_post_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| The unique post tag identifier to retrieve. - &#x60;post_tag_leBDiFdrUnRmRz4nfopSrv&#x60;  | 

### Return type

[**RestRPostTag**](RestRPostTag.md)

### Authorization

[TeamApiKey](../README.md#TeamApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ✅ Tag retrieved successfully |  -  |
**401** | ❌ Unauthorized - Invalid or missing API key |  -  |
**404** | ❌ Not Found - Resource does not exist |  -  |
**500** | ❌ Internal Server Error - System error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_post_tag**
> RestRPostTag update_post_tag(identifier, rest_e_post_tag)

Update post tag

Updates a post tag.


### Example

* Api Key Authentication (TeamApiKey):

```python
import sendx_python_sdk
from sendx_python_sdk.models.rest_e_post_tag import RestEPostTag
from sendx_python_sdk.models.rest_r_post_tag import RestRPostTag
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
    api_instance = sendx_python_sdk.PostTagApi(api_client)
    identifier = 'post_tag_leBDiFdrUnRmRz4nfopSrv' # str | The unique post tag identifier to retrieve. - `post_tag_leBDiFdrUnRmRz4nfopSrv` 
    rest_e_post_tag = sendx_python_sdk.RestEPostTag() # RestEPostTag | 

    try:
        # Update post tag
        api_response = api_instance.update_post_tag(identifier, rest_e_post_tag)
        print("The response of PostTagApi->update_post_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostTagApi->update_post_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| The unique post tag identifier to retrieve. - &#x60;post_tag_leBDiFdrUnRmRz4nfopSrv&#x60;  | 
 **rest_e_post_tag** | [**RestEPostTag**](RestEPostTag.md)|  | 

### Return type

[**RestRPostTag**](RestRPostTag.md)

### Authorization

[TeamApiKey](../README.md#TeamApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ✅ Tag updated successfully |  -  |
**400** | ❌ Bad Request - Invalid input data |  -  |
**401** | ❌ Unauthorized - Invalid or missing API key |  -  |
**404** | ❌ Not Found - Resource does not exist |  -  |
**409** | ❌ Conflict - Resource already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

