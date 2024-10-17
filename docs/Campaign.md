# Campaign


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Encrypted ID of the campaign | [optional] 
**name** | **str** | Name of the campaign | [optional] 
**track_reply** | **bool** | Indicates if replies to the campaign should be tracked | [optional] 
**status** | **int** | Campaign status: 0 (Draft), 1 (Scheduled), 2 (Sending), 3 (Sent), 4 (Quarantined) | [optional] 
**schedule_type** | **int** | Schedule type: 0 (Schedule later), 1 (Send Now), 2 (Trigger via automation), 3 (Recurring) | [optional] 
**schedule_condition** | **str** | Condition for scheduling the campaign | [optional] 
**time_condition** | **str** | Time-related condition for the campaign | [optional] 
**timezone** | **str** | Timezone for the scheduled send | [optional] 
**preferred_time_condition** | **str** | Preferred time condition for the campaign | [optional] 
**preferred_timezone** | **str** | Preferred timezone for sending the campaign | [optional] 
**strategy** | **str** | Strategy for the campaign | [optional] 
**send_in_contacts_timezone** | **bool** | Indicates if the campaign should be sent in the recipient&#39;s timezone | [optional] 
**smart_send** | **bool** | Indicates if smart sending should be used | [optional] 
**is_archived** | **bool** | Indicates if the campaign is archived | [optional] 
**sender** | **str** | Information about the sender of the campaign | [optional] 
**campaign_screenshot_url** | **str** | URL of the campaign&#39;s screenshot | [optional] 
**included_segments** | **List[str]** | Segments to be included in the campaign | [optional] 
**included_lists** | **List[str]** | Lists to be included in the campaign | [optional] 
**included_tags** | **List[str]** | Tags to be included in the campaign | [optional] 
**excluded_segments** | **List[str]** | Segments to be excluded from the campaign | [optional] 
**excluded_lists** | **List[str]** | Lists to be excluded from the campaign | [optional] 
**excluded_tags** | **List[str]** | Tags to be excluded from the campaign | [optional] 

## Example

```python
from sendx_python_sdk.models.campaign import Campaign

# TODO update the JSON string below
json = "{}"
# create an instance of Campaign from a JSON string
campaign_instance = Campaign.from_json(json)
# print the JSON string representation of the object
print(Campaign.to_json())

# convert the object into a dict
campaign_dict = campaign_instance.to_dict()
# create an instance of Campaign from a dict
campaign_from_dict = Campaign.from_dict(campaign_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


