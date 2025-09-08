# SendX Python SDK

## 🚀 Introduction

The SendX API is organized around REST principles. Our API has predictable resource-oriented URLs, accepts JSON-encoded request bodies, returns JSON-encoded responses, and uses standard HTTP response codes, authentication, and verbs.

**Key Features:**
- 🔒 **Security**: Team-based authentication with optional member-level access
- 🎯 **Resource-Oriented**: RESTful design with clear resource boundaries
- 📊 **Rich Data Models**: Three-layer model system (Input/Output/Internal)
- 🔗 **Relationships**: Automatic prefix handling for resource relationships
- 📈 **Scalable**: Built for high-volume email marketing operations

## 🏗️ Architecture Overview

SendX uses a three-layer model architecture:

1. **Input Models** (`RestE*`): For API requests
2. **Output Models** (`RestR*`): For API responses with prefixed IDs
3. **Internal Models**: Core business logic (not exposed in API)

## 🔐 Security & Authentication

SendX uses API key authentication:

### Team API Key
```http
X-Team-ApiKey: YOUR_TEAM_API_KEY
```
- **Required for all requests**
- Team-level access to resources
- Available in SendX Settings → Team API Key

## 🆔 Encrypted ID System

SendX uses encrypted IDs for security and better developer experience:

- **Internal IDs**: Sequential integers (not exposed)
- **Encrypted IDs**: 22-character alphanumeric strings
- **Prefixed IDs**: Resource-type prefixes in API responses (`contact_<22-char-id>`)

### ID Format

**All resource IDs follow this pattern:**
```
<resource_prefix>_<22_character_alphanumeric_string>
```

**Example:**
```json
{
  "id": "contact_BnKjkbBBS500CoBCP0oChQ",
  "lists": ["list_OcuxJHdiAvujmwQVJfd3ss", "list_0tOFLp5RgV7s3LNiHrjGYs"],
  "tags": ["tag_UhsDkjL772Qbj5lWtT62VK", "tag_fL7t9lsnZ9swvx2HrtQ9wM"]
}
```

## 📚 Resource Prefixes

| Resource | Prefix | Example |
|----------|--------|---------|
| Contact | `contact_` | `contact_BnKjkbBBS500CoBCP0oChQ` |
| Campaign | `campaign_` | `campaign_LUE9BTxmksSmqHWbh96zsn` |
| List | `list_` | `list_OcuxJHdiAvujmwQVJfd3ss` |
| Tag | `tag_` | `tag_UhsDkjL772Qbj5lWtT62VK` |
| Sender | `sender_` | `sender_4vK3WFhMgvOwUNyaL4QxCD` |
| Template | `template_` | `template_f3lJvTEhSjKGVb5Lwc5SWS` |
| Custom Field | `field_` | `field_MnuqBAG2NPLm7PZMWbjQxt` |
| Webhook | `webhook_` | `webhook_9l154iiXlZoPo7vngmamee` |
| Post | `post_` | `post_XyZ123aBc456DeF789GhI` |
| Post Category | `post_category_` | `post_category_YzS1wOU20yw87UUHKxMzwn` |
| Post Tag | `post_tag_` | `post_tag_123XyZ456AbC` |
| Member | `member_` | `member_JkL012MnO345PqR678` |

## 🎯 Best Practices

### Error Handling
- **Always check status codes**: 2xx = success, 4xx = client error, 5xx = server error
- **Read error messages**: Descriptive messages help debug issues
- **Handle rate limits**: Respect API rate limits for optimal performance

### Data Validation
- **Email format**: Must be valid email addresses
- **Required fields**: Check documentation for mandatory fields
- **Field lengths**: Respect maximum length constraints

### Performance
- **Pagination**: Use offset/limit for large datasets
- **Batch operations**: Process multiple items when supported
- **Caching**: Cache responses when appropriate

## 🛠️ SDKs & Integration

