# sendx_python_sdk.CustomFieldApi

All URIs are relative to *https://api.sendx.io/api/v1/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customfield_customfield_id_delete**](CustomFieldApi.md#customfield_customfield_id_delete) | **DELETE** /customfield/{customfieldId} | Delete Custom Field
[**customfield_customfield_id_get**](CustomFieldApi.md#customfield_customfield_id_get) | **GET** /customfield/{customfieldId} | Get Custom Field
[**customfield_customfield_id_put**](CustomFieldApi.md#customfield_customfield_id_put) | **PUT** /customfield/{customfieldId} | Update Custom Field
[**customfield_get**](CustomFieldApi.md#customfield_get) | **GET** /customfield | Get All Custom Fields
[**customfield_post**](CustomFieldApi.md#customfield_post) | **POST** /customfield | Create Custom Field


# **customfield_customfield_id_delete**
> CustomfieldCustomfieldIdDelete200Response customfield_customfield_id_delete(customfield_id)

Delete Custom Field

Deletes a custom field.

### Example

* Api Key Authentication (apiKeyAuth):

```python
import sendx_python_sdk
from sendx_python_sdk.models.customfield_customfield_id_delete200_response import CustomfieldCustomfieldIdDelete200Response
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
    api_instance = sendx_python_sdk.CustomFieldApi(api_client)
    customfield_id = 'encrypted_id_124' # str | The CustomFieldId you want to delete.

    try:
        # Delete Custom Field
        api_response = api_instance.customfield_customfield_id_delete(customfield_id)
        print("The response of CustomFieldApi->customfield_customfield_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFieldApi->customfield_customfield_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customfield_id** | **str**| The CustomFieldId you want to delete. | 

### Return type

[**CustomfieldCustomfieldIdDelete200Response**](CustomfieldCustomfieldIdDelete200Response.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Custom Field deleted successfully. |  -  |
**401** | Not Authorized |  -  |
**406** | customfieldId is empty |  -  |
**422** | Request body is not in proper format |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customfield_customfield_id_get**
> CustomField customfield_customfield_id_get(customfield_id)

Get Custom Field

Find Custom Field by customfieldId.

### Example

* Api Key Authentication (apiKeyAuth):

```python
import sendx_python_sdk
from sendx_python_sdk.models.custom_field import CustomField
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
    api_instance = sendx_python_sdk.CustomFieldApi(api_client)
    customfield_id = 'encrypted_id_123' # str | The CustomFieldId you want to get.

    try:
        # Get Custom Field
        api_response = api_instance.customfield_customfield_id_get(customfield_id)
        print("The response of CustomFieldApi->customfield_customfield_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFieldApi->customfield_customfield_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customfield_id** | **str**| The CustomFieldId you want to get. | 

### Return type

[**CustomField**](CustomField.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Custom Field retrieved successfully. |  -  |
**401** | Not Authorized |  -  |
**406** | customfieldId is empty |  -  |
**422** | Request body is not in proper format |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customfield_customfield_id_put**
> CustomField customfield_customfield_id_put(customfield_id, e_custom_field)

Update Custom Field

Update Custom Field with the given data.

### Example

* Api Key Authentication (apiKeyAuth):

```python
import sendx_python_sdk
from sendx_python_sdk.models.custom_field import CustomField
from sendx_python_sdk.models.e_custom_field import ECustomField
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
    api_instance = sendx_python_sdk.CustomFieldApi(api_client)
    customfield_id = 'encrypted_id_123' # str | The CustomFieldId you want to update.
    e_custom_field = {"name":"Updated Field","type":"number","shown":false,"isShareable":true,"description":"An updated custom field description"} # ECustomField | 

    try:
        # Update Custom Field
        api_response = api_instance.customfield_customfield_id_put(customfield_id, e_custom_field)
        print("The response of CustomFieldApi->customfield_customfield_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFieldApi->customfield_customfield_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customfield_id** | **str**| The CustomFieldId you want to update. | 
 **e_custom_field** | [**ECustomField**](ECustomField.md)|  | 

### Return type

[**CustomField**](CustomField.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Custom Field updated successfully. |  -  |
**401** | Not Authorized |  -  |
**406** | Not Acceptable |  -  |
**422** | Request body is not in proper format |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customfield_get**
> List[CustomField] customfield_get(offset, limit, search=search)

Get All Custom Fields

Retrieve all custom fields.

### Example

* Api Key Authentication (apiKeyAuth):

```python
import sendx_python_sdk
from sendx_python_sdk.models.custom_field import CustomField
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
    api_instance = sendx_python_sdk.CustomFieldApi(api_client)
    offset = 0 # int | Offset for pagination.
    limit = 10 # int | Limit for pagination.
    search = 'example search' # str | Search term for filtering results. (optional)

    try:
        # Get All Custom Fields
        api_response = api_instance.customfield_get(offset, limit, search=search)
        print("The response of CustomFieldApi->customfield_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFieldApi->customfield_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| Offset for pagination. | 
 **limit** | **int**| Limit for pagination. | 
 **search** | **str**| Search term for filtering results. | [optional] 

### Return type

[**List[CustomField]**](CustomField.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of custom fields retrieved successfully. |  -  |
**401** | Not Authorized |  -  |
**422** | Request body is not in proper format |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customfield_post**
> CustomField customfield_post(e_custom_field)

Create Custom Field

Create a custom field with the given data.

### Example

* Api Key Authentication (apiKeyAuth):

```python
import sendx_python_sdk
from sendx_python_sdk.models.custom_field import CustomField
from sendx_python_sdk.models.e_custom_field import ECustomField
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
    api_instance = sendx_python_sdk.CustomFieldApi(api_client)
    e_custom_field = {"name":"Custom Field Example","type":0,"shown":true,"isShareable":false,"description":"An example custom field"} # ECustomField | 

    try:
        # Create Custom Field
        api_response = api_instance.customfield_post(e_custom_field)
        print("The response of CustomFieldApi->customfield_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomFieldApi->customfield_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **e_custom_field** | [**ECustomField**](ECustomField.md)|  | 

### Return type

[**CustomField**](CustomField.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Custom Field created successfully. |  -  |
**401** | Not Authorized |  -  |
**406** | Not Acceptable |  -  |
**422** | Request body is not in proper format |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

