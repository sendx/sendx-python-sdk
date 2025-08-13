# RestRTag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique tag identifier with tag_ prefix | [optional] 
**name** | **str** | Tag name | [optional] 
**created** | **datetime** | Tag creation timestamp | [optional] 
**updated** | **datetime** | Tag last update timestamp | [optional] 

## Example

```python
from sendx_python_sdk.models.rest_r_tag import RestRTag

# TODO update the JSON string below
json = "{}"
# create an instance of RestRTag from a JSON string
rest_r_tag_instance = RestRTag.from_json(json)
# print the JSON string representation of the object
print(RestRTag.to_json())

# convert the object into a dict
rest_r_tag_dict = rest_r_tag_instance.to_dict()
# create an instance of RestRTag from a dict
rest_r_tag_from_dict = RestRTag.from_dict(rest_r_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


