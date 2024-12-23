# [SendX Python SDK](https://pypi.org/project/SendX/)
## Introduction

SendX is an email marketing product. It helps you convert website visitors to customers, send them promotional emails, engage with them using drip sequences and craft custom journeys using powerful but simple automations.

The SendX API is organized around REST. Our API has predictable resource-oriented URLs, accepts form-encoded request bodies, returns JSON-encoded responses, and uses standard HTTP response codes, authentication, and verbs.
The SendX Rest API doesn’t support bulk updates. You can work on only one object per request. <br>



## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install sendx
```

(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/sendx/sendx-python-sdk.git`)

Then import the package:
```python
import sendx_python_sdk
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import sendx_python_sdk
```


## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import sendx_python_sdk
from sendx_python_sdk.models.contact_request import ContactRequest
from sendx_python_sdk.models.response import Response
from sendx_python_sdk.rest import ApiException
from pprint import pprint


configuration = sendx_python_sdk.Configuration()

# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.environ["API_KEY"]

# Enter a context with an instance of the API client
with sendx_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sendx_python_sdk.ContactApi(api_client)
    contact_request = sendx_python_sdk.ContactRequest() # ContactRequest | 
    contact_request.email = "johndoe@sendx.io"
    contact_request.first_name = "John"
    contact_request.last_name = "Doe"
    contact_request.company = "SendX"
    contact_request.tags = ["12nb32nk43k2", "34njnk42bkj3"]
    contact_request.custom_fields = {"1434nfk324kn4d": "VIP", "34njnk42bkj3": "Gold"}
    contact_request.last_tracked_ip = "34.212.42.122"

    try:
        # Create a contact
        api_response = api_instance.create_contact(contact_request)
        print("The response of ContactApi->create_contact:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CampaignApi->create_campaign: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.sendx.io/api/v1/rest*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CampaignApi* | [**create_campaign**](docs/CampaignApi.md#create_campaign) | **POST** /campaign | Create Campaign
*CampaignApi* | [**delete_campaign**](docs/CampaignApi.md#delete_campaign) | **DELETE** /campaign/{campaignId} | Delete Campaign
*CampaignApi* | [**edit_campaign**](docs/CampaignApi.md#edit_campaign) | **PUT** /campaign/{campaignId} | Edit Campaign
*CampaignApi* | [**get_all_campaigns**](docs/CampaignApi.md#get_all_campaigns) | **GET** /campaign | Get All Campaigns
*CampaignApi* | [**get_campaign_by_id**](docs/CampaignApi.md#get_campaign_by_id) | **GET** /campaign/{campaignId} | Get Campaign By Id
*ContactApi* | [**create_contact**](docs/ContactApi.md#create_contact) | **POST** /contact | Create a contact
*ContactApi* | [**delete_contact**](docs/ContactApi.md#delete_contact) | **DELETE** /contact/{identifier} | Delete Contact
*ContactApi* | [**get_all_contacts**](docs/ContactApi.md#get_all_contacts) | **GET** /contact | Get All Contacts
*ContactApi* | [**get_contact_by_id**](docs/ContactApi.md#get_contact_by_id) | **GET** /contact/{identifier} | Get Contact by Identifier
*ContactApi* | [**unsubscribe_contact**](docs/ContactApi.md#unsubscribe_contact) | **POST** /contact/unsubscribe/{identifier} | Unsubscribe Contact
*ContactApi* | [**update_contact**](docs/ContactApi.md#update_contact) | **PUT** /contact/{identifier} | Update Contact
*CustomFieldApi* | [**customfield_customfield_id_delete**](docs/CustomFieldApi.md#customfield_customfield_id_delete) | **DELETE** /customfield/{customfieldId} | Delete Custom Field
*CustomFieldApi* | [**customfield_customfield_id_get**](docs/CustomFieldApi.md#customfield_customfield_id_get) | **GET** /customfield/{customfieldId} | Get Custom Field
*CustomFieldApi* | [**customfield_customfield_id_put**](docs/CustomFieldApi.md#customfield_customfield_id_put) | **PUT** /customfield/{customfieldId} | Update Custom Field
*CustomFieldApi* | [**customfield_get**](docs/CustomFieldApi.md#customfield_get) | **GET** /customfield | Get All Custom Fields
*CustomFieldApi* | [**customfield_post**](docs/CustomFieldApi.md#customfield_post) | **POST** /customfield | Create Custom Field
*EventApi* | [**create_revenue_event**](docs/EventApi.md#create_revenue_event) | **POST** /events/revenue | Record a revenue event for a specific contact
*EventApi* | [**push_custom_event**](docs/EventApi.md#push_custom_event) | **POST** /events/custom | Push a custom event associated with a contact
*GettingStartedApi* | [**identify_contact**](docs/GettingStartedApi.md#identify_contact) | **POST** /contact/identify | Identify contact
*GettingStartedApi* | [**tracking_contact**](docs/GettingStartedApi.md#tracking_contact) | **POST** /contact/track | Add Tracking info
*ListApi* | [**create_list**](docs/ListApi.md#create_list) | **POST** /list | Create List
*ListApi* | [**delete_list**](docs/ListApi.md#delete_list) | **DELETE** /list/{listId} | Delete List
*ListApi* | [**get_all_lists**](docs/ListApi.md#get_all_lists) | **GET** /list | Get All Lists
*ListApi* | [**get_list_by_id**](docs/ListApi.md#get_list_by_id) | **GET** /list/{listId} | Get List
*ListApi* | [**update_list**](docs/ListApi.md#update_list) | **PUT** /list/{listId} | Update List
*ReportsApi* | [**get_campaign_report**](docs/ReportsApi.md#get_campaign_report) | **GET** /report/campaign/{campaignId} | Get CampaignReport Data
*SenderApi* | [**create_sender**](docs/SenderApi.md#create_sender) | **POST** /sender | Create Sender
*SenderApi* | [**get_all_senders**](docs/SenderApi.md#get_all_senders) | **GET** /sender | Get All Senders
*TagsApi* | [**create_tag**](docs/TagsApi.md#create_tag) | **POST** /tag | Create a Tag
*TagsApi* | [**delete_tag**](docs/TagsApi.md#delete_tag) | **DELETE** /tag/{tagId} | Delete a Tag
*TagsApi* | [**get_all_tags**](docs/TagsApi.md#get_all_tags) | **GET** /tag | Get All Tags
*TagsApi* | [**get_tag_by_id**](docs/TagsApi.md#get_tag_by_id) | **GET** /tag/{tagId} | Get a Tag by ID
*TagsApi* | [**update_tag**](docs/TagsApi.md#update_tag) | **PUT** /tag/{tagId} | Update a Tag
*WebhookApi* | [**create_team_webhook**](docs/WebhookApi.md#create_team_webhook) | **POST** /webhook | Create TeamWebhook
*WebhookApi* | [**delete_team_webhook**](docs/WebhookApi.md#delete_team_webhook) | **DELETE** /webhook/{webhookId} | Delete Team Webhook
*WebhookApi* | [**get_all_team_webhook**](docs/WebhookApi.md#get_all_team_webhook) | **GET** /webhook | Get All team Webhook
*WebhookApi* | [**get_team_webhook**](docs/WebhookApi.md#get_team_webhook) | **GET** /webhook/{webhookId} | Get TeamWebhook
*WebhookApi* | [**update_team_webhook**](docs/WebhookApi.md#update_team_webhook) | **PUT** /webhook/{webhookId} | Update Team Webhook


## Documentation For Models

 - [Campaign](docs/Campaign.md)
 - [CampaignDashboardData](docs/CampaignDashboardData.md)
 - [CampaignRequest](docs/CampaignRequest.md)
 - [Contact](docs/Contact.md)
 - [ContactRequest](docs/ContactRequest.md)
 - [CreateResponse](docs/CreateResponse.md)
 - [CustomEventRequest](docs/CustomEventRequest.md)
 - [CustomField](docs/CustomField.md)
 - [CustomfieldCustomfieldIdDelete200Response](docs/CustomfieldCustomfieldIdDelete200Response.md)
 - [DashboardStats](docs/DashboardStats.md)
 - [DeleteCampaign200Response](docs/DeleteCampaign200Response.md)
 - [DeleteRequest](docs/DeleteRequest.md)
 - [DeleteResponse](docs/DeleteResponse.md)
 - [ECustomField](docs/ECustomField.md)
 - [EventResponse](docs/EventResponse.md)
 - [IdentifyRequest](docs/IdentifyRequest.md)
 - [IdentifyResponse](docs/IdentifyResponse.md)
 - [LastSentCampaignStat](docs/LastSentCampaignStat.md)
 - [ListModel](docs/ListModel.md)
 - [ListRequest](docs/ListRequest.md)
 - [ReportData](docs/ReportData.md)
 - [Response](docs/Response.md)
 - [RevenueEventRequest](docs/RevenueEventRequest.md)
 - [Sender](docs/Sender.md)
 - [SenderRequest](docs/SenderRequest.md)
 - [SenderResponse](docs/SenderResponse.md)
 - [Tag](docs/Tag.md)
 - [TagRequest](docs/TagRequest.md)
 - [TrackRequest](docs/TrackRequest.md)
 - [TrackResponse](docs/TrackResponse.md)
 - [Webhook](docs/Webhook.md)
 - [WebhookObject](docs/WebhookObject.md)
 - [WebhookRequest](docs/WebhookRequest.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="apiKeyAuth"></a>
### apiKeyAuth

- **Type**: API key
- **API key parameter name**: X-Team-ApiKey
- **Location**: HTTP header


## Author

support@sendx.io


