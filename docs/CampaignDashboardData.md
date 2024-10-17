# CampaignDashboardData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the campaign. | [optional] 
**name** | **str** | Name of the campaign. | [optional] 
**subject** | **str** | Subject of the campaign. | [optional] 
**sent_time** | **datetime** | The time the campaign was sent. | [optional] 
**campaign_screenshot_url** | **str** | URL to a screenshot of the campaign. | [optional] 

## Example

```python
from sendx_python_sdk.models.campaign_dashboard_data import CampaignDashboardData

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignDashboardData from a JSON string
campaign_dashboard_data_instance = CampaignDashboardData.from_json(json)
# print the JSON string representation of the object
print(CampaignDashboardData.to_json())

# convert the object into a dict
campaign_dashboard_data_dict = campaign_dashboard_data_instance.to_dict()
# create an instance of CampaignDashboardData from a dict
campaign_dashboard_data_from_dict = CampaignDashboardData.from_dict(campaign_dashboard_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


