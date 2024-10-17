# CreateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**success** | **bool** |  | [optional] 

## Example

```python
from sendx_python_sdk.models.create_response import CreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateResponse from a JSON string
create_response_instance = CreateResponse.from_json(json)
# print the JSON string representation of the object
print(CreateResponse.to_json())

# convert the object into a dict
create_response_dict = create_response_instance.to_dict()
# create an instance of CreateResponse from a dict
create_response_from_dict = CreateResponse.from_dict(create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


