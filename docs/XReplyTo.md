# XReplyTo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**name** | **str** |  | [optional] 

## Example

```python
from sendx_python_sdk.models.x_reply_to import XReplyTo

# TODO update the JSON string below
json = "{}"
# create an instance of XReplyTo from a JSON string
x_reply_to_instance = XReplyTo.from_json(json)
# print the JSON string representation of the object
print(XReplyTo.to_json())

# convert the object into a dict
x_reply_to_dict = x_reply_to_instance.to_dict()
# create an instance of XReplyTo from a dict
x_reply_to_from_dict = XReplyTo.from_dict(x_reply_to_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


