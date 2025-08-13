# RestRWebhook


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**url** | **str** | Webhook endpoint URL | [optional] 
**enabled** | **bool** | Whether webhook is enabled | [optional] [default to True]
**unsubscribed** | **bool** | Trigger webhook when a contact unsubscribes | [optional] [default to False]
**dropped** | **bool** | Trigger webhook when an email is dropped | [optional] [default to False]
**bounced** | **bool** | Trigger webhook when an email bounces | [optional] [default to False]
**marked_spam** | **bool** | Trigger webhook when an email is marked as spam | [optional] [default to False]
**clicked** | **bool** | Trigger webhook when a link in the email is clicked | [optional] [default to False]
**opened** | **bool** | Trigger webhook when an email is opened | [optional] [default to False]
**contact_created** | **bool** | Trigger webhook when a new contact is created | [optional] [default to False]

## Example

```python
from sendx_python_sdk.models.rest_r_webhook import RestRWebhook

# TODO update the JSON string below
json = "{}"
# create an instance of RestRWebhook from a JSON string
rest_r_webhook_instance = RestRWebhook.from_json(json)
# print the JSON string representation of the object
print(RestRWebhook.to_json())

# convert the object into a dict
rest_r_webhook_dict = rest_r_webhook_instance.to_dict()
# create an instance of RestRWebhook from a dict
rest_r_webhook_from_dict = RestRWebhook.from_dict(rest_r_webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


