# TrackRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | [**Email**](Email.md) | Email address of the contact to track. | [optional] 
**add_tags** | **List[str]** |  | [optional] 
**remove_tags** | **List[str]** |  | [optional] 

## Example

```python
from sendx_python_sdk.models.track_request import TrackRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TrackRequest from a JSON string
track_request_instance = TrackRequest.from_json(json)
# print the JSON string representation of the object
print(TrackRequest.to_json())

# convert the object into a dict
track_request_dict = track_request_instance.to_dict()
# create an instance of TrackRequest from a dict
track_request_from_dict = TrackRequest.from_dict(track_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


