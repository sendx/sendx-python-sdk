# RevenueEventRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Contact email address | 
**amount** | **float** | Revenue amount | 
**source** | **str** | Source of the revenue event | [optional] 
**time** | **int** | Unix timestamp (in seconds since January 1, 1970) representing when the event occurred. | [optional] 

## Example

```python
from sendx_python_sdk.models.revenue_event_request import RevenueEventRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RevenueEventRequest from a JSON string
revenue_event_request_instance = RevenueEventRequest.from_json(json)
# print the JSON string representation of the object
print(RevenueEventRequest.to_json())

# convert the object into a dict
revenue_event_request_dict = revenue_event_request_instance.to_dict()
# create an instance of RevenueEventRequest from a dict
revenue_event_request_from_dict = RevenueEventRequest.from_dict(revenue_event_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


