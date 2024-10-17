# ListRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the list | [optional] 
**type** | **int** | Type of the list representing opt-in methods &lt;br&gt; 0: Single opt-in list &lt;br&gt; 1: Double opt-in list  | [optional] 
**send_thank_you_mail** | **bool** | Indicates if a thank-you email should be sent | [optional] 
**thank_you_from_name** | **str** | Name displayed as the sender in the thank-you email | [optional] 
**thank_you_from_email** | **str** | Email address from which the thank-you email is sent | [optional] 
**thank_you_mail_subject** | **str** | Subject line of the thank-you email | [optional] 
**thank_you_mail_message** | **str** | Plain text message body of the thank-you email | [optional] 
**thank_you_sender** | **str** | Sender ID for the thank-you email | [optional] 
**confirm_from_name** | **str** | Name displayed as the sender in the confirmation email | [optional] 
**confirm_from_email** | **str** | Email address from which the confirmation email is sent | [optional] 
**confirm_mail_subject** | **str** | Subject line of the confirmation email | [optional] 
**confirm_mail_message** | **str** | Plain text message body of the confirmation email | [optional] 
**confirm_success_page** | **str** | URL of the success page after confirmation | [optional] 
**confirm_sender** | **str** | Sender ID for the confirmation email | [optional] 

## Example

```python
from sendx_python_sdk.models.list_request import ListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListRequest from a JSON string
list_request_instance = ListRequest.from_json(json)
# print the JSON string representation of the object
print(ListRequest.to_json())

# convert the object into a dict
list_request_dict = list_request_instance.to_dict()
# create an instance of ListRequest from a dict
list_request_from_dict = ListRequest.from_dict(list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


