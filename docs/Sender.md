# Sender


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the sender | 
**name** | **str** | Name of the sender | 
**email** | **str** | Email address of the sender | 

## Example

```python
from sendx_python_sdk.models.sender import Sender

# TODO update the JSON string below
json = "{}"
# create an instance of Sender from a JSON string
sender_instance = Sender.from_json(json)
# print the JSON string representation of the object
print(Sender.to_json())

# convert the object into a dict
sender_dict = sender_instance.to_dict()
# create an instance of Sender from a dict
sender_from_dict = Sender.from_dict(sender_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