Official SDKs available for:
- [Golang](https://github.com/sendx/sendx-go-sdk)
- [Python](https://github.com/sendx/sendx-python-sdk)
- [Ruby](https://github.com/sendx/sendx-ruby-sdk)
- [Java](https://github.com/sendx/sendx-java-sdk)
- [PHP](https://github.com/sendx/sendx-php-sdk)
- [JavaScript](https://github.com/sendx/sendx-javascript-sdk)

## 📞 Support

Need help? Contact us:
- 💬 **Website Chat**: Available on sendx.io
- 📧 **Email**: hello@sendx.io
- 📚 **Documentation**: Full guides at help.sendx.io

---

**API Endpoint:** `https://api.sendx.io/api/v1/rest`

## Requirements.

Python 3.9+

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

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import sendx_python_sdk
from sendx_python_sdk.models.contact_request import ContactRequest
from sendx_python_sdk.models.response import Response
from sendx_python_sdk.rest import ApiException
from pprint import pprint


configuration = sendx_python_sdk.Configuration()

# Configure API key authorization: TeamApiKey
configuration.api_key['TeamApiKey'] = os.environ["API_KEY"]

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
*CampaignApi* | [**create_campaign**](docs/CampaignApi.md#create_campaign) | **POST** /campaign | Create campaign
*CampaignApi* | [**delete_campaign**](docs/CampaignApi.md#delete_campaign) | **DELETE** /campaign/{identifier} | Delete campaign
*CampaignApi* | [**get_all_campaigns**](docs/CampaignApi.md#get_all_campaigns) | **GET** /campaign | Get all campaigns
*CampaignApi* | [**get_campaign**](docs/CampaignApi.md#get_campaign) | **GET** /campaign/{identifier} | Get campaign by ID
*ContactApi* | [**create_contact**](docs/ContactApi.md#create_contact) | **POST** /contact | Create a new contact
*ContactApi* | [**delete_contact**](docs/ContactApi.md#delete_contact) | **DELETE** /contact/{identifier} | Delete contact
*ContactApi* | [**get_all_contacts**](docs/ContactApi.md#get_all_contacts) | **GET** /contact | Get all contacts
*ContactApi* | [**get_contact**](docs/ContactApi.md#get_contact) | **GET** /contact/{identifier} | Get contact by ID
*ContactApi* | [**unsubscribe_contact**](docs/ContactApi.md#unsubscribe_contact) | **POST** /contact/unsubscribe/{identifier} | Unsubscribe contact
*ContactApi* | [**update_contact**](docs/ContactApi.md#update_contact) | **PUT** /contact/{identifier} | Update contact
*CustomFieldApi* | [**create_custom_field**](docs/CustomFieldApi.md#create_custom_field) | **POST** /customfield | Create custom field
*CustomFieldApi* | [**delete_custom_field**](docs/CustomFieldApi.md#delete_custom_field) | **DELETE** /customfield/{identifier} | Delete custom field
*CustomFieldApi* | [**get_all_custom_fields**](docs/CustomFieldApi.md#get_all_custom_fields) | **GET** /customfield | Get all custom fields
*CustomFieldApi* | [**get_custom_field**](docs/CustomFieldApi.md#get_custom_field) | **GET** /customfield/{identifier} | Get custom field by ID
*CustomFieldApi* | [**update_custom_field**](docs/CustomFieldApi.md#update_custom_field) | **PUT** /customfield/{identifier} | Update custom field
*EmailSendingApi* | [**send_email**](docs/EmailSendingApi.md#send_email) | **POST** /send/email | Send transactional email
*EmailSendingApi* | [**send_email_with_template**](docs/EmailSendingApi.md#send_email_with_template) | **POST** /send/template | Send email using template
*EventApi* | [**events_custom_postback_get**](docs/EventApi.md#events_custom_postback_get) | **GET** /events/custom/postback | Custom Event Postback URL
*EventApi* | [**events_revenue_postback_get**](docs/EventApi.md#events_revenue_postback_get) | **GET** /events/revenue/postback | Revenue Event Postback URL
*EventsApi* | [**track_custom_event**](docs/EventsApi.md#track_custom_event) | **POST** /events/custom | Track custom event
*EventsApi* | [**track_revenue_event**](docs/EventsApi.md#track_revenue_event) | **POST** /events/revenue | Track revenue event
*ListApi* | [**create_list**](docs/ListApi.md#create_list) | **POST** /list | Create list
*ListApi* | [**delete_list**](docs/ListApi.md#delete_list) | **DELETE** /list/{identifier} | Delete list
*ListApi* | [**get_all_lists**](docs/ListApi.md#get_all_lists) | **GET** /list | Get all lists
*ListApi* | [**get_list**](docs/ListApi.md#get_list) | **GET** /list/{identifier} | Get list by ID
*ListApi* | [**update_list**](docs/ListApi.md#update_list) | **PUT** /list/{identifier} | Update list
*PostApi* | [**create_post**](docs/PostApi.md#create_post) | **POST** /post | Create blog post
*PostApi* | [**delete_post**](docs/PostApi.md#delete_post) | **DELETE** /post/{identifier} | Delete post
*PostApi* | [**get_all_posts**](docs/PostApi.md#get_all_posts) | **GET** /post | Get all posts
*PostApi* | [**get_post**](docs/PostApi.md#get_post) | **GET** /post/{identifier} | Get post by ID
*PostApi* | [**update_post**](docs/PostApi.md#update_post) | **PUT** /post/{identifier} | Update post
*PostCategoryApi* | [**create_post_category**](docs/PostCategoryApi.md#create_post_category) | **POST** /post/category | Create post category
*PostCategoryApi* | [**delete_post_category**](docs/PostCategoryApi.md#delete_post_category) | **DELETE** /post/category/{identifier} | Delete post category
*PostCategoryApi* | [**get_all_post_categories**](docs/PostCategoryApi.md#get_all_post_categories) | **GET** /post/category | Get all post categories
*PostCategoryApi* | [**get_post_category**](docs/PostCategoryApi.md#get_post_category) | **GET** /post/category/{identifier} | Get post category by ID
*PostCategoryApi* | [**update_post_category**](docs/PostCategoryApi.md#update_post_category) | **PUT** /post/category/{identifier} | Update post category
*PostTagApi* | [**create_post_tag**](docs/PostTagApi.md#create_post_tag) | **POST** /post/tag | Create post tag
*PostTagApi* | [**delete_post_tag**](docs/PostTagApi.md#delete_post_tag) | **DELETE** /post/tag/{identifier} | Delete post tag
*PostTagApi* | [**get_all_post_tags**](docs/PostTagApi.md#get_all_post_tags) | **GET** /post/tag | Get all post tags
*PostTagApi* | [**get_post_tag**](docs/PostTagApi.md#get_post_tag) | **GET** /post/tag/{identifier} | Get post tag by ID
*PostTagApi* | [**update_post_tag**](docs/PostTagApi.md#update_post_tag) | **PUT** /post/tag/{identifier} | Update post tag
*ReportApi* | [**get_campaign_report**](docs/ReportApi.md#get_campaign_report) | **GET** /report/campaign/{identifier} | Get campaign report
*SenderApi* | [**create_sender**](docs/SenderApi.md#create_sender) | **POST** /sender | Create sender
*SenderApi* | [**get_all_senders**](docs/SenderApi.md#get_all_senders) | **GET** /sender | Get all senders
*TagApi* | [**create_tag**](docs/TagApi.md#create_tag) | **POST** /tag | Create tag
*TagApi* | [**delete_tag**](docs/TagApi.md#delete_tag) | **DELETE** /tag/{identifier} | Delete tag
*TagApi* | [**get_all_tags**](docs/TagApi.md#get_all_tags) | **GET** /tag | Get all tags
*TagApi* | [**get_tag**](docs/TagApi.md#get_tag) | **GET** /tag/{identifier} | Get tag by ID
*TagApi* | [**update_tag**](docs/TagApi.md#update_tag) | **PUT** /tag/{identifier} | Update tag
*TeamMemberApi* | [**get_all_team_members**](docs/TeamMemberApi.md#get_all_team_members) | **GET** /team/member | Get all team members
*TeamMemberApi* | [**get_team_member**](docs/TeamMemberApi.md#get_team_member) | **GET** /team/member/{identifier} | Get a team member by ID
*TemplateApi* | [**create_email_template**](docs/TemplateApi.md#create_email_template) | **POST** /template/email | Create email template
*TemplateApi* | [**delete_email_template**](docs/TemplateApi.md#delete_email_template) | **DELETE** /template/email/{identifier} | Delete template
*TemplateApi* | [**get_all_email_templates**](docs/TemplateApi.md#get_all_email_templates) | **GET** /template/email | Get all templates
*TemplateApi* | [**get_email_template**](docs/TemplateApi.md#get_email_template) | **GET** /template/email/{identifier} | Get template by ID
*TemplateApi* | [**update_email_template**](docs/TemplateApi.md#update_email_template) | **PUT** /template/email/{identifier} | Update template
*TrackingApi* | [**identify_contact**](docs/TrackingApi.md#identify_contact) | **POST** /contact/identify | Identify contact
*TrackingApi* | [**track_contact**](docs/TrackingApi.md#track_contact) | **POST** /contact/track | Track contact
*WebhookApi* | [**create_webhook**](docs/WebhookApi.md#create_webhook) | **POST** /webhook | Create webhook
*WebhookApi* | [**delete_webhook**](docs/WebhookApi.md#delete_webhook) | **DELETE** /webhook/{identifier} | Delete webhook
*WebhookApi* | [**get_all_webhooks**](docs/WebhookApi.md#get_all_webhooks) | **GET** /webhook | Get all webhooks
*WebhookApi* | [**get_webhook**](docs/WebhookApi.md#get_webhook) | **GET** /webhook/{identifier} | Get webhook by ID
*WebhookApi* | [**update_webhook**](docs/WebhookApi.md#update_webhook) | **PUT** /webhook/{identifier} | Update webhook


## Documentation For Models

 - [CustomEventRequest](docs/CustomEventRequest.md)
 - [DeleteResponse](docs/DeleteResponse.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [EventResponse](docs/EventResponse.md)
 - [EventsRevenuePostbackGet200Response](docs/EventsRevenuePostbackGet200Response.md)
 - [EventsRevenuePostbackGet400Response](docs/EventsRevenuePostbackGet400Response.md)
 - [EventsRevenuePostbackGet500Response](docs/EventsRevenuePostbackGet500Response.md)
 - [IdentifyRequest](docs/IdentifyRequest.md)
 - [IdentifyResponse](docs/IdentifyResponse.md)
 - [LinkStat](docs/LinkStat.md)
 - [MessageResponse](docs/MessageResponse.md)
 - [PostbackResponse](docs/PostbackResponse.md)
 - [RestECampaign](docs/RestECampaign.md)
 - [RestEContact](docs/RestEContact.md)
 - [RestECustomField](docs/RestECustomField.md)
 - [RestEList](docs/RestEList.md)
 - [RestEPost](docs/RestEPost.md)
 - [RestEPostCategory](docs/RestEPostCategory.md)
 - [RestEPostTag](docs/RestEPostTag.md)
 - [RestESender](docs/RestESender.md)
 - [RestETag](docs/RestETag.md)
 - [RestETemplate](docs/RestETemplate.md)
 - [RestEWebhook](docs/RestEWebhook.md)
 - [RestRCampaign](docs/RestRCampaign.md)
 - [RestRContact](docs/RestRContact.md)
 - [RestRCustomField](docs/RestRCustomField.md)
 - [RestRList](docs/RestRList.md)
 - [RestRMember](docs/RestRMember.md)
 - [RestRPost](docs/RestRPost.md)
 - [RestRPostCategory](docs/RestRPostCategory.md)
 - [RestRPostTag](docs/RestRPostTag.md)
 - [RestRSender](docs/RestRSender.md)
 - [RestRTag](docs/RestRTag.md)
 - [RestRTemplate](docs/RestRTemplate.md)
 - [RestRWebhook](docs/RestRWebhook.md)
 - [RestReportData](docs/RestReportData.md)
 - [RevenueEventRequest](docs/RevenueEventRequest.md)
 - [TemplateEmailMessage](docs/TemplateEmailMessage.md)
 - [TrackRequest](docs/TrackRequest.md)
 - [TrackResponse](docs/TrackResponse.md)
 - [WebhookObject](docs/WebhookObject.md)
 - [XEmailMessage](docs/XEmailMessage.md)
 - [XEmailResponse](docs/XEmailResponse.md)
 - [XFrom](docs/XFrom.md)
 - [XReplyTo](docs/XReplyTo.md)
 - [XTo](docs/XTo.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="TeamApiKey"></a>
### TeamApiKey

- **Type**: API key
- **API key parameter name**: X-Team-ApiKey
- **Location**: HTTP header


## Author

hello@sendx.io


