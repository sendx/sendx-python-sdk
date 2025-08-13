# RestReportData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**campaign_id** | **str** | Unique identifier of the campaign | [optional] 
**link_stats** | [**List[LinkStat]**](LinkStat.md) |  | [optional] 
**clicked_unique_contact_count** | **int** | Total number of unique contacts who clicked on the link | [optional] 
**opened_unique_contact_count** | **int** | Total number of unique contacts who opened the link | [optional] 
**sent_contact_count** | **int** | Total number of contacts who sent the link | [optional] 
**unsubscribe_contact_count** | **int** | Total number of contacts who unsubscribed from the link | [optional] 
**bounce_contact_count** | **int** | Total number of contacts who bounced the link | [optional] 
**spam_contact_count** | **int** | Total number of contacts who marked the link as spam | [optional] 
**clicked_contact_count** | **int** | Total number of contacts who clicked on the link | [optional] 
**opened_contact_count** | **int** | Total number of contacts who opened the link | [optional] 

## Example

```python
from sendx_python_sdk.models.rest_report_data import RestReportData

# TODO update the JSON string below
json = "{}"
# create an instance of RestReportData from a JSON string
rest_report_data_instance = RestReportData.from_json(json)
# print the JSON string representation of the object
print(RestReportData.to_json())

# convert the object into a dict
rest_report_data_dict = rest_report_data_instance.to_dict()
# create an instance of RestReportData from a dict
rest_report_data_from_dict = RestReportData.from_dict(rest_report_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


