# RestECampaign


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Campaign name for internal organization | 
**subject** | **str** | Email subject line with personalization support.  **Features:** - Supports template variables ({{contact.firstName}}) - Emoji support for better engagement - A/B testing variations supported  | 
**sender** | **str** | Sender identifier.  **Note:** Sender must be verified before use  | 
**html_code** | **str** | HTML content of the email campaign | 
**preview_text** | **str** | Preview text shown in email clients | [optional] 
**plain_text** | **str** | Plain text version for better deliverability | [optional] 
**schedule_type** | **int** | Campaign scheduling type.  **Values:** - &#x60;0&#x60; - Schedule for specific date/time - &#x60;1&#x60; - Send immediately  | [optional] 
**schedule_condition** | **str** | datetime for scheduled campaigns (required if scheduleType&#x3D;0) | [optional] 
**time_condition** | **str** | Time condition for scheduled campaigns in HH:MM PM/AM format | [optional] 
**timezone** | **str** | Timezone for scheduled campaigns (IANA format) | [optional] 
**preferred_timezone** | **str** | Preferred timezone for smart send optimization (required for smartSend and sendInContactsTimezone) | [optional] 
**preferred_time_condition** | **str** | Preferred time optimization setting (required for smartSend and sendInContactsTimezone) | [optional] 
**send_in_contacts_timezone** | **bool** | Send at specified time in each contact&#39;s timezone | [optional] 
**smart_send** | **bool** | Enable AI-powered send time optimization | [optional] 
**included_segments** | **List[str]** | Segment IDs to include | [optional] 
**included_lists** | **List[str]** | List IDs to include | [optional] 
**included_tags** | **List[str]** | Tag IDs to include | [optional] 
**excluded_segments** | **List[str]** | Segment IDs to exclude | [optional] 
**excluded_lists** | **List[str]** | List IDs to exclude | [optional] 
**excluded_tags** | **List[str]** | Tag IDs to exclude (prefix automatically stripped) | [optional] 

## Example

```python
from sendx_python_sdk.models.rest_e_campaign import RestECampaign

# TODO update the JSON string below
json = "{}"
# create an instance of RestECampaign from a JSON string
rest_e_campaign_instance = RestECampaign.from_json(json)
# print the JSON string representation of the object
print(RestECampaign.to_json())

# convert the object into a dict
rest_e_campaign_dict = rest_e_campaign_instance.to_dict()
# create an instance of RestECampaign from a dict
rest_e_campaign_from_dict = RestECampaign.from_dict(rest_e_campaign_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


