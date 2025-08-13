# sendx_python_sdk.EventsApi

All URIs are relative to *https://api.sendx.io/api/v1/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**track_custom_event**](EventsApi.md#track_custom_event) | **POST** /events/custom | Track custom event
[**track_revenue_event**](EventsApi.md#track_revenue_event) | **POST** /events/revenue | Track revenue event


# **track_custom_event**
> EventResponse track_custom_event(custom_event_request)

Track custom event

Records custom events for advanced tracking.


### Example

* Api Key Authentication (TeamApiKey):

```python
import sendx_python_sdk
from sendx_python_sdk.models.custom_event_request import CustomEventRequest
from sendx_python_sdk.models.event_response import EventResponse
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
    api_instance = sendx_python_sdk.EventsApi(api_client)
    custom_event_request = {"identifier":"user@example.com","name":"video_watched","data":{"video_id":"12345","duration":"120","completed":"true"},"time":1669990400} # CustomEventRequest | 

    try:
        # Track custom event
        api_response = api_instance.track_custom_event(custom_event_request)
        print("The response of EventsApi->track_custom_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->track_custom_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_event_request** | [**CustomEventRequest**](CustomEventRequest.md)|  | 

### Return type

[**EventResponse**](EventResponse.md)

### Authorization

[TeamApiKey](../README.md#TeamApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ✅ Custom event tracked successfully |  -  |
**401** | ❌ Unauthorized - Invalid or missing API key |  -  |
**422** | ❌ Unprocessable Entity - Invalid request format |  -  |
**500** | ❌ Internal Server Error - System error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **track_revenue_event**
> EventResponse track_revenue_event(revenue_event_request)

Track revenue event

Records revenue events for analytics and attribution.


### Example

* Api Key Authentication (TeamApiKey):

```python
import sendx_python_sdk
from sendx_python_sdk.models.event_response import EventResponse
from sendx_python_sdk.models.revenue_event_request import RevenueEventRequest
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
    api_instance = sendx_python_sdk.EventsApi(api_client)
    revenue_event_request = sendx_python_sdk.RevenueEventRequest() # RevenueEventRequest | 

    try:
        # Track revenue event
        api_response = api_instance.track_revenue_event(revenue_event_request)
        print("The response of EventsApi->track_revenue_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->track_revenue_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **revenue_event_request** | [**RevenueEventRequest**](RevenueEventRequest.md)|  | 

### Return type

[**EventResponse**](EventResponse.md)

### Authorization

[TeamApiKey](../README.md#TeamApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ✅ Revenue event tracked successfully |  -  |
**401** | ❌ Unauthorized - Invalid or missing API key |  -  |
**422** | ❌ Unprocessable Entity - Invalid request format |  -  |
**500** | ❌ Internal Server Error - System error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

