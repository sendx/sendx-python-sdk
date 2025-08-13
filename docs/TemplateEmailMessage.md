# TemplateEmailMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | [**XFrom**](XFrom.md) |  | 
**to** | [**List[XTo]**](XTo.md) |  | 
**reply_to** | [**XReplyTo**](XReplyTo.md) |  | [optional] 
**subject** | **str** | Override template subject | 
**template** | **str** | Template identifier | 

## Example

```python
from sendx_python_sdk.models.template_email_message import TemplateEmailMessage

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateEmailMessage from a JSON string
template_email_message_instance = TemplateEmailMessage.from_json(json)
# print the JSON string representation of the object
print(TemplateEmailMessage.to_json())

# convert the object into a dict
template_email_message_dict = template_email_message_instance.to_dict()
# create an instance of TemplateEmailMessage from a dict
template_email_message_from_dict = TemplateEmailMessage.from_dict(template_email_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


