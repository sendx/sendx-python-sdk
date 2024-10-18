# sendx_python_sdk.SenderApi

All URIs are relative to *https://api.sendx.io/api/v1/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sender**](SenderApi.md#create_sender) | **POST** /sender | Create Sender
[**get_all_senders**](SenderApi.md#get_all_senders) | **GET** /sender | Get All Senders


# **create_sender**
> Sender create_sender(sender_request)

Create Sender

Creates a new sender in the system.

### Example

* Api Key Authentication (apiKeyAuth):

```python
import sendx_python_sdk
from sendx_python_sdk.models.sender import Sender
from sendx_python_sdk.models.sender_request import SenderRequest
from sendx_python_sdk.rest import ApiException
from pprint import pprint


configuration = sendx_python_sdk.Configuration()



# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.environ["API_KEY"]



# Enter a context with an instance of the API client
with sendx_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sendx_python_sdk.SenderApi(api_client)
    sender_request = sendx_python_sdk.SenderRequest() # SenderRequest | 

    try:
        # Create Sender
        api_response = api_instance.create_sender(sender_request)
        print("The response of SenderApi->create_sender:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SenderApi->create_sender: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sender_request** | [**SenderRequest**](SenderRequest.md)|  | 

### Return type

[**Sender**](Sender.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sender Created Successfully |  -  |
**401** | Not Authorized |  -  |
**403** | Forbidden - Tag with name already exists |  -  |
**406** | Not Acceptable |  -  |
**422** | Unprocessable Entity - Request body is not in the proper format |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_senders**
> List[SenderResponse] get_all_senders(offset=offset, limit=limit, search=search)

Get All Senders

Retrieve all senders for the team, with optional filters like offset, limit, and search.

### Example

* Api Key Authentication (apiKeyAuth):

```python
import sendx_python_sdk
from sendx_python_sdk.models.sender_response import SenderResponse
from sendx_python_sdk.rest import ApiException
from pprint import pprint


configuration = sendx_python_sdk.Configuration()



# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.environ["API_KEY"]



# Enter a context with an instance of the API client
with sendx_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sendx_python_sdk.SenderApi(api_client)
    offset = 0 # int | Number of records to skip (optional) (default to 0)
    limit = 10 # int | Maximum number of records to return (optional) (default to 10)
    search = 'search_example' # str | Search keyword to filter senders by name or email (optional)

    try:
        # Get All Senders
        api_response = api_instance.get_all_senders(offset=offset, limit=limit, search=search)
        print("The response of SenderApi->get_all_senders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SenderApi->get_all_senders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| Number of records to skip | [optional] [default to 0]
 **limit** | **int**| Maximum number of records to return | [optional] [default to 10]
 **search** | **str**| Search keyword to filter senders by name or email | [optional] 

### Return type

[**List[SenderResponse]**](SenderResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieved all senders for team successfully |  -  |
**401** | Not Authorized |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

