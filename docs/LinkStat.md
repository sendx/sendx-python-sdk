# LinkStat

Link statistics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The link clicked | [optional] 
**count** | **int** | Total number of times the link was clicked | [optional] 

## Example

```python
from sendx_python_sdk.models.link_stat import LinkStat

# TODO update the JSON string below
json = "{}"
# create an instance of LinkStat from a JSON string
link_stat_instance = LinkStat.from_json(json)
# print the JSON string representation of the object
print(LinkStat.to_json())

# convert the object into a dict
link_stat_dict = link_stat_instance.to_dict()
# create an instance of LinkStat from a dict
link_stat_from_dict = LinkStat.from_dict(link_stat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


