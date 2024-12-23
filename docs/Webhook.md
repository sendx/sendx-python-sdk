# Webhook


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Webhook ID | [optional] 
**enabled** | **bool** | Indicates whether the webhook is enabled. | [optional] 
**url** | **str** | The URL where webhook events will be sent. | [optional] 
**unsubscribed** | **bool** | Indicates if the webhook unsubscribes users. | [optional] 
**dropped** | **bool** | Indicates if the webhook processes dropped events. | [optional] 
**bounced** | **bool** | Indicates if the webhook processes bounced events. | [optional] 
**marked_spam** | **bool** | Indicates if the webhook processes marked-as-spam events. | [optional] 
**clicked** | **bool** | Indicates if the webhook processes click events. | [optional] 
**opened** | **bool** | Indicates if the webhook processes open events. | [optional] 
**created** | **int** | Timestamp of when the webhook was created. | [optional] 

## Example

```python
from sendx_python_sdk.models.webhook import Webhook

# TODO update the JSON string below
json = "{}"
# create an instance of Webhook from a JSON string
webhook_instance = Webhook.from_json(json)
# print the JSON string representation of the object
print(Webhook.to_json())

# convert the object into a dict
webhook_dict = webhook_instance.to_dict()
# create an instance of Webhook from a dict
webhook_from_dict = Webhook.from_dict(webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


