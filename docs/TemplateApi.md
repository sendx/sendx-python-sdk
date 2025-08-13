# sendx_python_sdk.TemplateApi

All URIs are relative to *https://api.sendx.io/api/v1/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_email_template**](TemplateApi.md#create_email_template) | **POST** /template/email | Create email template
[**delete_email_template**](TemplateApi.md#delete_email_template) | **DELETE** /template/email/{identifier} | Delete template
[**get_all_email_templates**](TemplateApi.md#get_all_email_templates) | **GET** /template/email | Get all templates
[**get_email_template**](TemplateApi.md#get_email_template) | **GET** /template/email/{identifier} | Get template by ID
[**update_email_template**](TemplateApi.md#update_email_template) | **PUT** /template/email/{identifier} | Update template


# **create_email_template**
> RestRTemplate create_email_template(rest_e_template)

Create email template

Creates a new reusable email template.


### Example

* Api Key Authentication (TeamApiKey):

```python
import sendx_python_sdk
from sendx_python_sdk.models.rest_e_template import RestETemplate
from sendx_python_sdk.models.rest_r_template import RestRTemplate
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
    api_instance = sendx_python_sdk.TemplateApi(api_client)
    rest_e_template = {"name":"Weekly Newsletter Template","htmlCode":"<div class=\"newsletter\"><h1>{{company.name}} Weekly Update</h1><div class=\"content\">{{email.content}}</div></div>","templateCode":"{\"type\":\"doc\",\"content\":[{\"type\":\"paragraph\",\"attrs\":{\"textAlign\":null,\"showIfKey\":null},\"content\":[{\"type\":\"text\",\"text\":\"This is a new template\"}]}]}","editorType":1} # RestETemplate | 

    try:
        # Create email template
        api_response = api_instance.create_email_template(rest_e_template)
        print("The response of TemplateApi->create_email_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplateApi->create_email_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rest_e_template** | [**RestETemplate**](RestETemplate.md)|  | 

### Return type

[**RestRTemplate**](RestRTemplate.md)

### Authorization

[TeamApiKey](../README.md#TeamApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | ✅ Template created successfully |  -  |
**401** | ❌ Unauthorized - Invalid or missing API key |  -  |
**403** | ❌ Forbidden - Resource name already exists |  -  |
**422** | ❌ Unprocessable Entity - Invalid request format |  -  |
**500** | ❌ Internal Server Error - System error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_email_template**
> DeleteResponse delete_email_template(identifier)

Delete template

Deletes an email template.


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
    api_instance = sendx_python_sdk.TemplateApi(api_client)
    identifier = 'template_f3lJvTEhSjKGVb5Lwc5SWS' # str | The unique template identifier to update.  - `template_f3lJvTEhSjKGVb5Lwc5SWS` 

    try:
        # Delete template
        api_response = api_instance.delete_email_template(identifier)
        print("The response of TemplateApi->delete_email_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplateApi->delete_email_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| The unique template identifier to update.  - &#x60;template_f3lJvTEhSjKGVb5Lwc5SWS&#x60;  | 

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
**200** | ✅ Template deleted successfully |  -  |
**401** | ❌ Unauthorized - Invalid or missing API key |  -  |
**404** | ❌ Not Found - Resource does not exist |  -  |
**500** | ❌ Internal Server Error - System error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_email_templates**
> List[RestRTemplate] get_all_email_templates(offset=offset, limit=limit, search=search)

Get all templates

Retrieves all email templates.


### Example

* Api Key Authentication (TeamApiKey):

```python
import sendx_python_sdk
from sendx_python_sdk.models.rest_r_template import RestRTemplate
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
    api_instance = sendx_python_sdk.TemplateApi(api_client)
    offset = 0 # int | Number of records to skip for pagination.  **Examples:** - `0` - First page (default) - `25` - Second page (with limit=25) - `50` - Third page (with limit=25)  (optional) (default to 0)
    limit = 10 # int | Maximum number of templates to return per page.  **Guidelines:** - Default: 10 templates - Maximum: 100 templates - Recommended: 25-100 for optimal performance  (optional) (default to 10)
    search = 'search_example' # str | Search templates by name (case-insensitive partial matching).  **Examples:** - `newsletter` - Finds \"Weekly Newsletter\", \"Monthly Newsletter\" - `welcome` - Finds \"Welcome Email\", \"New User Welcome\" - `product` - Finds \"Product Launch\", \"Product Update\"  (optional)

    try:
        # Get all templates
        api_response = api_instance.get_all_email_templates(offset=offset, limit=limit, search=search)
        print("The response of TemplateApi->get_all_email_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplateApi->get_all_email_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| Number of records to skip for pagination.  **Examples:** - &#x60;0&#x60; - First page (default) - &#x60;25&#x60; - Second page (with limit&#x3D;25) - &#x60;50&#x60; - Third page (with limit&#x3D;25)  | [optional] [default to 0]
 **limit** | **int**| Maximum number of templates to return per page.  **Guidelines:** - Default: 10 templates - Maximum: 100 templates - Recommended: 25-100 for optimal performance  | [optional] [default to 10]
 **search** | **str**| Search templates by name (case-insensitive partial matching).  **Examples:** - &#x60;newsletter&#x60; - Finds \&quot;Weekly Newsletter\&quot;, \&quot;Monthly Newsletter\&quot; - &#x60;welcome&#x60; - Finds \&quot;Welcome Email\&quot;, \&quot;New User Welcome\&quot; - &#x60;product&#x60; - Finds \&quot;Product Launch\&quot;, \&quot;Product Update\&quot;  | [optional] 

### Return type

[**List[RestRTemplate]**](RestRTemplate.md)

### Authorization

[TeamApiKey](../README.md#TeamApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ✅ Templates retrieved successfully |  -  |
**401** | ❌ Unauthorized - Invalid or missing API key |  -  |
**500** | ❌ Internal Server Error - System error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_template**
> RestRTemplate get_email_template(identifier)

Get template by ID

Retrieves a specific email template.


### Example

* Api Key Authentication (TeamApiKey):

```python
import sendx_python_sdk
from sendx_python_sdk.models.rest_r_template import RestRTemplate
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
    api_instance = sendx_python_sdk.TemplateApi(api_client)
    identifier = 'template_f3lJvTEhSjKGVb5Lwc5SWS' # str | The unique template identifier.  - `template_f3lJvTEhSjKGVb5Lwc5SWS` - Standard prefixed ID 

    try:
        # Get template by ID
        api_response = api_instance.get_email_template(identifier)
        print("The response of TemplateApi->get_email_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplateApi->get_email_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| The unique template identifier.  - &#x60;template_f3lJvTEhSjKGVb5Lwc5SWS&#x60; - Standard prefixed ID  | 

### Return type

[**RestRTemplate**](RestRTemplate.md)

### Authorization

[TeamApiKey](../README.md#TeamApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ✅ Template retrieved successfully |  -  |
**401** | ❌ Unauthorized - Invalid or missing API key |  -  |
**404** | ❌ Not Found - Resource does not exist |  -  |
**500** | ❌ Internal Server Error - System error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_email_template**
> RestRTemplate update_email_template(identifier, rest_e_template)

Update template

Updates an existing email template.


### Example

* Api Key Authentication (TeamApiKey):

```python
import sendx_python_sdk
from sendx_python_sdk.models.rest_e_template import RestETemplate
from sendx_python_sdk.models.rest_r_template import RestRTemplate
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
    api_instance = sendx_python_sdk.TemplateApi(api_client)
    identifier = 'template_f3lJvTEhSjKGVb5Lwc5SWS' # str | The unique template identifier to update.  - `template_f3lJvTEhSjKGVb5Lwc5SWS` 
    rest_e_template = sendx_python_sdk.RestETemplate() # RestETemplate | 

    try:
        # Update template
        api_response = api_instance.update_email_template(identifier, rest_e_template)
        print("The response of TemplateApi->update_email_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplateApi->update_email_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| The unique template identifier to update.  - &#x60;template_f3lJvTEhSjKGVb5Lwc5SWS&#x60;  | 
 **rest_e_template** | [**RestETemplate**](RestETemplate.md)|  | 

### Return type

[**RestRTemplate**](RestRTemplate.md)

### Authorization

[TeamApiKey](../README.md#TeamApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ✅ Template updated successfully |  -  |
**401** | ❌ Unauthorized - Invalid or missing API key |  -  |
**403** | ❌ Forbidden - Resource name already exists |  -  |
**404** | ❌ Not Found - Resource does not exist |  -  |
**422** | ❌ Unprocessable Entity - Invalid request format |  -  |
**500** | ❌ Internal Server Error - System error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

