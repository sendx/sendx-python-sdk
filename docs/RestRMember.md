# RestRMember


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**user_name** | **str** |  | [optional] 
**full_name** | **str** |  | [optional] 
**avatar_url** | **str** |  | [optional] 
**created** | **datetime** |  | [optional] 
**updated** | **datetime** |  | [optional] 

## Example

```python
from sendx_python_sdk.models.rest_r_member import RestRMember

# TODO update the JSON string below
json = "{}"
# create an instance of RestRMember from a JSON string
rest_r_member_instance = RestRMember.from_json(json)
# print the JSON string representation of the object
print(RestRMember.to_json())

# convert the object into a dict
rest_r_member_dict = rest_r_member_instance.to_dict()
# create an instance of RestRMember from a dict
rest_r_member_from_dict = RestRMember.from_dict(rest_r_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


