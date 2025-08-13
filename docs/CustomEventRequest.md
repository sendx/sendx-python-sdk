# CustomEventRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | This is the contact identifier. Contact id and email can be used interchangeably.  | [optional] 
**name** | **str** | Event name | 
**data** | **Dict[str, object]** | Event data | [optional] 
**time** | **int** | Unix timestamp (in seconds since January 1, 1970) representing when the event occurred. | [optional] 

## Example

```python
from sendx_python_sdk.models.custom_event_request import CustomEventRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomEventRequest from a JSON string
custom_event_request_instance = CustomEventRequest.from_json(json)
# print the JSON string representation of the object
print(CustomEventRequest.to_json())

# convert the object into a dict
custom_event_request_dict = custom_event_request_instance.to_dict()
# create an instance of CustomEventRequest from a dict
custom_event_request_from_dict = CustomEventRequest.from_dict(custom_event_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


