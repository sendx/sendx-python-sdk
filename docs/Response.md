# Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The status of the response. | [optional] 
**message** | **str** | A message indicating the result of the operation. | [optional] 
**data** | **str** | Additional data associated with the response. | [optional] 

## Example

```python
from sendx_python_sdk.models.response import Response

# TODO update the JSON string below
json = "{}"
# create an instance of Response from a JSON string
response_instance = Response.from_json(json)
# print the JSON string representation of the object
print(Response.to_json())

# convert the object into a dict
response_dict = response_instance.to_dict()
# create an instance of Response from a dict
response_from_dict = Response.from_dict(response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


