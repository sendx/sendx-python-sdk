# RestRPostCategory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id for the post category | [optional] 
**name** | **str** | Name for the post category | [optional] 
**created** | **datetime** | Date and time when the post category was created | [optional] 
**updated** | **datetime** | Date and time when the post category was last updated | [optional] 

## Example

```python
from sendx_python_sdk.models.rest_r_post_category import RestRPostCategory

# TODO update the JSON string below
json = "{}"
# create an instance of RestRPostCategory from a JSON string
rest_r_post_category_instance = RestRPostCategory.from_json(json)
# print the JSON string representation of the object
print(RestRPostCategory.to_json())

# convert the object into a dict
rest_r_post_category_dict = rest_r_post_category_instance.to_dict()
# create an instance of RestRPostCategory from a dict
rest_r_post_category_from_dict = RestRPostCategory.from_dict(rest_r_post_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


