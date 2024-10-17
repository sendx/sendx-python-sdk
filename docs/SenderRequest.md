# SenderRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the sender | 
**email** | **str** | Email address of the sender | 

## Example

```python
from sendx_python_sdk.models.sender_request import SenderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SenderRequest from a JSON string
sender_request_instance = SenderRequest.from_json(json)
# print the JSON string representation of the object
print(SenderRequest.to_json())

# convert the object into a dict
sender_request_dict = sender_request_instance.to_dict()
# create an instance of SenderRequest from a dict
sender_request_from_dict = SenderRequest.from_dict(sender_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


