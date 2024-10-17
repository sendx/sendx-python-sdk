# LastSentCampaignStat


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**campaign** | [**CampaignDashboardData**](CampaignDashboardData.md) |  | [optional] 
**sent** | **int** | Number of emails sent. | [optional] 
**delivered** | **int** | Number of emails delivered. | [optional] 
**subscribed** | **int** | Number of new subscriptions. | [optional] 
**unsubscribed** | **int** | Number of unsubscribes. | [optional] 
**open** | **int** | Number of emails opened. | [optional] 
**link_clicked** | **int** | Number of link clicks. | [optional] 
**replied** | **int** | Number of replies received. | [optional] 

## Example

```python
from sendx_python_sdk.models.last_sent_campaign_stat import LastSentCampaignStat

# TODO update the JSON string below
json = "{}"
# create an instance of LastSentCampaignStat from a JSON string
last_sent_campaign_stat_instance = LastSentCampaignStat.from_json(json)
# print the JSON string representation of the object
print(LastSentCampaignStat.to_json())

# convert the object into a dict
last_sent_campaign_stat_dict = last_sent_campaign_stat_instance.to_dict()
# create an instance of LastSentCampaignStat from a dict
last_sent_campaign_stat_from_dict = LastSentCampaignStat.from_dict(last_sent_campaign_stat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


