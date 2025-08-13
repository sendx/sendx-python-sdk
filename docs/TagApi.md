# sendx_python_sdk.TagApi

All URIs are relative to *https://api.sendx.io/api/v1/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tag**](TagApi.md#create_tag) | **POST** /tag | Create tag
[**delete_tag**](TagApi.md#delete_tag) | **DELETE** /tag/{identifier} | Delete tag
[**get_all_tags**](TagApi.md#get_all_tags) | **GET** /tag | Get all tags
[**get_tag**](TagApi.md#get_tag) | **GET** /tag/{identifier} | Get tag by ID
[**update_tag**](TagApi.md#update_tag) | **PUT** /tag/{identifier} | Update tag


# **create_tag**
> RestRTag create_tag(rest_e_tag)

Create tag

Creates a new tag for contact categorization.


### Example

* Api Key Authentication (TeamApiKey):

```python
import sendx_python_sdk
from sendx_python_sdk.models.rest_e_tag import RestETag
from sendx_python_sdk.models.rest_r_tag import RestRTag
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
    api_instance = sendx_python_sdk.TagApi(api_client)
    rest_e_tag = {"name":"VIP Customer"} # RestETag | 

    try:
        # Create tag
        api_response = api_instance.create_tag(rest_e_tag)
        print("The response of TagApi->create_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagApi->create_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rest_e_tag** | [**RestETag**](RestETag.md)|  | 

### Return type

[**RestRTag**](RestRTag.md)

### Authorization

[TeamApiKey](../README.md#TeamApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | ✅ Tag created successfully |  -  |
**401** | ❌ Unauthorized - Invalid or missing API key |  -  |
**403** | ❌ Forbidden - Resource name already exists |  -  |
**422** | ❌ Unprocessable Entity - Invalid request format |  -  |
**500** | ❌ Internal Server Error - System error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tag**
> DeleteResponse delete_tag(identifier)

Delete tag

Deletes a tag from the system.


### Example

* Api Key Authentication (TeamApiKey):

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

# Configure API key authorization: TeamApiKey
configuration.api_key['TeamApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TeamApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with sendx_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sendx_python_sdk.TagApi(api_client)
    identifier = 'identifier_example' # str | Tag identifier to update

    try:
        # Delete tag
        api_response = api_instance.delete_tag(identifier)
        print("The response of TagApi->delete_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagApi->delete_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Tag identifier to update | 

### Return type

[**DeleteResponse**](DeleteResponse.md)

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
**422** | ❌ Unprocessable Entity - Invalid request format |  -  |
**500** | ❌ Internal Server Error - System error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_tags**
> List[RestRTag] get_all_tags(offset=offset, limit=limit)

Get all tags

Retrieves all tags in your team.


### Example

* Api Key Authentication (TeamApiKey):

```python
import sendx_python_sdk
from sendx_python_sdk.models.rest_r_tag import RestRTag
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
    api_instance = sendx_python_sdk.TagApi(api_client)
    offset = 0 # int | Number of tags to skip (optional) (default to 0)
    limit = 10 # int | Maximum number of tags to return (optional) (default to 10)

    try:
        # Get all tags
        api_response = api_instance.get_all_tags(offset=offset, limit=limit)
        print("The response of TagApi->get_all_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagApi->get_all_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| Number of tags to skip | [optional] [default to 0]
 **limit** | **int**| Maximum number of tags to return | [optional] [default to 10]

### Return type

[**List[RestRTag]**](RestRTag.md)

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

# **get_tag**
> RestRTag get_tag(identifier)

Get tag by ID

Retrieves detailed information about a specific tag.


### Example

* Api Key Authentication (TeamApiKey):

```python
import sendx_python_sdk
from sendx_python_sdk.models.rest_r_tag import RestRTag
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
    api_instance = sendx_python_sdk.TagApi(api_client)
    identifier = 'identifier_example' # str | Tag identifier to retrieve

    try:
        # Get tag by ID
        api_response = api_instance.get_tag(identifier)
        print("The response of TagApi->get_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagApi->get_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Tag identifier to retrieve | 

### Return type

[**RestRTag**](RestRTag.md)

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
**422** | ❌ Unprocessable Entity - Invalid request format |  -  |
**500** | ❌ Internal Server Error - System error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tag**
> RestRTag update_tag(identifier, rest_e_tag)

Update tag

Updates an existing tag's name.


### Example

* Api Key Authentication (TeamApiKey):

```python
import sendx_python_sdk
from sendx_python_sdk.models.rest_e_tag import RestETag
from sendx_python_sdk.models.rest_r_tag import RestRTag
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
    api_instance = sendx_python_sdk.TagApi(api_client)
    identifier = 'identifier_example' # str | Tag identifier to update
    rest_e_tag = sendx_python_sdk.RestETag() # RestETag | 

    try:
        # Update tag
        api_response = api_instance.update_tag(identifier, rest_e_tag)
        print("The response of TagApi->update_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagApi->update_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Tag identifier to update | 
 **rest_e_tag** | [**RestETag**](RestETag.md)|  | 

### Return type

[**RestRTag**](RestRTag.md)

### Authorization

[TeamApiKey](../README.md#TeamApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ✅ Tag updated successfully |  -  |
**401** | ❌ Unauthorized - Invalid or missing API key |  -  |
**403** | ❌ Forbidden - Resource name already exists |  -  |
**404** | ❌ Not Found - Resource does not exist |  -  |
**422** | ❌ Unprocessable Entity - Invalid request format |  -  |
**500** | ❌ Internal Server Error - System error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

