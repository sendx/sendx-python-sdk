# RestRSender


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique sender identifier with sender_ prefix | [optional] 
**name** | **str** | Sender display name | [optional] 
**email** | **str** | Sender email address | [optional] 
**is_whitelisted** | **bool** | Sender whitelist status | [optional] 

## Example

```python
from sendx_python_sdk.models.rest_r_sender import RestRSender

# TODO update the JSON string below
json = "{}"
# create an instance of RestRSender from a JSON string
rest_r_sender_instance = RestRSender.from_json(json)
# print the JSON string representation of the object
print(RestRSender.to_json())

# convert the object into a dict
rest_r_sender_dict = rest_r_sender_instance.to_dict()
# create an instance of RestRSender from a dict
rest_r_sender_from_dict = RestRSender.from_dict(rest_r_sender_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


