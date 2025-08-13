# PostbackResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from sendx_python_sdk.models.postback_response import PostbackResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostbackResponse from a JSON string
postback_response_instance = PostbackResponse.from_json(json)
# print the JSON string representation of the object
print(PostbackResponse.to_json())

# convert the object into a dict
postback_response_dict = postback_response_instance.to_dict()
# create an instance of PostbackResponse from a dict
postback_response_from_dict = PostbackResponse.from_dict(postback_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


