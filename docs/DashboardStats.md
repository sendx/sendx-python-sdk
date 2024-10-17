# DashboardStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_email_campaign_stat** | [**LastSentCampaignStat**](LastSentCampaignStat.md) |  | [optional] 
**newsletter_count** | **int** | Number of newsletters sent. | [optional] 
**automation_count** | **int** | Number of automations set up. | [optional] 

## Example

```python
from sendx_python_sdk.models.dashboard_stats import DashboardStats

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardStats from a JSON string
dashboard_stats_instance = DashboardStats.from_json(json)
# print the JSON string representation of the object
print(DashboardStats.to_json())

# convert the object into a dict
dashboard_stats_dict = dashboard_stats_instance.to_dict()
# create an instance of DashboardStats from a dict
dashboard_stats_from_dict = DashboardStats.from_dict(dashboard_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


