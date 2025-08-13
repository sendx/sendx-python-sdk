# XTo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**name** | **str** |  | [optional] 
**cc** | **List[str]** |  | [optional] 
**bcc** | **List[str]** |  | [optional] 
**custom_fields** | **Dict[str, str]** |  | [optional] 

## Example

```python
from sendx_python_sdk.models.xto import XTo

# TODO update the JSON string below
json = "{}"
# create an instance of XTo from a JSON string
xto_instance = XTo.from_json(json)
# print the JSON string representation of the object
print(XTo.to_json())

# convert the object into a dict
xto_dict = xto_instance.to_dict()
# create an instance of XTo from a dict
xto_from_dict = XTo.from_dict(xto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


