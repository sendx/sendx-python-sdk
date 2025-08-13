# EventsRevenuePostbackGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from sendx_python_sdk.models.events_revenue_postback_get200_response import EventsRevenuePostbackGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of EventsRevenuePostbackGet200Response from a JSON string
events_revenue_postback_get200_response_instance = EventsRevenuePostbackGet200Response.from_json(json)
# print the JSON string representation of the object
print(EventsRevenuePostbackGet200Response.to_json())

# convert the object into a dict
events_revenue_postback_get200_response_dict = events_revenue_postback_get200_response_instance.to_dict()
# create an instance of EventsRevenuePostbackGet200Response from a dict
events_revenue_postback_get200_response_from_dict = EventsRevenuePostbackGet200Response.from_dict(events_revenue_postback_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


