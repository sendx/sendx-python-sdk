# sendx_python_sdk.SenderApi

All URIs are relative to *https://api.sendx.io/api/v1/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sender**](SenderApi.md#create_sender) | **POST** /sender | Create sender
[**get_all_senders**](SenderApi.md#get_all_senders) | **GET** /sender | Get all senders


# **create_sender**
> RestRSender create_sender(rest_e_sender)

Create sender

Adds a new sender email address.


### Example

* Api Key Authentication (TeamApiKey):

```python
import sendx_python_sdk
from sendx_python_sdk.models.rest_e_sender import RestESender
from sendx_python_sdk.models.rest_r_sender import RestRSender
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
    api_instance = sendx_python_sdk.SenderApi(api_client)
    rest_e_sender = sendx_python_sdk.RestESender() # RestESender | 

    try:
        # Create sender
        api_response = api_instance.create_sender(rest_e_sender)
        print("The response of SenderApi->create_sender:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SenderApi->create_sender: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rest_e_sender** | [**RestESender**](RestESender.md)|  | 

### Return type

[**RestRSender**](RestRSender.md)

### Authorization

[TeamApiKey](../README.md#TeamApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | ✅ Sender created successfully |  -  |
**401** | ❌ Unauthorized - Invalid or missing API key |  -  |
**403** | ❌ Forbidden - Resource name already exists |  -  |
**422** | ❌ Unprocessable Entity - Invalid request format |  -  |
**500** | ❌ Internal Server Error - System error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_senders**
> List[RestRSender] get_all_senders()

Get all senders

Retrieves all verified sender addresses.


### Example

* Api Key Authentication (TeamApiKey):

```python
import sendx_python_sdk
from sendx_python_sdk.models.rest_r_sender import RestRSender
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
    api_instance = sendx_python_sdk.SenderApi(api_client)

    try:
        # Get all senders
        api_response = api_instance.get_all_senders()
        print("The response of SenderApi->get_all_senders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SenderApi->get_all_senders: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[RestRSender]**](RestRSender.md)

### Authorization

[TeamApiKey](../README.md#TeamApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ✅ Senders retrieved successfully |  -  |
**401** | ❌ Unauthorized - Invalid or missing API key |  -  |
**500** | ❌ Internal Server Error - System error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

