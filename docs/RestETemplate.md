# RestETemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Template name | 
**subject** | **str** | Email subject line | 
**html_content** | **str** | HTML email content | [optional] 
**text_content** | **str** | Plain text content | [optional] 
**preheader** | **str** | Preview text | [optional] 
**tags** | **List[str]** | Template tags for organization | [optional] 

## Example

```python
from sendx_python_sdk.models.rest_e_template import RestETemplate

# TODO update the JSON string below
json = "{}"
# create an instance of RestETemplate from a JSON string
rest_e_template_instance = RestETemplate.from_json(json)
# print the JSON string representation of the object
print(RestETemplate.to_json())

# convert the object into a dict
rest_e_template_dict = rest_e_template_instance.to_dict()
# create an instance of RestETemplate from a dict
rest_e_template_from_dict = RestETemplate.from_dict(rest_e_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


