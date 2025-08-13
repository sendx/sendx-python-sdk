# RestRPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**post_title** | **str** |  | [optional] 
**post_description** | **str** |  | [optional] 
**post_category** | **str** |  | [optional] 
**member** | **str** |  | [optional] 
**post_thumbnail** | **str** |  | [optional] 
**is_published** | **bool** |  | [optional] 
**included_tags** | **List[str]** |  | [optional] 
**post_slug** | **str** |  | [optional] 
**status** | **int** |  | [optional] 
**page_title** | **str** |  | [optional] 
**page_description** | **str** |  | [optional] 
**page_keywords** | **str** |  | [optional] 
**social_title** | **str** |  | [optional] 
**social_description** | **str** |  | [optional] 
**social_image_url** | **str** |  | [optional] 
**created** | **datetime** |  | [optional] 
**updated** | **datetime** |  | [optional] 

## Example

```python
from sendx_python_sdk.models.rest_r_post import RestRPost

# TODO update the JSON string below
json = "{}"
# create an instance of RestRPost from a JSON string
rest_r_post_instance = RestRPost.from_json(json)
# print the JSON string representation of the object
print(RestRPost.to_json())

# convert the object into a dict
rest_r_post_dict = rest_r_post_instance.to_dict()
# create an instance of RestRPost from a dict
rest_r_post_from_dict = RestRPost.from_dict(rest_r_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


