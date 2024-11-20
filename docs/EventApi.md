# sendx_python_sdk.EventApi

All URIs are relative to *https://api.sendx.io/api/v1/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_revenue_event**](EventApi.md#create_revenue_event) | **POST** /events/revenue | Record a revenue event for a specific contact
[**push_custom_event**](EventApi.md#push_custom_event) | **POST** /events/custom | Push a custom event associated with a contact


# **create_revenue_event**
> EventResponse create_revenue_event(revenue_event_request)

Record a revenue event for a specific contact

Records a revenue event, which can be attributed to campaigns, drips, workflows, or other sources of user interaction.

### Example

* Api Key Authentication (apiKeyAuth):

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

# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with sendx_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sendx_python_sdk.EventApi(api_client)
    revenue_event_request = sendx_python_sdk.RevenueEventRequest() # RevenueEventRequest | 

    try:
        # Record a revenue event for a specific contact
        api_response = api_instance.create_revenue_event(revenue_event_request)
        print("The response of EventApi->create_revenue_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventApi->create_revenue_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **revenue_event_request** | [**RevenueEventRequest**](RevenueEventRequest.md)|  | 

### Return type

[**EventResponse**](EventResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Revenue event recorded successfully. |  -  |
**400** | Invalid request parameters. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **push_custom_event**
> EventResponse push_custom_event(custom_event_request)

Push a custom event associated with a contact

Pushes a custom event with properties and values for a specified contact.

### Example

* Api Key Authentication (apiKeyAuth):

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

# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with sendx_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sendx_python_sdk.EventApi(api_client)
    custom_event_request = sendx_python_sdk.CustomEventRequest() # CustomEventRequest | 

    try:
        # Push a custom event associated with a contact
        api_response = api_instance.push_custom_event(custom_event_request)
        print("The response of EventApi->push_custom_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventApi->push_custom_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_event_request** | [**CustomEventRequest**](CustomEventRequest.md)|  | 

### Return type

[**EventResponse**](EventResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Custom event created successfully. |  -  |
**400** | Invalid request parameters. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

