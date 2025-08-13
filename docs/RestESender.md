# RestESender


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Sender display name | 
**email** | **str** | Sender email address (must be verified) | 

## Example

```python
from sendx_python_sdk.models.rest_e_sender import RestESender

# TODO update the JSON string below
json = "{}"
# create an instance of RestESender from a JSON string
rest_e_sender_instance = RestESender.from_json(json)
# print the JSON string representation of the object
print(RestESender.to_json())

# convert the object into a dict
rest_e_sender_dict = rest_e_sender_instance.to_dict()
# create an instance of RestESender from a dict
rest_e_sender_from_dict = RestESender.from_dict(rest_e_sender_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


