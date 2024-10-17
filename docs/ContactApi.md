# sendx_python_sdk.ContactApi

All URIs are relative to *https://api.sendx.io/api/v1/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_contact**](ContactApi.md#create_contact) | **POST** /contact | Create a contact
[**delete_contact**](ContactApi.md#delete_contact) | **DELETE** /contact/{contactId} | Delete Contact
[**get_all_contacts**](ContactApi.md#get_all_contacts) | **GET** /contact | Get All Contacts
[**get_contact_by_id**](ContactApi.md#get_contact_by_id) | **GET** /contact/{contactId} | Get Contact by ID
[**unsubscribe_contact**](ContactApi.md#unsubscribe_contact) | **PUT** /contact/unsubscribe/{contactId} | Unsubscribe Contact
[**update_contact**](ContactApi.md#update_contact) | **PUT** /contact/{contactId} | Update Contact


# **create_contact**
> Response create_contact(contact_request)

Create a contact

Create Contact with given data

### Example

* Api Key Authentication (apiKeyAuth):

```python
import sendx_python_sdk
from sendx_python_sdk.models.contact_request import ContactRequest
from sendx_python_sdk.models.response import Response
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
    api_instance = sendx_python_sdk.ContactApi(api_client)
    contact_request = sendx_python_sdk.ContactRequest() # ContactRequest | 

    try:
        # Create a contact
        api_response = api_instance.create_contact(contact_request)
        print("The response of ContactApi->create_contact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactApi->create_contact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_request** | [**ContactRequest**](ContactRequest.md)|  | 

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
**200** | Contact Created Successfully |  -  |
**401** | Not Authorized |  -  |
**406** | Not Acceptable |  -  |
**422** | Request body is not in proper format |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_contact**
> Response delete_contact(contact_id)

Delete Contact

Deletes Contact

### Example

* Api Key Authentication (apiKeyAuth):

```python
import sendx_python_sdk
from sendx_python_sdk.models.response import Response
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
    api_instance = sendx_python_sdk.ContactApi(api_client)
    contact_id = 'contact_id_example' # str | The Contact ID to delete

    try:
        # Delete Contact
        api_response = api_instance.delete_contact(contact_id)
        print("The response of ContactApi->delete_contact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactApi->delete_contact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_id** | **str**| The Contact ID to delete | 

### Return type

[**Response**](Response.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Contact deleted successfully |  -  |
**401** | Not Authorized |  -  |
**406** | Contact ID is empty |  -  |
**422** | Request body is not in proper format |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_contacts**
> List[Contact] get_all_contacts(offset=offset, limit=limit, contact_type=contact_type, search=search)

Get All Contacts

Find all contacts with optional filters

### Example

* Api Key Authentication (apiKeyAuth):

```python
import sendx_python_sdk
from sendx_python_sdk.models.contact import Contact
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
    api_instance = sendx_python_sdk.ContactApi(api_client)
    offset = 0 # int | Offset for pagination (optional) (default to 0)
    limit = 10 # int | Limit for pagination (optional) (default to 10)
    contact_type = 'contact_type_example' # str | Filter contacts by type (optional)
    search = 'search_example' # str | Search term to filter contacts (optional)

    try:
        # Get All Contacts
        api_response = api_instance.get_all_contacts(offset=offset, limit=limit, contact_type=contact_type, search=search)
        print("The response of ContactApi->get_all_contacts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactApi->get_all_contacts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| Offset for pagination | [optional] [default to 0]
 **limit** | **int**| Limit for pagination | [optional] [default to 10]
 **contact_type** | **str**| Filter contacts by type | [optional] 
 **search** | **str**| Search term to filter contacts | [optional] 

### Return type

[**List[Contact]**](Contact.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Contacts |  -  |
**401** | Not Authorized |  -  |
**422** | Request body is not in proper format |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contact_by_id**
> Contact get_contact_by_id(contact_id)

Get Contact by ID

Retrieve a specific contact by its contactId.

### Example

* Api Key Authentication (apiKeyAuth):

```python
import sendx_python_sdk
from sendx_python_sdk.models.contact import Contact
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
    api_instance = sendx_python_sdk.ContactApi(api_client)
    contact_id = 'sendxid123' # str | The ID of the contact to retrieve.

    try:
        # Get Contact by ID
        api_response = api_instance.get_contact_by_id(contact_id)
        print("The response of ContactApi->get_contact_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactApi->get_contact_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_id** | **str**| The ID of the contact to retrieve. | 

### Return type

[**Contact**](Contact.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieved contact successfully. |  -  |
**401** | Not Authorized - Invalid or missing API key. |  -  |
**406** | Contact ID is empty or invalid. |  -  |
**422** | Request body is not in proper format. |  -  |
**500** | Internal Server Error - Something went wrong on the server. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unsubscribe_contact**
> Response unsubscribe_contact(contact_id)

Unsubscribe Contact

Unsubscribe a globally existing contact

### Example

* Api Key Authentication (apiKeyAuth):

```python
import sendx_python_sdk
from sendx_python_sdk.models.response import Response
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
    api_instance = sendx_python_sdk.ContactApi(api_client)
    contact_id = 'sendx123' # str | The Contact ID to unsubscribe

    try:
        # Unsubscribe Contact
        api_response = api_instance.unsubscribe_contact(contact_id)
        print("The response of ContactApi->unsubscribe_contact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactApi->unsubscribe_contact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_id** | **str**| The Contact ID to unsubscribe | 

### Return type

[**Response**](Response.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Contact successfully unsubscribed |  -  |
**401** | Not Authorized |  -  |
**406** | Contact ID is empty or invalid |  -  |
**422** | Request body is not in proper format |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_contact**
> Contact update_contact(contact_id, contact_request)

Update Contact

Update Contact with given data

### Example

* Api Key Authentication (apiKeyAuth):

```python
import sendx_python_sdk
from sendx_python_sdk.models.contact import Contact
from sendx_python_sdk.models.contact_request import ContactRequest
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
    api_instance = sendx_python_sdk.ContactApi(api_client)
    contact_id = 'sendxid123' # str | The ID of the Contact to update
    contact_request = sendx_python_sdk.ContactRequest() # ContactRequest | 

    try:
        # Update Contact
        api_response = api_instance.update_contact(contact_id, contact_request)
        print("The response of ContactApi->update_contact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactApi->update_contact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_id** | **str**| The ID of the Contact to update | 
 **contact_request** | [**ContactRequest**](ContactRequest.md)|  | 

### Return type

[**Contact**](Contact.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Contact Updated Successfully |  -  |
**401** | Not Authorized |  -  |
**406** | Not Acceptable |  -  |
**422** | Request body is not in proper format |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

