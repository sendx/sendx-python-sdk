# RestEWebhook


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | Webhook endpoint URL | 
**enabled** | **bool** | Whether webhook is enabled | [default to True]
**unsubscribed** | **bool** | Trigger webhook when a contact unsubscribes | [optional] [default to False]
**dropped** | **bool** | Trigger webhook when an email is dropped | [optional] [default to False]
**bounced** | **bool** | Trigger webhook when an email bounces | [optional] [default to False]
**marked_spam** | **bool** | Trigger webhook when an email is marked as spam | [optional] [default to False]
**clicked** | **bool** | Trigger webhook when a link in the email is clicked | [optional] [default to False]
**opened** | **bool** | Trigger webhook when an email is opened | [optional] [default to False]
**contact_created** | **bool** | Trigger webhook when a new contact is created | [optional] [default to False]

## Example

```python
from sendx_python_sdk.models.rest_e_webhook import RestEWebhook

# TODO update the JSON string below
json = "{}"
# create an instance of RestEWebhook from a JSON string
rest_e_webhook_instance = RestEWebhook.from_json(json)
# print the JSON string representation of the object
print(RestEWebhook.to_json())

# convert the object into a dict
rest_e_webhook_dict = rest_e_webhook_instance.to_dict()
# create an instance of RestEWebhook from a dict
rest_e_webhook_from_dict = RestEWebhook.from_dict(rest_e_webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


