# ListModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Encrypted ID of the list | [optional] 
**name** | **str** | Name of the list | [optional] 
**type** | **int** | Type of the list representing opt-in methods (1: Single Opt-In, 2: Double Opt-In) | [optional] 
**send_thank_you_mail** | **bool** | Indicates if a thank-you email should be sent | [optional] 
**thank_you_from_name** | **str** | Name displayed as the sender in the thank-you email | [optional] 
**thank_you_from_email** | **str** | Email address from which the thank-you email is sent | [optional] 
**thank_you_mail_subject** | **str** | Subject line of the thank-you email | [optional] 
**thank_you_mail_message** | **str** | Plain text message body of the thank-you email | [optional] 
**thank_you_sender** | **str** | Details of the sender of the thank-you email | [optional] 
**confirm_from_name** | **str** | Name displayed as the sender in the confirmation email | [optional] 
**confirm_from_email** | **str** | Email address from which the confirmation email is sent | [optional] 
**confirm_mail_subject** | **str** | Subject line of the confirmation email | [optional] 
**confirm_mail_message** | **str** | Plain text message body of the confirmation email | [optional] 
**confirm_success_page** | **str** | URL of the success page after confirmation | [optional] 
**created** | **datetime** | Date and time when the list was created | [optional] 
**updated** | **datetime** | Date and time when the list was last updated | [optional] 
**confirm_sender** | **str** | Details of the sender of the confirmation email | [optional] 

## Example

```python
from sendx_python_sdk.models.list_model import ListModel

# TODO update the JSON string below
json = "{}"
# create an instance of ListModel from a JSON string
list_model_instance = ListModel.from_json(json)
# print the JSON string representation of the object
print(ListModel.to_json())

# convert the object into a dict
list_model_dict = list_model_instance.to_dict()
# create an instance of ListModel from a dict
list_model_from_dict = ListModel.from_dict(list_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


