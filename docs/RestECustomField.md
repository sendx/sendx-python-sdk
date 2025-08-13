# RestECustomField


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Custom field name (must be unique within team) | 
**type** | **int** | Field data type.  **Values:** - &#x60;0&#x60; - Text (max 255 characters) - &#x60;1&#x60; - Number (integer or decimal) - &#x60;2&#x60; - Date (YYYY-MM-DD format) - &#x60;3&#x60; - Boolean (true/false) - &#x60;4&#x60; - Phone number (international format)  | 
**description** | **str** | Field description for documentation | [optional] 

## Example

```python
from sendx_python_sdk.models.rest_e_custom_field import RestECustomField

# TODO update the JSON string below
json = "{}"
# create an instance of RestECustomField from a JSON string
rest_e_custom_field_instance = RestECustomField.from_json(json)
# print the JSON string representation of the object
print(RestECustomField.to_json())

# convert the object into a dict
rest_e_custom_field_dict = rest_e_custom_field_instance.to_dict()
# create an instance of RestECustomField from a dict
rest_e_custom_field_from_dict = RestECustomField.from_dict(rest_e_custom_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


