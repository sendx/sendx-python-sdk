# XEmailMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | [**XFrom**](XFrom.md) |  | 
**to** | [**List[XTo]**](XTo.md) |  | 
**reply_to** | [**XReplyTo**](XReplyTo.md) |  | [optional] 
**subject** | **str** |  | 
**html_body** | **str** |  | 
**text_body** | **str** |  | [optional] 
**headers** | **Dict[str, str]** |  | [optional] 
**template** | **str** | Template identifier | [optional] 

## Example

```python
from sendx_python_sdk.models.x_email_message import XEmailMessage

# TODO update the JSON string below
json = "{}"
# create an instance of XEmailMessage from a JSON string
x_email_message_instance = XEmailMessage.from_json(json)
# print the JSON string representation of the object
print(XEmailMessage.to_json())

# convert the object into a dict
x_email_message_dict = x_email_message_instance.to_dict()
# create an instance of XEmailMessage from a dict
x_email_message_from_dict = XEmailMessage.from_dict(x_email_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


