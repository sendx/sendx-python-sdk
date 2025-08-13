# RestRCustomField


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique field identifier with field_ prefix | [optional] 
**name** | **str** | Custom field name | [optional] 
**type** | **int** | Field data type.  **Values:** - &#x60;0&#x60; - Text (max 255 characters) - &#x60;1&#x60; - Number (integer or decimal) - &#x60;2&#x60; - Date (YYYY-MM-DD format) - &#x60;3&#x60; - Boolean (true/false) - &#x60;4&#x60; - Phone number (international format)  | [optional] 
**description** | **str** | Field description for documentation | [optional] 

## Example

```python
from sendx_python_sdk.models.rest_r_custom_field import RestRCustomField

# TODO update the JSON string below
json = "{}"
# create an instance of RestRCustomField from a JSON string
rest_r_custom_field_instance = RestRCustomField.from_json(json)
# print the JSON string representation of the object
print(RestRCustomField.to_json())

# convert the object into a dict
rest_r_custom_field_dict = rest_r_custom_field_instance.to_dict()
# create an instance of RestRCustomField from a dict
rest_r_custom_field_from_dict = RestRCustomField.from_dict(rest_r_custom_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


