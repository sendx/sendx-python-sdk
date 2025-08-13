# sendx_python_sdk.CustomFieldApi

All URIs are relative to *https://api.sendx.io/api/v1/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_custom_field**](CustomFieldApi.md#create_custom_field) | **POST** /customfield | Create custom field
[**delete_custom_field**](CustomFieldApi.md#delete_custom_field) | **DELETE** /customfield/{identifier} | Delete custom field
[**get_all_custom_fields**](CustomFieldApi.md#get_all_custom_fields) | **GET** /customfield | Get all custom fields
[**get_custom_field**](CustomFieldApi.md#get_custom_field) | **GET** /customfield/{identifier} | Get custom field by ID
[**update_custom_field**](CustomFieldApi.md#update_custom_field) | **PUT** /customfield/{identifier} | Update custom field


# **create_custom_field**
> RestRCustomField create_custom_field(rest_e_custom_field)

Create custom field

Creates a new custom field for storing contact data.


### Example

* Api Key Authentication (TeamApiKey):

```python
import sendx_python_sdk
from sendx_python_sdk.models.rest_e_custom_field import RestECustomField
from sendx_python_sdk.models.rest_r_custom_field import RestRCustomField
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
    api_instance = sendx_python_sdk.CustomFieldApi(api_client)
    rest_e_custom_field = sendx_python_sdk.RestECustomField() # RestECustomField | 

    try:
        # Create custom field
        api_response = api_instance.create_custom_field(rest_e_custom_field)
        print("The response of CustomFieldApi->create_custom_field:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFieldApi->create_custom_field: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rest_e_custom_field** | [**RestECustomField**](RestECustomField.md)|  | 

### Return type

[**RestRCustomField**](RestRCustomField.md)

### Authorization

[TeamApiKey](../README.md#TeamApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | ✅ Custom field created successfully |  -  |
**401** | ❌ Unauthorized - Invalid or missing API key |  -  |
**403** | ❌ Forbidden - Resource name already exists |  -  |
**422** | ❌ Unprocessable Entity - Invalid request format |  -  |
**500** | ❌ Internal Server Error - System error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_custom_field**
> DeleteResponse delete_custom_field(identifier)

Delete custom field

Deletes a custom field (data is preserved).

**🎯 Key Features:**
- Remove unused fields
- Data remains on contacts
- Clean up field list


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
    api_instance = sendx_python_sdk.CustomFieldApi(api_client)
    identifier = 'identifier_example' # str | Custom field identifier to update

    try:
        # Delete custom field
        api_response = api_instance.delete_custom_field(identifier)
        print("The response of CustomFieldApi->delete_custom_field:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFieldApi->delete_custom_field: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Custom field identifier to update | 

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
**200** | ✅ Custom field deleted successfully |  -  |
**401** | ❌ Unauthorized - Invalid or missing API key |  -  |
**404** | ❌ Not Found - Resource does not exist |  -  |
**422** | ❌ Unprocessable Entity - Invalid request format |  -  |
**500** | ❌ Internal Server Error - System error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_custom_fields**
> List[RestRCustomField] get_all_custom_fields(offset=offset, limit=limit, search=search)

Get all custom fields

Retrieves all custom fields defined for your team.


### Example

* Api Key Authentication (TeamApiKey):

```python
import sendx_python_sdk
from sendx_python_sdk.models.rest_r_custom_field import RestRCustomField
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
    api_instance = sendx_python_sdk.CustomFieldApi(api_client)
    offset = 0 # int | Number of fields to skip for pagination (optional) (default to 0)
    limit = 10 # int | Maximum number of fields to return (optional) (default to 10)
    search = 'search_example' # str | Search custom fields by name (case-insensitive partial matching).  **Examples:** - `points` - Finds \"Loyalty points\", \"Reward points\"  (optional)

    try:
        # Get all custom fields
        api_response = api_instance.get_all_custom_fields(offset=offset, limit=limit, search=search)
        print("The response of CustomFieldApi->get_all_custom_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFieldApi->get_all_custom_fields: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| Number of fields to skip for pagination | [optional] [default to 0]
 **limit** | **int**| Maximum number of fields to return | [optional] [default to 10]
 **search** | **str**| Search custom fields by name (case-insensitive partial matching).  **Examples:** - &#x60;points&#x60; - Finds \&quot;Loyalty points\&quot;, \&quot;Reward points\&quot;  | [optional] 

### Return type

[**List[RestRCustomField]**](RestRCustomField.md)

### Authorization

[TeamApiKey](../README.md#TeamApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ✅ Custom fields retrieved successfully |  -  |
**401** | ❌ Unauthorized - Invalid or missing API key |  -  |
**500** | ❌ Internal Server Error - System error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_field**
> RestRCustomField get_custom_field(identifier)

Get custom field by ID

Retrieves details about a specific custom field.


### Example

* Api Key Authentication (TeamApiKey):

```python
import sendx_python_sdk
from sendx_python_sdk.models.rest_r_custom_field import RestRCustomField
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
    api_instance = sendx_python_sdk.CustomFieldApi(api_client)
    identifier = 'identifier_example' # str | Custom field identifier to update

    try:
        # Get custom field by ID
        api_response = api_instance.get_custom_field(identifier)
        print("The response of CustomFieldApi->get_custom_field:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFieldApi->get_custom_field: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Custom field identifier to update | 

### Return type

[**RestRCustomField**](RestRCustomField.md)

### Authorization

[TeamApiKey](../README.md#TeamApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ✅ Custom field retrieved successfully |  -  |
**401** | ❌ Unauthorized - Invalid or missing API key |  -  |
**404** | ❌ Not Found - Resource does not exist |  -  |
**422** | ❌ Unprocessable Entity - Invalid request format |  -  |
**500** | ❌ Internal Server Error - System error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_custom_field**
> RestRCustomField update_custom_field(identifier, rest_e_custom_field)

Update custom field

Updates a custom field definition.


### Example

* Api Key Authentication (TeamApiKey):

```python
import sendx_python_sdk
from sendx_python_sdk.models.rest_e_custom_field import RestECustomField
from sendx_python_sdk.models.rest_r_custom_field import RestRCustomField
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
    api_instance = sendx_python_sdk.CustomFieldApi(api_client)
    identifier = 'identifier_example' # str | Custom field identifier to update
    rest_e_custom_field = {"name":"Customer Tier","description":"Customer segmentation tier (Bronze/Silver/Gold)"} # RestECustomField | 

    try:
        # Update custom field
        api_response = api_instance.update_custom_field(identifier, rest_e_custom_field)
        print("The response of CustomFieldApi->update_custom_field:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFieldApi->update_custom_field: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Custom field identifier to update | 
 **rest_e_custom_field** | [**RestECustomField**](RestECustomField.md)|  | 

### Return type

[**RestRCustomField**](RestRCustomField.md)

### Authorization

[TeamApiKey](../README.md#TeamApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ✅ Custom field updated successfully |  -  |
**401** | ❌ Unauthorized - Invalid or missing API key |  -  |
**403** | ❌ Forbidden - Resource name already exists |  -  |
**404** | ❌ Not Found - Resource does not exist |  -  |
**422** | ❌ Unprocessable Entity - Invalid request format |  -  |
**500** | ❌ Internal Server Error - System error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

