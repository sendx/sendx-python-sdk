# ECustomField


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the custom field. | [optional] 
**type** | **int** | Type of the custom field. | [optional] 
**shown** | **bool** | Whether the custom field is shown. | [optional] 
**is_shareable** | **bool** | Whether the custom field is shareable. | [optional] 
**description** | **str** | Description of the custom field. | [optional] 

## Example

```python
from sendx_python_sdk.models.e_custom_field import ECustomField

# TODO update the JSON string below
json = "{}"
# create an instance of ECustomField from a JSON string
e_custom_field_instance = ECustomField.from_json(json)
# print the JSON string representation of the object
print(ECustomField.to_json())

# convert the object into a dict
e_custom_field_dict = e_custom_field_instance.to_dict()
# create an instance of ECustomField from a dict
e_custom_field_from_dict = ECustomField.from_dict(e_custom_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


