# XEmailResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to** | **str** | Recipient email address | [optional] 
**submitted_at** | **int** | Unix timestamp of submission | [optional] 
**message_id** | **str** | Unique message identifier | [optional] 
**error_code** | **int** | Error code (0 &#x3D; success) | [optional] 
**message** | **str** | Status message | [optional] 

## Example

```python
from sendx_python_sdk.models.x_email_response import XEmailResponse

# TODO update the JSON string below
json = "{}"
# create an instance of XEmailResponse from a JSON string
x_email_response_instance = XEmailResponse.from_json(json)
# print the JSON string representation of the object
print(XEmailResponse.to_json())

# convert the object into a dict
x_email_response_dict = x_email_response_instance.to_dict()
# create an instance of XEmailResponse from a dict
x_email_response_from_dict = XEmailResponse.from_dict(x_email_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


