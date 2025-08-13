# sendx_python_sdk.EventApi

All URIs are relative to *https://api.sendx.io/api/v1/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**events_custom_postback_get**](EventApi.md#events_custom_postback_get) | **GET** /events/custom/postback | Custom Event Postback URL
[**events_revenue_postback_get**](EventApi.md#events_revenue_postback_get) | **GET** /events/revenue/postback | Revenue Event Postback URL


# **events_custom_postback_get**
> EventsRevenuePostbackGet200Response events_custom_postback_get(team_id, id, event, any_key)

Custom Event Postback URL

Register a custom event for a specific team and event.

### Example

* Api Key Authentication (TeamApiKey):

```python
import sendx_python_sdk
from sendx_python_sdk.models.events_revenue_postback_get200_response import EventsRevenuePostbackGet200Response
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
    api_instance = sendx_python_sdk.EventApi(api_client)
    team_id = 'team_id_example' # str | The unique identifier for the team.
    id = 'id_example' # str | The unique sendx identifier for the contact/customer.
    event = 'event_example' # str | The custom event name.
    any_key = '24.43' # str | Arbitrary custom data as key-value pairs. Add custom parameters directly to the query string.  For example, `amount=24.43` or `currency=USD`. 

    try:
        # Custom Event Postback URL
        api_response = api_instance.events_custom_postback_get(team_id, id, event, any_key)
        print("The response of EventApi->events_custom_postback_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventApi->events_custom_postback_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| The unique identifier for the team. | 
 **id** | **str**| The unique sendx identifier for the contact/customer. | 
 **event** | **str**| The custom event name. | 
 **any_key** | **str**| Arbitrary custom data as key-value pairs. Add custom parameters directly to the query string.  For example, &#x60;amount&#x3D;24.43&#x60; or &#x60;currency&#x3D;USD&#x60;.  | 

### Return type

[**EventsRevenuePostbackGet200Response**](EventsRevenuePostbackGet200Response.md)

### Authorization

[TeamApiKey](../README.md#TeamApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **events_revenue_postback_get**
> EventsRevenuePostbackGet200Response events_revenue_postback_get(team_id, id, amount, campaign_id)

Revenue Event Postback URL

Trigger a revenue postback for a specific team and event.

### Example

* Api Key Authentication (TeamApiKey):

```python
import sendx_python_sdk
from sendx_python_sdk.models.events_revenue_postback_get200_response import EventsRevenuePostbackGet200Response
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
    api_instance = sendx_python_sdk.EventApi(api_client)
    team_id = 'team_id_example' # str | The unique identifier for the team.
    id = 'id_example' # str | The unique sendx identifier for the contact/customer.
    amount = 3.4 # float | The revenue amount to be posted back.
    campaign_id = 'campaign_id_example' # str | The unique identifier for the campaign.

    try:
        # Revenue Event Postback URL
        api_response = api_instance.events_revenue_postback_get(team_id, id, amount, campaign_id)
        print("The response of EventApi->events_revenue_postback_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventApi->events_revenue_postback_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| The unique identifier for the team. | 
 **id** | **str**| The unique sendx identifier for the contact/customer. | 
 **amount** | **float**| The revenue amount to be posted back. | 
 **campaign_id** | **str**| The unique identifier for the campaign. | 

### Return type

[**EventsRevenuePostbackGet200Response**](EventsRevenuePostbackGet200Response.md)

### Authorization

[TeamApiKey](../README.md#TeamApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

