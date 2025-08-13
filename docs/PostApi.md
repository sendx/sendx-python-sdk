# sendx_python_sdk.PostApi

All URIs are relative to *https://api.sendx.io/api/v1/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_post**](PostApi.md#create_post) | **POST** /post | Create blog post
[**delete_post**](PostApi.md#delete_post) | **DELETE** /post/{identifier} | Delete post
[**get_all_posts**](PostApi.md#get_all_posts) | **GET** /post | Get all posts
[**get_post**](PostApi.md#get_post) | **GET** /post/{identifier} | Get post by ID
[**update_post**](PostApi.md#update_post) | **PUT** /post/{identifier} | Update post


# **create_post**
> RestRPost create_post(rest_e_post)

Create blog post

Creates a new blog post.


### Example

* Api Key Authentication (TeamApiKey):

```python
import sendx_python_sdk
from sendx_python_sdk.models.rest_e_post import RestEPost
from sendx_python_sdk.models.rest_r_post import RestRPost
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
    api_instance = sendx_python_sdk.PostApi(api_client)
    rest_e_post = {"name":"launch_draft_2025","postTitle":"Upcoming Product Launch"} # RestEPost | 

    try:
        # Create blog post
        api_response = api_instance.create_post(rest_e_post)
        print("The response of PostApi->create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostApi->create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rest_e_post** | [**RestEPost**](RestEPost.md)|  | 

### Return type

[**RestRPost**](RestRPost.md)

### Authorization

[TeamApiKey](../README.md#TeamApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | ✅ Post created successfully |  -  |
**400** | ❌ Bad Request - Invalid input data |  -  |
**401** | ❌ Unauthorized - Invalid or missing API key |  -  |
**409** | ❌ Conflict - Resource already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_post**
> MessageResponse delete_post(identifier)

Delete post

Soft deletes a blog post.

**🎯 Key Features:**
- Soft delete
- Preserve data
- Remove from listings


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
    api_instance = sendx_python_sdk.PostApi(api_client)
    identifier = 'contact_BnKjkbBBS500CoBCP0oChQ' # str | Resource identifier with prefix (e.g., `contact_BnKjkbBBS500CoBCP0oChQ`)  **Format:** `<prefix>_<22-character-id>` 

    try:
        # Delete post
        api_response = api_instance.delete_post(identifier)
        print("The response of PostApi->delete_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostApi->delete_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Resource identifier with prefix (e.g., &#x60;contact_BnKjkbBBS500CoBCP0oChQ&#x60;)  **Format:** &#x60;&lt;prefix&gt;_&lt;22-character-id&gt;&#x60;  | 

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
**200** | ✅ Post deleted successfully |  -  |
**401** | ❌ Unauthorized - Invalid or missing API key |  -  |
**404** | ❌ Not Found - Resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_posts**
> List[RestRPost] get_all_posts(offset=offset, limit=limit)

Get all posts

Retrieves all blog posts with pagination.

**🎯 Key Features:**
- Filter by status
- Search functionality
- Sort options
- Include metadata


### Example

* Api Key Authentication (TeamApiKey):

```python
import sendx_python_sdk
from sendx_python_sdk.models.rest_r_post import RestRPost
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
    api_instance = sendx_python_sdk.PostApi(api_client)
    offset = 0 # int | Number of posts to skip (optional) (default to 0)
    limit = 10 # int | Maximum number of posts to return (optional) (default to 10)

    try:
        # Get all posts
        api_response = api_instance.get_all_posts(offset=offset, limit=limit)
        print("The response of PostApi->get_all_posts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostApi->get_all_posts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| Number of posts to skip | [optional] [default to 0]
 **limit** | **int**| Maximum number of posts to return | [optional] [default to 10]

### Return type

[**List[RestRPost]**](RestRPost.md)

### Authorization

[TeamApiKey](../README.md#TeamApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ✅ Posts retrieved successfully |  -  |
**401** | ❌ Unauthorized - Invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_post**
> RestRPost get_post(identifier)

Get post by ID

Retrieves a specific blog post.

**🎯 Key Features:**
- Full post content
- SEO metadata
- Related posts
- Engagement metrics


### Example

* Api Key Authentication (TeamApiKey):

```python
import sendx_python_sdk
from sendx_python_sdk.models.rest_r_post import RestRPost
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
    api_instance = sendx_python_sdk.PostApi(api_client)
    identifier = 'contact_BnKjkbBBS500CoBCP0oChQ' # str | Resource identifier with prefix (e.g., `contact_BnKjkbBBS500CoBCP0oChQ`)  **Format:** `<prefix>_<22-character-id>` 

    try:
        # Get post by ID
        api_response = api_instance.get_post(identifier)
        print("The response of PostApi->get_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostApi->get_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Resource identifier with prefix (e.g., &#x60;contact_BnKjkbBBS500CoBCP0oChQ&#x60;)  **Format:** &#x60;&lt;prefix&gt;_&lt;22-character-id&gt;&#x60;  | 

### Return type

[**RestRPost**](RestRPost.md)

### Authorization

[TeamApiKey](../README.md#TeamApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ✅ Post retrieved successfully |  -  |
**401** | ❌ Unauthorized - Invalid or missing API key |  -  |
**404** | ❌ Not Found - Resource does not exist |  -  |
**500** | ❌ Internal Server Error - System error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_post**
> RestRPost update_post(identifier, rest_e_post)

Update post

Updates an existing blog post.

**🎯 Key Features:**
- Edit content
- Update metadata
- Change status
- Modify tags/categories


### Example

* Api Key Authentication (TeamApiKey):

```python
import sendx_python_sdk
from sendx_python_sdk.models.rest_e_post import RestEPost
from sendx_python_sdk.models.rest_r_post import RestRPost
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
    api_instance = sendx_python_sdk.PostApi(api_client)
    identifier = 'contact_BnKjkbBBS500CoBCP0oChQ' # str | Resource identifier with prefix (e.g., `contact_BnKjkbBBS500CoBCP0oChQ`)  **Format:** `<prefix>_<22-character-id>` 
    rest_e_post = sendx_python_sdk.RestEPost() # RestEPost | 

    try:
        # Update post
        api_response = api_instance.update_post(identifier, rest_e_post)
        print("The response of PostApi->update_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PostApi->update_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Resource identifier with prefix (e.g., &#x60;contact_BnKjkbBBS500CoBCP0oChQ&#x60;)  **Format:** &#x60;&lt;prefix&gt;_&lt;22-character-id&gt;&#x60;  | 
 **rest_e_post** | [**RestEPost**](RestEPost.md)|  | 

### Return type

[**RestRPost**](RestRPost.md)

### Authorization

[TeamApiKey](../README.md#TeamApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ✅ Post updated successfully |  -  |
**400** | ❌ Bad Request - Invalid input data |  -  |
**401** | ❌ Unauthorized - Invalid or missing API key |  -  |
**404** | ❌ Not Found - Resource does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

