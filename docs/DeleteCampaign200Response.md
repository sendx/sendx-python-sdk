# DeleteCampaign200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID of the deleted campaign | [optional] 
**message** | **str** | Success message | [optional] 

## Example

```python
from sendx_python_sdk.models.delete_campaign200_response import DeleteCampaign200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteCampaign200Response from a JSON string
delete_campaign200_response_instance = DeleteCampaign200Response.from_json(json)
# print the JSON string representation of the object
print(DeleteCampaign200Response.to_json())

# convert the object into a dict
delete_campaign200_response_dict = delete_campaign200_response_instance.to_dict()
# create an instance of DeleteCampaign200Response from a dict
delete_campaign200_response_from_dict = DeleteCampaign200Response.from_dict(delete_campaign200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


