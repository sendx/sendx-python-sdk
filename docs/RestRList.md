# RestRList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**type** | **int** | List type.  **Values:** - &#x60;0&#x60; - Regular list (single opt-in) - &#x60;1&#x60; - Double opt-in list (requires email confirmation)  | [optional] 
**created** | **datetime** |  | [optional] 
**updated** | **datetime** |  | [optional] 

## Example

```python
from sendx_python_sdk.models.rest_r_list import RestRList

# TODO update the JSON string below
json = "{}"
# create an instance of RestRList from a JSON string
rest_r_list_instance = RestRList.from_json(json)
# print the JSON string representation of the object
print(RestRList.to_json())

# convert the object into a dict
rest_r_list_dict = rest_r_list_instance.to_dict()
# create an instance of RestRList from a dict
rest_r_list_from_dict = RestRList.from_dict(rest_r_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


