# RestRCampaign


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Encrypted ID of the campaign | [optional] 
**name** | **str** | Internal campaign name | 
**subject** | **str** | Email subject line | 
**preheader** | **str** | Email preview text | [optional] 
**sender** | **str** | Sender id | 
**html_content** | **str** | HTML email content | [optional] 
**text_content** | **str** | Plain text email content | [optional] 
**schedule_type** | **int** | Campaign scheduling type.  **Values:** - &#x60;0&#x60; - Schedule later - &#x60;1&#x60; - Send Now  | [default to 0]
**schedule_condition** | **str** | datetime for scheduled campaigns (required if scheduleType&#x3D;1) | 
**time_condition** | **str** | Time-related condition for the campaign | [optional] 
**timezone** | **str** | Campaign timezone | [optional] 
**smart_send** | **bool** | Timezone for the scheduled send | [optional] 
**send_in_contacts_timezone** | **bool** | Send at specified time in each contact&#39;s timezone | [optional] 
**preferred_time_condition** | **str** | Preferred time condition, in case of smartSend and sendInContactTimeZone | [optional] 
**preferred_timezone** | **str** | Preferred timezone for smart send optimization | [optional] 
**strategy** | **str** | Campaign delivery strategy | [optional] 
**included_segments** | **List[str]** | Included segment IDs | [optional] 
**included_lists** | **List[str]** | Included list IDs with prefix | 
**included_tags** | **List[str]** | Included tag IDs with prefix | [optional] 
**excluded_segments** | **List[str]** | Excluded segment IDs | [optional] 
**excluded_lists** | **List[str]** | Excluded list IDs with prefix | 
**excluded_tags** | **List[str]** | Excluded tag IDs with prefix | [optional] 
**created** | **datetime** |  | [optional] 
**updated** | **datetime** |  | [optional] 

## Example

```python
from sendx_python_sdk.models.rest_r_campaign import RestRCampaign

# TODO update the JSON string below
json = "{}"
# create an instance of RestRCampaign from a JSON string
rest_r_campaign_instance = RestRCampaign.from_json(json)
# print the JSON string representation of the object
print(RestRCampaign.to_json())

# convert the object into a dict
rest_r_campaign_dict = rest_r_campaign_instance.to_dict()
# create an instance of RestRCampaign from a dict
rest_r_campaign_from_dict = RestRCampaign.from_dict(rest_r_campaign_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


