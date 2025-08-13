# sendx_python_sdk.EmailSendingApi

All URIs are relative to *https://api.sendx.io/api/v1/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**send_email**](EmailSendingApi.md#send_email) | **POST** /send/email | Send transactional email
[**send_email_with_template**](EmailSendingApi.md#send_email_with_template) | **POST** /send/template | Send email using template


# **send_email**
> List[XEmailResponse] send_email(x_email_message)

Send transactional email

Sends transactional emails to specified recipients with support for personalization, attachments, and tracking.


### Example

* Api Key Authentication (TeamApiKey):

```python
import sendx_python_sdk
from sendx_python_sdk.models.x_email_message import XEmailMessage
from sendx_python_sdk.models.x_email_response import XEmailResponse
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
    api_instance = sendx_python_sdk.EmailSendingApi(api_client)
    x_email_message = sendx_python_sdk.XEmailMessage() # XEmailMessage | 

    try:
        # Send transactional email
        api_response = api_instance.send_email(x_email_message)
        print("The response of EmailSendingApi->send_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailSendingApi->send_email: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_email_message** | [**XEmailMessage**](XEmailMessage.md)|  | 

### Return type

[**List[XEmailResponse]**](XEmailResponse.md)

### Authorization

[TeamApiKey](../README.md#TeamApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ✅ Email sent successfully |  -  |
**401** | ❌ Unauthorized - Invalid or missing API key |  -  |
**422** | ❌ Unprocessable Entity - Invalid request format |  -  |
**429** | ❌ Too Many Requests - Rate limit exceeded |  -  |
**500** | ❌ Internal Server Error - System error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_email_with_template**
> List[XEmailResponse] send_email_with_template(template_email_message)

Send email using template

Sends emails using a pre-defined template with variable substitution.


### Example

* Api Key Authentication (TeamApiKey):

```python
import sendx_python_sdk
from sendx_python_sdk.models.template_email_message import TemplateEmailMessage
from sendx_python_sdk.models.x_email_response import XEmailResponse
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
    api_instance = sendx_python_sdk.EmailSendingApi(api_client)
    template_email_message = sendx_python_sdk.TemplateEmailMessage() # TemplateEmailMessage | 

    try:
        # Send email using template
        api_response = api_instance.send_email_with_template(template_email_message)
        print("The response of EmailSendingApi->send_email_with_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailSendingApi->send_email_with_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_email_message** | [**TemplateEmailMessage**](TemplateEmailMessage.md)|  | 

### Return type

[**List[XEmailResponse]**](XEmailResponse.md)

### Authorization

[TeamApiKey](../README.md#TeamApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ✅ Email sent successfully |  -  |
**401** | ❌ Unauthorized - Invalid or missing API key |  -  |
**404** | Template not found |  -  |
**422** | ❌ Unprocessable Entity - Invalid request format |  -  |
**429** | ❌ Too Many Requests - Rate limit exceeded |  -  |
**500** | ❌ Internal Server Error - System error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

