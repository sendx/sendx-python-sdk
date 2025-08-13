# sendx_python_sdk.TrackingApi

All URIs are relative to *https://api.sendx.io/api/v1/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**identify_contact**](TrackingApi.md#identify_contact) | **POST** /contact/identify | Identify contact
[**track_contact**](TrackingApi.md#track_contact) | **POST** /contact/track | Track contact


# **identify_contact**
> IdentifyResponse identify_contact(identify_request)

Identify contact

Legacy endpoint for identifying contacts. Creates or updates a contact.


**🎯 Key Features:**
- Creates contact if doesn't exist
- Updates if email already exists
- Supports custom fields and tags


### Example

* Api Key Authentication (TeamApiKey):

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

# Configure API key authorization: TeamApiKey
configuration.api_key['TeamApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TeamApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with sendx_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sendx_python_sdk.TrackingApi(api_client)
    identify_request = {"email":"john.doe@example.com"} # IdentifyRequest | 

    try:
        # Identify contact
        api_response = api_instance.identify_contact(identify_request)
        print("The response of TrackingApi->identify_contact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackingApi->identify_contact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identify_request** | [**IdentifyRequest**](IdentifyRequest.md)|  | 

### Return type

[**IdentifyResponse**](IdentifyResponse.md)

### Authorization

[TeamApiKey](../README.md#TeamApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ✅ Contact identified successfully |  -  |
**401** | ❌ Unauthorized - Invalid or missing API key |  -  |
**422** | ❌ Unprocessable Entity - Invalid request format |  -  |
**500** | ❌ Internal Server Error - System error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **track_contact**
> TrackResponse track_contact(track_request)

Track contact

Legacy endpoint for tracking contact behavior through tags.


**🎯 Key Features:**
- Add or remove tags
- Trigger automations
- Track user behavior


### Example

* Api Key Authentication (TeamApiKey):

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

# Configure API key authorization: TeamApiKey
configuration.api_key['TeamApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TeamApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with sendx_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sendx_python_sdk.TrackingApi(api_client)
    track_request = {"email":"test@example.com","addTags":["new","cool"],"removeTags":["old","bad"]} # TrackRequest | 

    try:
        # Track contact
        api_response = api_instance.track_contact(track_request)
        print("The response of TrackingApi->track_contact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrackingApi->track_contact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **track_request** | [**TrackRequest**](TrackRequest.md)|  | 

### Return type

[**TrackResponse**](TrackResponse.md)

### Authorization

[TeamApiKey](../README.md#TeamApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ✅ Contact tracked successfully |  -  |
**401** | ❌ Unauthorized - Invalid or missing API key |  -  |
**404** | ❌ Not Found - Resource does not exist |  -  |
**422** | ❌ Unprocessable Entity - Invalid request format |  -  |
**500** | ❌ Internal Server Error - System error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

