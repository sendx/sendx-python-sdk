# sendx_python_sdk.WebhookApi

All URIs are relative to *https://api.sendx.io/api/v1/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_webhook**](WebhookApi.md#create_webhook) | **POST** /webhook | Create webhook
[**delete_webhook**](WebhookApi.md#delete_webhook) | **DELETE** /webhook/{identifier} | Delete webhook
[**get_all_webhooks**](WebhookApi.md#get_all_webhooks) | **GET** /webhook | Get all webhooks
[**get_webhook**](WebhookApi.md#get_webhook) | **GET** /webhook/{identifier} | Get webhook by ID
[**update_webhook**](WebhookApi.md#update_webhook) | **PUT** /webhook/{identifier} | Update webhook


# **create_webhook**
> RestRWebhook create_webhook(rest_e_webhook)

Create webhook

Creates a new webhook for event notifications.


### Example

* Api Key Authentication (TeamApiKey):

```python
import sendx_python_sdk
from sendx_python_sdk.models.rest_e_webhook import RestEWebhook
from sendx_python_sdk.models.rest_r_webhook import RestRWebhook
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
    api_instance = sendx_python_sdk.WebhookApi(api_client)
    rest_e_webhook = {"enabled":true,"url":"https://api.example.com/webhooks/sendx","unsubscribed":true,"dropped":true,"bounced":true,"markedSpam":true,"clicked":true,"opened":true,"contactCreated":true} # RestEWebhook | 

    try:
        # Create webhook
        api_response = api_instance.create_webhook(rest_e_webhook)
        print("The response of WebhookApi->create_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookApi->create_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rest_e_webhook** | [**RestEWebhook**](RestEWebhook.md)|  | 

### Return type

[**RestRWebhook**](RestRWebhook.md)

### Authorization

[TeamApiKey](../README.md#TeamApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | ✅ Webhook created successfully |  -  |
**401** | ❌ Unauthorized - Invalid or missing API key |  -  |
**403** | ❌ Forbidden - Resource name already exists |  -  |
**422** | ❌ Unprocessable Entity - Invalid request format |  -  |
**500** | ❌ Internal Server Error - System error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_webhook**
> DeleteResponse delete_webhook(identifier)

Delete webhook

Deletes a webhook configuration.

**🎯 Key Features:**
- Remove webhooks
- Stop event delivery
- Clean up endpoints


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
    api_instance = sendx_python_sdk.WebhookApi(api_client)
    identifier = 'identifier_example' # str | Webhook identifier to update

    try:
        # Delete webhook
        api_response = api_instance.delete_webhook(identifier)
        print("The response of WebhookApi->delete_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookApi->delete_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Webhook identifier to update | 

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
**200** | ✅ Webhook deleted successfully |  -  |
**401** | ❌ Unauthorized - Invalid or missing API key |  -  |
**404** | ❌ Not Found - Resource does not exist |  -  |
**422** | ❌ Unprocessable Entity - Invalid request format |  -  |
**500** | ❌ Internal Server Error - System error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_webhooks**
> List[RestRWebhook] get_all_webhooks()

Get all webhooks

Retrieves all configured webhooks.


### Example

* Api Key Authentication (TeamApiKey):

```python
import sendx_python_sdk
from sendx_python_sdk.models.rest_r_webhook import RestRWebhook
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
    api_instance = sendx_python_sdk.WebhookApi(api_client)

    try:
        # Get all webhooks
        api_response = api_instance.get_all_webhooks()
        print("The response of WebhookApi->get_all_webhooks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookApi->get_all_webhooks: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[RestRWebhook]**](RestRWebhook.md)

### Authorization

[TeamApiKey](../README.md#TeamApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ✅ Webhooks retrieved successfully |  -  |
**401** | ❌ Unauthorized - Invalid or missing API key |  -  |
**500** | ❌ Internal Server Error - System error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhook**
> RestRWebhook get_webhook(identifier)

Get webhook by ID

Retrieves details about a specific webhook.


### Example

* Api Key Authentication (TeamApiKey):

```python
import sendx_python_sdk
from sendx_python_sdk.models.rest_r_webhook import RestRWebhook
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
    api_instance = sendx_python_sdk.WebhookApi(api_client)
    identifier = 'identifier_example' # str | Webhook identifier to retrieve

    try:
        # Get webhook by ID
        api_response = api_instance.get_webhook(identifier)
        print("The response of WebhookApi->get_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookApi->get_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Webhook identifier to retrieve | 

### Return type

[**RestRWebhook**](RestRWebhook.md)

### Authorization

[TeamApiKey](../README.md#TeamApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ✅ Webhook retrieved successfully |  -  |
**401** | ❌ Unauthorized - Invalid or missing API key |  -  |
**404** | ❌ Not Found - Resource does not exist |  -  |
**422** | ❌ Unprocessable Entity - Invalid request format |  -  |
**500** | ❌ Internal Server Error - System error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_webhook**
> RestRWebhook update_webhook(identifier, rest_e_webhook)

Update webhook

Updates webhook configuration.


### Example

* Api Key Authentication (TeamApiKey):

```python
import sendx_python_sdk
from sendx_python_sdk.models.rest_e_webhook import RestEWebhook
from sendx_python_sdk.models.rest_r_webhook import RestRWebhook
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
    api_instance = sendx_python_sdk.WebhookApi(api_client)
    identifier = 'identifier_example' # str | Webhook identifier to update
    rest_e_webhook = sendx_python_sdk.RestEWebhook() # RestEWebhook | 

    try:
        # Update webhook
        api_response = api_instance.update_webhook(identifier, rest_e_webhook)
        print("The response of WebhookApi->update_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookApi->update_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Webhook identifier to update | 
 **rest_e_webhook** | [**RestEWebhook**](RestEWebhook.md)|  | 

### Return type

[**RestRWebhook**](RestRWebhook.md)

### Authorization

[TeamApiKey](../README.md#TeamApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ✅ Webhook updated successfully |  -  |
**401** | ❌ Unauthorized - Invalid or missing API key |  -  |
**403** | ❌ Forbidden - Resource name already exists |  -  |
**404** | ❌ Not Found - Resource does not exist |  -  |
**422** | ❌ Unprocessable Entity - Invalid request format |  -  |
**500** | ❌ Internal Server Error - System error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

