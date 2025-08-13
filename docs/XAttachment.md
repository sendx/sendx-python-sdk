# XAttachment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filename** | **str** |  | 
**content** | **bytearray** |  | 

## Example

```python
from sendx_python_sdk.models.x_attachment import XAttachment

# TODO update the JSON string below
json = "{}"
# create an instance of XAttachment from a JSON string
x_attachment_instance = XAttachment.from_json(json)
# print the JSON string representation of the object
print(XAttachment.to_json())

# convert the object into a dict
x_attachment_dict = x_attachment_instance.to_dict()
# create an instance of XAttachment from a dict
x_attachment_from_dict = XAttachment.from_dict(x_attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


