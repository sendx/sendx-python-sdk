# sendx_python_sdk.CampaignApi

All URIs are relative to *https://api.sendx.io/api/v1/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_campaign**](CampaignApi.md#create_campaign) | **POST** /campaign | Create Campaign
[**delete_campaign**](CampaignApi.md#delete_campaign) | **DELETE** /campaign/{campaignId} | Delete Campaign
[**edit_campaign**](CampaignApi.md#edit_campaign) | **PUT** /campaign/{campaignId} | Edit Campaign
[**get_all_campaigns**](CampaignApi.md#get_all_campaigns) | **GET** /campaign | Get All Campaigns
[**get_campaign_by_id**](CampaignApi.md#get_campaign_by_id) | **GET** /campaign/{campaignId} | Get Campaign By Id


# **create_campaign**
> CreateResponse create_campaign(campaign_request)

Create Campaign

Create a new email campaign

### Example

* Api Key Authentication (apiKeyAuth):

```python
import sendx_python_sdk
from sendx_python_sdk.models.campaign_request import CampaignRequest
from sendx_python_sdk.models.create_response import CreateResponse
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
    api_instance = sendx_python_sdk.CampaignApi(api_client)
    campaign_request = sendx_python_sdk.CampaignRequest() # CampaignRequest | The campaign content

    try:
        # Create Campaign
        api_response = api_instance.create_campaign(campaign_request)
        print("The response of CampaignApi->create_campaign:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignApi->create_campaign: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_request** | [**CampaignRequest**](CampaignRequest.md)| The campaign content | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Campaign Created Successfully |  -  |
**401** | Not Authorized |  -  |
**403** | Forbidden - Tag with name already exists |  -  |
**406** | Not Acceptable |  -  |
**422** | Request body is not in proper format |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_campaign**
> DeleteCampaign200Response delete_campaign(campaign_id)

Delete Campaign

Deletes a specific campaign by its campaignId.

### Example

* Api Key Authentication (apiKeyAuth):

```python
import sendx_python_sdk
from sendx_python_sdk.models.delete_campaign200_response import DeleteCampaign200Response
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
    api_instance = sendx_python_sdk.CampaignApi(api_client)
    campaign_id = 'campaign_id_example' # str | The ID of the campaign to delete

    try:
        # Delete Campaign
        api_response = api_instance.delete_campaign(campaign_id)
        print("The response of CampaignApi->delete_campaign:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignApi->delete_campaign: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| The ID of the campaign to delete | 

### Return type

[**DeleteCampaign200Response**](DeleteCampaign200Response.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Campaign deleted successfully |  -  |
**401** | Not Authorized |  -  |
**406** | Campaign ID is empty |  -  |
**422** | Request body is not in proper format |  -  |
**500** | Internal Server Err |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_campaign**
> Campaign edit_campaign(campaign_id, campaign_request)

Edit Campaign

Submit edited content for a specific campaign.

### Example

* Api Key Authentication (apiKeyAuth):

```python
import sendx_python_sdk
from sendx_python_sdk.models.campaign import Campaign
from sendx_python_sdk.models.campaign_request import CampaignRequest
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
    api_instance = sendx_python_sdk.CampaignApi(api_client)
    campaign_id = 'campaign_id_example' # str | The ID of the campaign to edit
    campaign_request = sendx_python_sdk.CampaignRequest() # CampaignRequest | 

    try:
        # Edit Campaign
        api_response = api_instance.edit_campaign(campaign_id, campaign_request)
        print("The response of CampaignApi->edit_campaign:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignApi->edit_campaign: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| The ID of the campaign to edit | 
 **campaign_request** | [**CampaignRequest**](CampaignRequest.md)|  | 

### Return type

[**Campaign**](Campaign.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Campaign edited successfully |  -  |
**401** | Not Authorized |  -  |
**406** | Not Acceptable |  -  |
**403** | Forbidden - Tag with name already exists |  -  |
**422** | Request body is not in proper format |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_campaigns**
> List[Campaign] get_all_campaigns(offset=offset, limit=limit, search=search)

Get All Campaigns

Retrieve a list of all campaigns.

### Example

* Api Key Authentication (apiKeyAuth):

```python
import sendx_python_sdk
from sendx_python_sdk.models.campaign import Campaign
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
    api_instance = sendx_python_sdk.CampaignApi(api_client)
    offset = 0 # int | Offset for pagination (optional) (default to 0)
    limit = 20 # int | Limit for pagination (optional) (default to 20)
    search = 'search_example' # str | Search term to filter campaigns (optional)

    try:
        # Get All Campaigns
        api_response = api_instance.get_all_campaigns(offset=offset, limit=limit, search=search)
        print("The response of CampaignApi->get_all_campaigns:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignApi->get_all_campaigns: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| Offset for pagination | [optional] [default to 0]
 **limit** | **int**| Limit for pagination | [optional] [default to 20]
 **search** | **str**| Search term to filter campaigns | [optional] 

### Return type

[**List[Campaign]**](Campaign.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieved campaigns successfully. |  -  |
**401** | Not Authorized - Invalid or missing API key. |  -  |
**500** | Internal Server Error - Something went wrong on the server. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_campaign_by_id**
> Campaign get_campaign_by_id(campaign_id)

Get Campaign By Id

Retrieve a specific campaign using its ID.

### Example

* Api Key Authentication (apiKeyAuth):

```python
import sendx_python_sdk
from sendx_python_sdk.models.campaign import Campaign
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
    api_instance = sendx_python_sdk.CampaignApi(api_client)
    campaign_id = 'campaign_id_example' # str | The ID of the campaign to retrieve.

    try:
        # Get Campaign By Id
        api_response = api_instance.get_campaign_by_id(campaign_id)
        print("The response of CampaignApi->get_campaign_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CampaignApi->get_campaign_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| The ID of the campaign to retrieve. | 

### Return type

[**Campaign**](Campaign.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieved campaign successfully. |  -  |
**401** | Not Authorized - Invalid or missing API key. |  -  |
**406** | Not Acceptable - Request not acceptable. |  -  |
**403** | Forbidden - Tag with name already exists. |  -  |
**422** | Request body is not in proper format. |  -  |
**500** | Internal Server Error - Something went wrong on the server. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

