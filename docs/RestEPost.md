# RestEPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Internal post name | 
**post_title** | **str** | Public post title | 
**post_description** | **str** | Post excerpt/description | [optional] 
**post_category** | **str** | Category ID (with or without prefix) | [optional] 
**member** | **str** | Author member ID | [optional] 
**post_thumbnail** | **str** | Thumbnail image URL | [optional] 
**post_html** | **str** | Post HTML content | [optional] 
**post_template** | **str** | Post template | [optional] 
**is_published** | **bool** | Publication status | [optional] [default to False]
**included_tags** | **List[str]** | Post tag IDs | [optional] 
**editor_type** | **int** | Editor type used | [optional] [default to 1]
**post_slug** | **str** | URL slug | [optional] 
**status** | **int** | Post status | [optional] [default to 1]
**page_title** | **str** | SEO page title | [optional] 
**page_description** | **str** | SEO meta description | [optional] 
**page_keywords** | **str** | SEO keywords | [optional] 
**social_title** | **str** | Social media title | [optional] 
**social_description** | **str** | Social media description | [optional] 
**social_image_url** | **str** | Social media image URL | [optional] 

## Example

```python
from sendx_python_sdk.models.rest_e_post import RestEPost

# TODO update the JSON string below
json = "{}"
# create an instance of RestEPost from a JSON string
rest_e_post_instance = RestEPost.from_json(json)
# print the JSON string representation of the object
print(RestEPost.to_json())

# convert the object into a dict
rest_e_post_dict = rest_e_post_instance.to_dict()
# create an instance of RestEPost from a dict
rest_e_post_from_dict = RestEPost.from_dict(rest_e_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


