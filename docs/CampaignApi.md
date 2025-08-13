# sendx_python_sdk.CampaignApi

All URIs are relative to *https://api.sendx.io/api/v1/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_campaign**](CampaignApi.md#create_campaign) | **POST** /campaign | Create campaign
[**delete_campaign**](CampaignApi.md#delete_campaign) | **DELETE** /campaign/{identifier} | Delete campaign
[**get_all_campaigns**](CampaignApi.md#get_all_campaigns) | **GET** /campaign | Get all campaigns
[**get_campaign**](CampaignApi.md#get_campaign) | **GET** /campaign/{identifier} | Get campaign by ID


# **create_campaign**
> RestRCampaign create_campaign(rest_e_campaign)

Create campaign

Creates a new email campaign.


### Example

* Api Key Authentication (TeamApiKey):

```python
import sendx_python_sdk
from sendx_python_sdk.models.rest_e_campaign import RestECampaign
from sendx_python_sdk.models.rest_r_campaign import RestRCampaign
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
    api_instance = sendx_python_sdk.CampaignApi(api_client)
    rest_e_campaign = {"name":"Flash Sale Announcement","subject":"⚡ 24-Hour Flash Sale - {{contact.firstName}}, Save 50%!","sender":"sender_4vK3WFhMgvOwUNyaL4QxCD","previewText":"Limited time offer - Today only!","htmlCode":"<html><body><h1>Flash Sale!</h1><p>Hi {{contact.firstName}},</p><p>Don't miss our 24-hour flash sale!</p><a href='{{sale.url}}'>Shop Now</a></body></html>","plainText":"Flash Sale!\n\nHi {{contact.firstName}},\n\nDon't miss our 24-hour flash sale!\n\nShop now: {{sale.url}}","scheduleType":1,"includedLists":["list_0tOFLp5RgV7s3LNiHrjGYs","list_vUCjsUmrVXtSppS8rD0Ssq"],"excludedTags":["tag_unengaged"]} # RestECampaign | 

    try:
        # Create campaign
        api_response = api_instance.create_campaign(rest_e_campaign)
        print("The response of CampaignApi->create_campaign:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignApi->create_campaign: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rest_e_campaign** | [**RestECampaign**](RestECampaign.md)|  | 

### Return type

[**RestRCampaign**](RestRCampaign.md)

### Authorization

[TeamApiKey](../README.md#TeamApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | ✅ Campaign created successfully |  -  |
**400** | ❌ Bad Request - Invalid input data |  -  |
**401** | ❌ Unauthorized - Invalid or missing API key |  -  |
**403** | ❌ Forbidden - Resource name already exists |  -  |
**422** | ❌ Unprocessable Entity - Invalid request format |  -  |
**500** | ❌ Internal Server Error - System error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_campaign**
> DeleteResponse delete_campaign(identifier)

Delete campaign

Deletes a campaign.


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
    api_instance = sendx_python_sdk.CampaignApi(api_client)
    identifier = 'identifier_example' # str | Campaign identifier to delete

    try:
        # Delete campaign
        api_response = api_instance.delete_campaign(identifier)
        print("The response of CampaignApi->delete_campaign:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignApi->delete_campaign: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Campaign identifier to delete | 

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
**200** | ✅ Campaign deleted successfully |  -  |
**400** | ❌ Bad Request - Invalid input data |  -  |
**401** | ❌ Unauthorized - Invalid or missing API key |  -  |
**404** | ❌ Not Found - Resource does not exist |  -  |
**500** | ❌ Internal Server Error - System error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_campaigns**
> List[RestRCampaign] get_all_campaigns(offset=offset, limit=limit, campaign_type=campaign_type)

Get all campaigns

Retrieves a paginated list of all campaigns.


### Example

* Api Key Authentication (TeamApiKey):

```python
import sendx_python_sdk
from sendx_python_sdk.models.rest_r_campaign import RestRCampaign
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
    api_instance = sendx_python_sdk.CampaignApi(api_client)
    offset = 0 # int | Number of campaigns to skip (optional) (default to 0)
    limit = 10 # int | Maximum number of campaigns to return (optional) (default to 10)
    campaign_type = all # str | Filter by campaign type (optional) (default to all)

    try:
        # Get all campaigns
        api_response = api_instance.get_all_campaigns(offset=offset, limit=limit, campaign_type=campaign_type)
        print("The response of CampaignApi->get_all_campaigns:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignApi->get_all_campaigns: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| Number of campaigns to skip | [optional] [default to 0]
 **limit** | **int**| Maximum number of campaigns to return | [optional] [default to 10]
 **campaign_type** | **str**| Filter by campaign type | [optional] [default to all]

### Return type

[**List[RestRCampaign]**](RestRCampaign.md)

### Authorization

[TeamApiKey](../README.md#TeamApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ✅ Campaigns retrieved successfully |  -  |
**401** | ❌ Unauthorized - Invalid or missing API key |  -  |
**500** | ❌ Internal Server Error - System error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_campaign**
> RestRCampaign get_campaign(identifier)

Get campaign by ID

Retrieves detailed information about a specific campaign.


### Example

* Api Key Authentication (TeamApiKey):

```python
import sendx_python_sdk
from sendx_python_sdk.models.rest_r_campaign import RestRCampaign
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
    api_instance = sendx_python_sdk.CampaignApi(api_client)
    identifier = 'identifier_example' # str | Campaign identifier - `campaign_IMBoxK2iB5sUdgiNOjqAMA` 

    try:
        # Get campaign by ID
        api_response = api_instance.get_campaign(identifier)
        print("The response of CampaignApi->get_campaign:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignApi->get_campaign: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**| Campaign identifier - &#x60;campaign_IMBoxK2iB5sUdgiNOjqAMA&#x60;  | 

### Return type

[**RestRCampaign**](RestRCampaign.md)

### Authorization

[TeamApiKey](../README.md#TeamApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ✅ Campaign retrieved successfully |  -  |
**400** | ❌ Bad Request - Invalid input data |  -  |
**401** | ❌ Unauthorized - Invalid or missing API key |  -  |
**404** | ❌ Not Found - Resource does not exist |  -  |
**500** | ❌ Internal Server Error - System error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

