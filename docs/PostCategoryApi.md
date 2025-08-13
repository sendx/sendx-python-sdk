# sendx_python_sdk.PostCategoryApi

All URIs are relative to *https://api.sendx.io/api/v1/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_post_category**](PostCategoryApi.md#create_post_category) | **POST** /post/category | Create post category
[**delete_post_category**](PostCategoryApi.md#delete_post_category) | **DELETE** /post/category/{identifier} | Delete post category
[**get_all_post_categories**](PostCategoryApi.md#get_all_post_categories) | **GET** /post/category | Get all post categories
[**get_post_category**](PostCategoryApi.md#get_post_category) | **GET** /post/category/{identifier} | Get post category by ID
[**update_post_category**](PostCategoryApi.md#update_post_category) | **PUT** /post/category/{identifier} | Update post category


# **create_post_category**
> RestRPostCategory create_post_category(rest_e_post_category)

Create post category

Creates a new category for organizing blog posts.


### Example

* Api Key Authentication (TeamApiKey):

```python
import sendx_python_sdk
from sendx_python_sdk.models.rest_e_post_category import RestEPostCategory
from sendx_python_sdk.models.rest_r_post_category import RestRPostCategory
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
    api_instance = sendx_python_sdk.PostCategoryApi(api_client)
    rest_e_post_category = {"name":"Product Updates"} # RestEPostCategory | 

    try:
        # Create post category
        api_response = api_instance.create_post_category(rest_e_post_category)
        print("The response of PostCategoryApi->create_post_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostCategoryApi->create_post_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rest_e_post_category** | [**RestEPostCategory**](RestEPostCategory.md)|  | 

### Return type

[**RestRPostCategory**](RestRPostCategory.md)

### Authorization

[TeamApiKey](../README.md#TeamApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | ✅ Category created successfully |  -  |
**400** | ❌ Bad Request - Invalid input data |  -  |
**401** | ❌ Unauthorized - Invalid or missing API key |  -  |
**409** | ❌ Conflict - Resource already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_post_category**
> MessageResponse delete_post_category(identifier)

Delete post category

Soft deletes a post category.


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
    api_instance = sendx_python_sdk.PostCategoryApi(api_client)
    identifier = 'post_category_YzS1wOU20yw87UUHKxMzwn' # str | The unique post category identifier to retrieve. - `post_category_YzS1wOU20yw87UUHKxMzwn` 

    try:
        # Delete post category
        api_response = api_instance.delete_post_category(identifier)
        print("The response of PostCategoryApi->delete_post_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostCategoryApi->delete_post_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| The unique post category identifier to retrieve. - &#x60;post_category_YzS1wOU20yw87UUHKxMzwn&#x60;  | 

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
**200** | ✅ Category deleted successfully |  -  |
**401** | ❌ Unauthorized - Invalid or missing API key |  -  |
**404** | ❌ Not Found - Resource does not exist |  -  |
**500** | ❌ Internal Server Error - System error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_post_categories**
> List[RestRPostCategory] get_all_post_categories()

Get all post categories

Retrieves all blog post categories.


### Example

* Api Key Authentication (TeamApiKey):

```python
import sendx_python_sdk
from sendx_python_sdk.models.rest_r_post_category import RestRPostCategory
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
    api_instance = sendx_python_sdk.PostCategoryApi(api_client)

    try:
        # Get all post categories
        api_response = api_instance.get_all_post_categories()
        print("The response of PostCategoryApi->get_all_post_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostCategoryApi->get_all_post_categories: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[RestRPostCategory]**](RestRPostCategory.md)

### Authorization

[TeamApiKey](../README.md#TeamApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ✅ Categories retrieved successfully |  -  |
**401** | ❌ Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_post_category**
> RestRPostCategory get_post_category(identifier)

Get post category by ID

Retrieves a specific post category.


### Example

* Api Key Authentication (TeamApiKey):

```python
import sendx_python_sdk
from sendx_python_sdk.models.rest_r_post_category import RestRPostCategory
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
    api_instance = sendx_python_sdk.PostCategoryApi(api_client)
    identifier = 'post_category_YzS1wOU20yw87UUHKxMzwn' # str | The unique post category identifier to retrieve. - `post_category_YzS1wOU20yw87UUHKxMzwn` 

    try:
        # Get post category by ID
        api_response = api_instance.get_post_category(identifier)
        print("The response of PostCategoryApi->get_post_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostCategoryApi->get_post_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| The unique post category identifier to retrieve. - &#x60;post_category_YzS1wOU20yw87UUHKxMzwn&#x60;  | 

### Return type

[**RestRPostCategory**](RestRPostCategory.md)

### Authorization

[TeamApiKey](../README.md#TeamApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ✅ Category retrieved successfully |  -  |
**401** | ❌ Unauthorized - Invalid or missing API key |  -  |
**404** | ❌ Not Found - Resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_post_category**
> RestRPostCategory update_post_category(identifier, rest_e_post_category)

Update post category

Updates a post category.


### Example

* Api Key Authentication (TeamApiKey):

```python
import sendx_python_sdk
from sendx_python_sdk.models.rest_e_post_category import RestEPostCategory
from sendx_python_sdk.models.rest_r_post_category import RestRPostCategory
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
    api_instance = sendx_python_sdk.PostCategoryApi(api_client)
    identifier = 'post_category_YzS1wOU20yw87UUHKxMzwn' # str | The unique post category identifier to retrieve. - `post_category_YzS1wOU20yw87UUHKxMzwn` 
    rest_e_post_category = sendx_python_sdk.RestEPostCategory() # RestEPostCategory | 

    try:
        # Update post category
        api_response = api_instance.update_post_category(identifier, rest_e_post_category)
        print("The response of PostCategoryApi->update_post_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostCategoryApi->update_post_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| The unique post category identifier to retrieve. - &#x60;post_category_YzS1wOU20yw87UUHKxMzwn&#x60;  | 
 **rest_e_post_category** | [**RestEPostCategory**](RestEPostCategory.md)|  | 

### Return type

[**RestRPostCategory**](RestRPostCategory.md)

### Authorization

[TeamApiKey](../README.md#TeamApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ✅ Category updated successfully |  -  |
**400** | ❌ Bad Request - Invalid input data |  -  |
**401** | ❌ Unauthorized - Invalid or missing API key |  -  |
**404** | ❌ Not Found - Resource does not exist |  -  |
**422** | ❌ Unprocessable Entity - Invalid request format |  -  |
**500** | ❌ Internal Server Error - System error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

