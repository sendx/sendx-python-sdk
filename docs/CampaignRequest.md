# CampaignRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the campaign. | [optional] 
**html_code** | **str** | The HTML code of the campaign. | [optional] 
**subject** | **str** | The subject of the campaign. | [optional] 
**sender** | **str** | Sender unique identifier. | [optional] 
**preview_text** | **str** | The preview text shown in email clients. | [optional] 
**schedule_type** | **int** | The type of scheduling for the campaign &lt;br&gt; 0: Send Now &lt;br&gt; 1: Send Later  | [optional] 
**schedule_condition** | **str** | The condition for scheduling the campaign. | [optional] 
**time_condition** | **str** | The specific time to send the campaign. | [optional] 
**timezone** | **str** | The timezone for the campaign scheduling. | [optional] 
**preferred_timezone** | **str** | Preferred timezone for scheduling. | [optional] 
**preferred_time_condition** | **str** | Specific time preference for sending the campaign. | [optional] 
**send_in_contacts_timezone** | **bool** | Whether to send emails in each contact&#39;s timezone. | [optional] 
**smart_send** | **bool** | Whether to enable smart send features (e.g., optimizing send time). | [optional] 
**included_segments** | **List[str]** | List of segment IDs to include. | [optional] 
**included_lists** | **List[str]** | List of list IDs to include. | [optional] 
**included_tags** | **List[str]** | List of tag IDs to include. | [optional] 
**excluded_segments** | **List[str]** | List of segment IDs to exclude. | [optional] 
**excluded_lists** | **List[str]** | List of list IDs to exclude. | [optional] 
**excluded_tags** | **List[str]** | List of tag IDs to exclude. | [optional] 

## Example

```python
from sendx_python_sdk.models.campaign_request import CampaignRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignRequest from a JSON string
campaign_request_instance = CampaignRequest.from_json(json)
# print the JSON string representation of the object
print(CampaignRequest.to_json())

# convert the object into a dict
campaign_request_dict = campaign_request_instance.to_dict()
# create an instance of CampaignRequest from a dict
campaign_request_from_dict = CampaignRequest.from_dict(campaign_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


