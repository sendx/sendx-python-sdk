# sendx_python_sdk.ReportsApi

All URIs are relative to *https://api.sendx.io/api/v1/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_campaign_report**](ReportsApi.md#get_campaign_report) | **GET** /report/campaign/{campaignId} | Get CampaignReport Data


# **get_campaign_report**
> ReportData get_campaign_report(campaign_id, integration_type=integration_type)

Get CampaignReport Data

Retrieve the campaign report data based on the provided campaign id.

### Example

* Api Key Authentication (apiKeyAuth):

```python
import sendx_python_sdk
from sendx_python_sdk.models.report_data import ReportData
from sendx_python_sdk.rest import ApiException
from pprint import pprint


configuration = sendx_python_sdk.Configuration()



# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.environ["API_KEY"]



# Enter a context with an instance of the API client
with sendx_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sendx_python_sdk.ReportsApi(api_client)
    campaign_id = 'campaign_id_example' # str | The ID of the campaign to retrieve the report data for
    integration_type = 'integration_type_example' # str | Type of integration for the report data (optional) (optional)

    try:
        # Get CampaignReport Data
        api_response = api_instance.get_campaign_report(campaign_id, integration_type=integration_type)
        print("The response of ReportsApi->get_campaign_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->get_campaign_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| The ID of the campaign to retrieve the report data for | 
 **integration_type** | **str**| Type of integration for the report data (optional) | [optional] 

### Return type

[**ReportData**](ReportData.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get Report Data Successfully |  -  |
**401** | Not Authorized |  -  |
**403** | Forbidden Tag with name already exists |  -  |
**406** | Not Acceptable |  -  |
**422** | Request body is not in proper format |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

