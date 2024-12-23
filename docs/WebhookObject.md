# WebhookObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** | The type of the event. | [optional] 
**time** | **int** | The timestamp of the event in milliseconds since the epoch. | [optional] 
**data** | **str** | Arbitrary data associated with the event. | [optional] 
**provider_message_id** | **str** | Optional provider message ID. | [optional] 
**campaign_id** | **str** | Optional campaign ID. | [optional] 
**drip_step_id** | **str** | Optional drip step ID. | [optional] 
**rss_exec_id** | **str** | Optional RSS execution ID. | [optional] 
**tag_id** | **str** | Optional tag ID. | [optional] 
**link** | **str** | Optional link associated with the event. | [optional] 
**list_id** | **str** | Optional list ID. | [optional] 
**contact_id** | **str** | Optional contact ID. | [optional] 
**custom_field_id** | **str** | Optional custom field ID. | [optional] 
**template_id** | **str** | Optional template ID. | [optional] 
**popup_id** | **str** | Optional popup ID. | [optional] 
**landing_page_id** | **str** | Optional landing page ID. | [optional] 
**form_id** | **str** | Optional form ID. | [optional] 
**segment_id** | **str** | Optional segment ID. | [optional] 
**automation_id** | **str** | Optional automation ID. | [optional] 
**drip_id** | **str** | Optional drip ID. | [optional] 
**rss_id** | **str** | Optional RSS ID. | [optional] 
**ab_test_id** | **str** | Optional A/B test ID. | [optional] 
**workflow_id** | **str** | Optional workflow ID. | [optional] 
**workflow_node_id** | **str** | Optional workflow node ID. | [optional] 
**workflow_email_id** | **str** | Optional workflow email ID. | [optional] 

## Example

```python
from sendx_python_sdk.models.webhook_object import WebhookObject

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookObject from a JSON string
webhook_object_instance = WebhookObject.from_json(json)
# print the JSON string representation of the object
print(WebhookObject.to_json())

# convert the object into a dict
webhook_object_dict = webhook_object_instance.to_dict()
# create an instance of WebhookObject from a dict
webhook_object_from_dict = WebhookObject.from_dict(webhook_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


