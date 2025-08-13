# IdentifyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**company** | **str** |  | [optional] 
**custom_fields** | **Dict[str, str]** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**new_email** | **str** | New email when updating existing contact | [optional] 

## Example

```python
from sendx_python_sdk.models.identify_request import IdentifyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IdentifyRequest from a JSON string
identify_request_instance = IdentifyRequest.from_json(json)
# print the JSON string representation of the object
print(IdentifyRequest.to_json())

# convert the object into a dict
identify_request_dict = identify_request_instance.to_dict()
# create an instance of IdentifyRequest from a dict
identify_request_from_dict = IdentifyRequest.from_dict(identify_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


