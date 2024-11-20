# sendx_python_sdk.GettingStartedApi

All URIs are relative to *https://api.sendx.io/api/v1/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**identify_contact**](GettingStartedApi.md#identify_contact) | **POST** /contact/identify | Identify contact
[**tracking_contact**](GettingStartedApi.md#tracking_contact) | **POST** /contact/track | Add Tracking info


# **identify_contact**
> IdentifyResponse identify_contact(identify_request)

Identify contact

Identify a contact by email address. If the contact already exists, it will be updated.

### Example

* Api Key Authentication (apiKeyAuth):

```python
import sendx_python_sdk
from sendx_python_sdk.models.identify_request import IdentifyRequest
from sendx_python_sdk.models.identify_response import IdentifyResponse
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
    api_instance = sendx_python_sdk.GettingStartedApi(api_client)
    identify_request = sendx_python_sdk.IdentifyRequest() # IdentifyRequest | 

    try:
        # Identify contact
        api_response = api_instance.identify_contact(identify_request)
        print("The response of GettingStartedApi->identify_contact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GettingStartedApi->identify_contact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identify_request** | [**IdentifyRequest**](IdentifyRequest.md)|  | 

### Return type

[**IdentifyResponse**](IdentifyResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The created Contact object |  -  |
**400** | Invalid request parameters. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tracking_contact**
> TrackResponse tracking_contact(track_request)

Add Tracking info

Track a contact

### Example

* Api Key Authentication (apiKeyAuth):

```python
import sendx_python_sdk
from sendx_python_sdk.models.track_request import TrackRequest
from sendx_python_sdk.models.track_response import TrackResponse
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
    api_instance = sendx_python_sdk.GettingStartedApi(api_client)
    track_request = sendx_python_sdk.TrackRequest() # TrackRequest | 

    try:
        # Add Tracking info
        api_response = api_instance.tracking_contact(track_request)
        print("The response of GettingStartedApi->tracking_contact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GettingStartedApi->tracking_contact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **track_request** | [**TrackRequest**](TrackRequest.md)|  | 

### Return type

[**TrackResponse**](TrackResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The created Contact object |  -  |
**400** | Invalid request parameters. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

