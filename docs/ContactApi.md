# sendx_python_sdk.ContactApi

All URIs are relative to *https://api.sendx.io/api/v1/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_contact**](ContactApi.md#create_contact) | **POST** /contact | Create a new contact
[**delete_contact**](ContactApi.md#delete_contact) | **DELETE** /contact/{identifier} | Delete contact
[**get_all_contacts**](ContactApi.md#get_all_contacts) | **GET** /contact | Get all contacts
[**get_contact**](ContactApi.md#get_contact) | **GET** /contact/{identifier} | Get contact by ID
[**unsubscribe_contact**](ContactApi.md#unsubscribe_contact) | **POST** /contact/unsubscribe/{identifier} | Unsubscribe contact
[**update_contact**](ContactApi.md#update_contact) | **PUT** /contact/{identifier} | Update contact


# **create_contact**
> RestRContact create_contact(rest_e_contact)

Create a new contact

Creates a new contact in your SendX team with the provided information.

**🎯 Key Features:**
- Email validation and duplicate detection
- Automatic relationship building with lists and tags
- Smart custom field handling

**📋 Business Rules:**
- Email is mandatory and must be unique within the team
- Last tracked IP is stored for analytics


### Example

* Api Key Authentication (TeamApiKey):

```python
import sendx_python_sdk
from sendx_python_sdk.models.rest_e_contact import RestEContact
from sendx_python_sdk.models.rest_r_contact import RestRContact
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
    api_instance = sendx_python_sdk.ContactApi(api_client)
    rest_e_contact = {"email":"john.doe@example.com"} # RestEContact | 

    try:
        # Create a new contact
        api_response = api_instance.create_contact(rest_e_contact)
        print("The response of ContactApi->create_contact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactApi->create_contact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rest_e_contact** | [**RestEContact**](RestEContact.md)|  | 

### Return type

[**RestRContact**](RestRContact.md)

### Authorization

[TeamApiKey](../README.md#TeamApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | ✅ Contact created successfully |  -  |
**400** | ❌ Bad Request - Invalid input data |  -  |
**401** | ❌ Unauthorized - Invalid or missing API key |  -  |
**409** | ❌ Conflict - Resource already exists |  -  |
**422** | ❌ Unprocessable Entity - Invalid request format |  -  |
**500** | ❌ Internal Server Error - System error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_contact**
> DeleteResponse delete_contact(identifier)

Delete contact

Soft deletes a contact from your team.

**🎯 Key Features:**
- Soft delete preserves data
- Removes from all lists
- Cancels pending campaigns
- Maintains historical data


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
    api_instance = sendx_python_sdk.ContactApi(api_client)
    identifier = 'contact_BnKjkbBBS500CoBCP0oChQ' # str | Resource identifier with prefix (e.g., `contact_BnKjkbBBS500CoBCP0oChQ`)  **Format:** `<prefix>_<22-character-id>` 

    try:
        # Delete contact
        api_response = api_instance.delete_contact(identifier)
        print("The response of ContactApi->delete_contact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactApi->delete_contact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Resource identifier with prefix (e.g., &#x60;contact_BnKjkbBBS500CoBCP0oChQ&#x60;)  **Format:** &#x60;&lt;prefix&gt;_&lt;22-character-id&gt;&#x60;  | 

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
**200** | ✅ Contact deleted successfully |  -  |
**400** | ❌ Bad Request - Invalid input data |  -  |
**401** | ❌ Unauthorized - Invalid or missing API key |  -  |
**404** | ❌ Not Found - Resource does not exist |  -  |
**500** | ❌ Internal Server Error - System error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_contacts**
> List[RestRContact] get_all_contacts(offset=offset, limit=limit, search=search)

Get all contacts

Retrieves a paginated list of all contacts in your team with optional filtering capabilities.

**🎯 Key Features:**
- Pagination support with offset/limit
- Search contacts by name or email
- All relationships included (lists, tags, custom fields)
- Prefixed IDs for easy integration

**📊 Pagination:**
- Default limit: 10 contacts per page
- Maximum limit: 100 contacts per page
- Use offset for page navigation

**🔍 Search:**
- Searches across firstName, lastName, and email fields
- Case-insensitive partial matching
- Combine with pagination for large datasets


### Example

* Api Key Authentication (TeamApiKey):

```python
import sendx_python_sdk
from sendx_python_sdk.models.rest_r_contact import RestRContact
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
    api_instance = sendx_python_sdk.ContactApi(api_client)
    offset = 0 # int | Number of records to skip for pagination.  **Examples:** - `0` - First page (default) - `50` - Second page (with limit=50) - `100` - Third page (with limit=50)  (optional) (default to 0)
    limit = 50 # int | Maximum number of records to return.  **Constraints:** - Minimum: 1 - Maximum: 100 - Default: 10  (optional) (default to 50)
    search = 'john' # str | Search term to filter contacts by name or email.  **Search Behavior:** - Searches firstName, lastName, and email fields - Case-insensitive partial matching - Minimum 2 characters for search  **Examples:** - `john` - Finds \"John Doe\", \"johnson@example.com\" - `@company.com` - Finds all emails from company.com - `smith` - Finds \"John Smith\", \"smith@email.com\"  (optional)

    try:
        # Get all contacts
        api_response = api_instance.get_all_contacts(offset=offset, limit=limit, search=search)
        print("The response of ContactApi->get_all_contacts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactApi->get_all_contacts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| Number of records to skip for pagination.  **Examples:** - &#x60;0&#x60; - First page (default) - &#x60;50&#x60; - Second page (with limit&#x3D;50) - &#x60;100&#x60; - Third page (with limit&#x3D;50)  | [optional] [default to 0]
 **limit** | **int**| Maximum number of records to return.  **Constraints:** - Minimum: 1 - Maximum: 100 - Default: 10  | [optional] [default to 50]
 **search** | **str**| Search term to filter contacts by name or email.  **Search Behavior:** - Searches firstName, lastName, and email fields - Case-insensitive partial matching - Minimum 2 characters for search  **Examples:** - &#x60;john&#x60; - Finds \&quot;John Doe\&quot;, \&quot;johnson@example.com\&quot; - &#x60;@company.com&#x60; - Finds all emails from company.com - &#x60;smith&#x60; - Finds \&quot;John Smith\&quot;, \&quot;smith@email.com\&quot;  | [optional] 

### Return type

[**List[RestRContact]**](RestRContact.md)

### Authorization

[TeamApiKey](../README.md#TeamApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ✅ Contacts retrieved successfully |  -  |
**400** | ❌ Bad Request - Invalid input data |  -  |
**401** | ❌ Unauthorized - Invalid or missing API key |  -  |
**500** | ❌ Internal Server Error - System error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contact**
> RestRContact get_contact(identifier)

Get contact by ID

Retrieves detailed information about a specific contact.

**🎯 Key Features:**
- Returns complete contact profile
- Includes all lists and tags
- Shows custom field values
- Provides engagement metrics


### Example

* Api Key Authentication (TeamApiKey):

```python
import sendx_python_sdk
from sendx_python_sdk.models.rest_r_contact import RestRContact
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
    api_instance = sendx_python_sdk.ContactApi(api_client)
    identifier = 'contact_BnKjkbBBS500CoBCP0oChQ' # str | Resource identifier with prefix (e.g., `contact_BnKjkbBBS500CoBCP0oChQ`)  **Format:** `<prefix>_<22-character-id>` 

    try:
        # Get contact by ID
        api_response = api_instance.get_contact(identifier)
        print("The response of ContactApi->get_contact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactApi->get_contact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Resource identifier with prefix (e.g., &#x60;contact_BnKjkbBBS500CoBCP0oChQ&#x60;)  **Format:** &#x60;&lt;prefix&gt;_&lt;22-character-id&gt;&#x60;  | 

### Return type

[**RestRContact**](RestRContact.md)

### Authorization

[TeamApiKey](../README.md#TeamApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ✅ Contact retrieved successfully |  -  |
**400** | ❌ Bad Request - Invalid input data |  -  |
**401** | ❌ Unauthorized - Invalid or missing API key |  -  |
**404** | ❌ Not Found - Resource does not exist |  -  |
**500** | ❌ Internal Server Error - System error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unsubscribe_contact**
> MessageResponse unsubscribe_contact(identifier)

Unsubscribe contact

Unsubscribes a contact from all marketing communications.

**🎯 Key Features:**
- Marks contact as unsubscribed
- Removes from all active campaigns
- Maintains unsubscribe history
- Complies with anti-spam regulations


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
    api_instance = sendx_python_sdk.ContactApi(api_client)
    identifier = 'contact_BnKjkbBBS500CoBCP0oChQ' # str | Resource identifier with prefix (e.g., `contact_BnKjkbBBS500CoBCP0oChQ`)  **Format:** `<prefix>_<22-character-id>` 

    try:
        # Unsubscribe contact
        api_response = api_instance.unsubscribe_contact(identifier)
        print("The response of ContactApi->unsubscribe_contact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactApi->unsubscribe_contact: %s\n" % e)
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
**200** | ✅ Contact unsubscribed successfully |  -  |
**400** | ❌ Bad Request - Invalid input data |  -  |
**401** | ❌ Unauthorized - Invalid or missing API key |  -  |
**404** | ❌ Not Found - Resource does not exist |  -  |
**500** | ❌ Internal Server Error - System error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_contact**
> RestRContact update_contact(identifier, rest_e_contact)

Update contact

Updates an existing contact's information.

**🎯 Key Features:**
- Partial updates supported
- Add/remove lists and tags
- Update custom fields
- Change email address


### Example

* Api Key Authentication (TeamApiKey):

```python
import sendx_python_sdk
from sendx_python_sdk.models.rest_e_contact import RestEContact
from sendx_python_sdk.models.rest_r_contact import RestRContact
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
    api_instance = sendx_python_sdk.ContactApi(api_client)
    identifier = 'contact_BnKjkbBBS500CoBCP0oChQ' # str | Resource identifier with prefix (e.g., `contact_BnKjkbBBS500CoBCP0oChQ`)  **Format:** `<prefix>_<22-character-id>` 
    rest_e_contact = {"firstName":"Alexander","lastName":"Johnson-Smith","company":"New Enterprise Corp"} # RestEContact | 

    try:
        # Update contact
        api_response = api_instance.update_contact(identifier, rest_e_contact)
        print("The response of ContactApi->update_contact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContactApi->update_contact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Resource identifier with prefix (e.g., &#x60;contact_BnKjkbBBS500CoBCP0oChQ&#x60;)  **Format:** &#x60;&lt;prefix&gt;_&lt;22-character-id&gt;&#x60;  | 
 **rest_e_contact** | [**RestEContact**](RestEContact.md)|  | 

### Return type

[**RestRContact**](RestRContact.md)

### Authorization

[TeamApiKey](../README.md#TeamApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ✅ Contact updated successfully |  -  |
**400** | ❌ Bad Request - Invalid input data |  -  |
**401** | ❌ Unauthorized - Invalid or missing API key |  -  |
**404** | ❌ Not Found - Resource does not exist |  -  |
**409** | ❌ Conflict - Resource already exists |  -  |
**422** | ❌ Unprocessable Entity - Invalid request format |  -  |
**500** | ❌ Internal Server Error - System error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

