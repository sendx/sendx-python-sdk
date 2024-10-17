# ReportData

Contains the report data for a given campaign

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**campaign_id** | **str** | The ID of the campaign | [optional] 
**link_stats** | **Dict[str, int]** | Statistics about the links clicked within the campaign | [optional] 
**clicked_contact_count** | **int** | The total number of contacts that clicked on any link | [optional] 
**opened_contact_count** | **int** | The total number of contacts that opened the campaign email | [optional] 
**replied_contact_count** | **int** | The total number of contacts that replied to the campaign email | [optional] 
**clicked_unique_contact_count** | **int** | The unique number of contacts that clicked on any link | [optional] 
**opened_unique_contact_count** | **int** | The unique number of contacts that opened the campaign email | [optional] 
**replied_unique_contact_count** | **int** | The unique number of contacts that replied to the campaign email | [optional] 
**sent_contact_count** | **int** | The total number of contacts the campaign was sent to | [optional] 
**unsubscribe_contact_count** | **int** | The total number of contacts that unsubscribed | [optional] 
**bounce_contact_count** | **int** | The total number of bounced contacts | [optional] 
**spam_contact_count** | **int** | The total number of contacts that marked the email as spam | [optional] 
**email_revenue** | **str** | The total revenue generated from the campaign email | [optional] 
**revenue_per_recipient** | **str** | The average revenue generated per recipient | [optional] 
**currency** | **str** | The currency in which the revenue is measured | [optional] 

## Example

```python
from sendx_python_sdk.models.report_data import ReportData

# TODO update the JSON string below
json = "{}"
# create an instance of ReportData from a JSON string
report_data_instance = ReportData.from_json(json)
# print the JSON string representation of the object
print(ReportData.to_json())

# convert the object into a dict
report_data_dict = report_data_instance.to_dict()
# create an instance of ReportData from a dict
report_data_from_dict = ReportData.from_dict(report_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


