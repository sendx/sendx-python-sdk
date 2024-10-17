# ContactRequest

Schema for the contact request payload. Used for creating or updating a contact.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | The email address of the contact. Must be a valid email. | [optional] 
**first_name** | **str** | The first name of the contact. | [optional] 
**last_name** | **str** | The last name of the contact. | [optional] 
**company** | **str** | The company where the contact works. | [optional] 
**last_tracked_ip** | **str** | The last known IP address of the contact. | [optional] 
**custom_fields** | **Dict[str, str]** | Custom fields specific to the contact, which may vary by account. | [optional] 
**lists** | **List[str]** | A list of &#x60;lists&#x60; ids the contact is subscribed to. | [optional] 
**tags** | **List[str]** | Tag ids associated with the contact for segmentation or categorization. | [optional] 

## Example

```python
from sendx_python_sdk.models.contact_request import ContactRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ContactRequest from a JSON string
contact_request_instance = ContactRequest.from_json(json)
# print the JSON string representation of the object
print(ContactRequest.to_json())

# convert the object into a dict
contact_request_dict = contact_request_instance.to_dict()
# create an instance of ContactRequest from a dict
contact_request_from_dict = ContactRequest.from_dict(contact_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


