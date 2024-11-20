# RevenueEventRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Unique identifier for the contact. | 
**amount** | **float** | Recognized revenue amount associated with the event. | 
**currency** | **str** | Currency code (ISO 4217) for the revenue (e.g., &#39;USD&#39;, &#39;EUR&#39;, &#39;INR&#39;). | 
**source** | **str** | Source of the revenue (e.g., &#39;website&#39;, &#39;mobile app&#39;, &#39;partner referral&#39;). | 
**time** | **int** | Unix timestamp indicating when the revenue event occurred. | 

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


