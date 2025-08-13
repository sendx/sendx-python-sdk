# RestRTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique template identifier with template_ prefix | [optional] 
**name** | **str** | Name of the template | [optional] 
**subject** | **str** | Email subject line (if applicable) | [optional] 
**html_code** | **str** | HTML content of the template | [optional] 
**template_code** | **str** | Template code for visual editors (JSON structure) | [optional] 
**type** | **int** | Template type.  **Values:** - &#x60;0&#x60; - Email template - &#x60;1&#x60; - Other types  | [optional] 
**thumbnail** | **str** | URL to template thumbnail image | [optional] 
**editor_type** | **int** | Editor type used to create the template.  **Values:** - &#x60;0&#x60; - PlainText - &#x60;1&#x60; - DragDrop - &#x60;2&#x60; - SendxEditor  | [optional] 
**created** | **datetime** | Template creation timestamp | [optional] 
**updated** | **datetime** | Template last update timestamp | [optional] 

## Example

```python
from sendx_python_sdk.models.rest_r_template import RestRTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of RestRTemplate from a JSON string
rest_r_template_instance = RestRTemplate.from_json(json)
# print the JSON string representation of the object
print(RestRTemplate.to_json())

# convert the object into a dict
rest_r_template_dict = rest_r_template_instance.to_dict()
# create an instance of RestRTemplate from a dict
rest_r_template_from_dict = RestRTemplate.from_dict(rest_r_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


