# Contact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier for the contact. | [optional] 
**first_name** | **str** | The first name of the contact. | [optional] 
**last_name** | **str** | The last name of the contact. | [optional] 
**email** | **str** | The email address of the contact. | [optional] 
**company** | **str** | The company of the contact. | [optional] 
**custom_fields** | **Dict[str, str]** | Custom fields and their values | [optional] 
**unsubscribed** | **bool** | Indicates if the contact has unsubscribed from emails. | [optional] 
**bounced** | **bool** | Indicates if the contact&#39;s email has bounced. | [optional] 
**spam** | **bool** | Indicates if the contact marked the email as spam. | [optional] 
**created** | **datetime** | The date and time when the contact was created. | [optional] 
**updated** | **datetime** | The date and time when the contact was last updated. | [optional] 
**blocked** | **bool** | Indicates if the contact is blocked from receiving emails. | [optional] 
**dropped** | **bool** | Indicates if emails to this contact were dropped. | [optional] 
**ltv** | **int** | Lifetime value (LTV) of the contact in currency units. | [optional] 
**contact_source** | **int** | The source from which the contact was added. Possible values:  | [optional] 
**last_tracked_ip** | **str** | The last known IP address tracked for the contact. | [optional] 

## Example

```python
from sendx_python_sdk.models.contact import Contact

# TODO update the JSON string below
json = "{}"
# create an instance of Contact from a JSON string
contact_instance = Contact.from_json(json)
# print the JSON string representation of the object
print(Contact.to_json())

# convert the object into a dict
contact_dict = contact_instance.to_dict()
# create an instance of Contact from a dict
contact_from_dict = Contact.from_dict(contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


