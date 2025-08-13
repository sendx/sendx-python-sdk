# RestETag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Tag name (must be unique within team) | 

## Example

```python
from sendx_python_sdk.models.rest_e_tag import RestETag

# TODO update the JSON string below
json = "{}"
# create an instance of RestETag from a JSON string
rest_e_tag_instance = RestETag.from_json(json)
# print the JSON string representation of the object
print(RestETag.to_json())

# convert the object into a dict
rest_e_tag_dict = rest_e_tag_instance.to_dict()
# create an instance of RestETag from a dict
rest_e_tag_from_dict = RestETag.from_dict(rest_e_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


