# RestEContact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | First name of the contact | [optional] 
**last_name** | **str** | Last name of the contact | [optional] 
**email** | **str** | Email address of the contact (required and must be unique within team).  **Validation:** - Must be a valid email format - Must be unique within the team - Cannot be empty or null  | 
**company** | **str** | Company name of the contact | [optional] 
**custom_fields** | **Dict[str, str]** | Custom fields as key-value pairs. Keys should use &#x60;field_&#x60; prefix.  **Processing:** - Keys are case-sensitive - Values are stored as strings  **Examples:** - &#x60;\&quot;field_MnuqBAG2NPLm7PZMWbjQxt\&quot;: \&quot;Engineering\&quot;&#x60; → stored as &#x60;department: Engineering&#x60;  | [optional] 
**lists** | **List[str]** | Array of list identifiers to associate with the contact.  Identifiers should use &#x60;list_&#x60; prefix.  **Processing:** - Invalid list IDs will send our 400 error - Duplicates will be removed  **Examples:** - &#x60;\&quot;list_OcuxJHdiAvujmwQVJfd3ss\&quot;&#x60; → valid prefixed format  | [optional] 
**tags** | **List[str]** | Array of tag identifiers to associate with the contact. Identifiers should use &#x60;tag_&#x60; prefix.  **Processing:** - Invalid tag IDs will be ignored - Duplicates will be removed  **Examples:** - &#x60;\&quot;tag_UhsDkjL772Qbj5lWtT62VK\&quot;&#x60; → valid prefixed format  | [optional] 
**last_tracked_ip** | **str** | Last tracked IP address of the contact for analytics purposes.  **Usage:** - Used for geographic analytics - Helps with spam detection - Optional field  | [optional] 

## Example

```python
from sendx_python_sdk.models.rest_e_contact import RestEContact

# TODO update the JSON string below
json = "{}"
# create an instance of RestEContact from a JSON string
rest_e_contact_instance = RestEContact.from_json(json)
# print the JSON string representation of the object
print(RestEContact.to_json())

# convert the object into a dict
rest_e_contact_dict = rest_e_contact_instance.to_dict()
# create an instance of RestEContact from a dict
rest_e_contact_from_dict = RestEContact.from_dict(rest_e_contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


