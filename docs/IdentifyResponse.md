# IdentifyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from sendx_python_sdk.models.identify_response import IdentifyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IdentifyResponse from a JSON string
identify_response_instance = IdentifyResponse.from_json(json)
# print the JSON string representation of the object
print(IdentifyResponse.to_json())

# convert the object into a dict
identify_response_dict = identify_response_instance.to_dict()
# create an instance of IdentifyResponse from a dict
identify_response_from_dict = IdentifyResponse.from_dict(identify_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


