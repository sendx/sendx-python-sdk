# CustomEventRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the custom event (e.g., &#39;abandoned_cart&#39;). | 
**identifier** | **str** | Unique identifier for the contact (e.g., contact&#39;s email). | 
**data** | **Dict[str, str]** | Map of property-value pairs associated with the event, where both key and value are strings. | 
**time** | **int** | Unix timestamp of when the event occurred. | 

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


