# RestRPostTag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** | Tag name | [optional] 
**created** | **datetime** | Date and time when tag was created | [optional] 
**updated** | **datetime** | Date and time when tag was updated | [optional] 

## Example

```python
from sendx_python_sdk.models.rest_r_post_tag import RestRPostTag

# TODO update the JSON string below
json = "{}"
# create an instance of RestRPostTag from a JSON string
rest_r_post_tag_instance = RestRPostTag.from_json(json)
# print the JSON string representation of the object
print(RestRPostTag.to_json())

# convert the object into a dict
rest_r_post_tag_dict = rest_r_post_tag_instance.to_dict()
# create an instance of RestRPostTag from a dict
rest_r_post_tag_from_dict = RestRPostTag.from_dict(rest_r_post_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


