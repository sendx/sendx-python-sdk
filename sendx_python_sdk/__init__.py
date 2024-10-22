# coding: utf-8

# flake8: noqa

"""
    SendX REST API

    # Introduction SendX is an email marketing product. It helps you convert website visitors to customers, send them promotional emails, engage with them using drip sequences and craft custom journeys using powerful but simple automations. The SendX API is organized around REST. Our API has predictable resource-oriented URLs, accepts form-encoded request bodies, returns JSON-encoded responses, and uses standard HTTP response codes, authentication, and verbs. The SendX Rest API doesn’t support bulk updates. You can work on only one object per request. <br> 

    The version of the OpenAPI document: 1.0.1
    Contact: support@sendx.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.0.2"

# import apis into sdk package
from sendx_python_sdk.api.campaign_api import CampaignApi
from sendx_python_sdk.api.contact_api import ContactApi
from sendx_python_sdk.api.list_api import ListApi
from sendx_python_sdk.api.reports_api import ReportsApi
from sendx_python_sdk.api.sender_api import SenderApi
from sendx_python_sdk.api.tags_api import TagsApi

# import ApiClient
from sendx_python_sdk.api_response import ApiResponse
from sendx_python_sdk.api_client import ApiClient
from sendx_python_sdk.configuration import Configuration
from sendx_python_sdk.exceptions import OpenApiException
from sendx_python_sdk.exceptions import ApiTypeError
from sendx_python_sdk.exceptions import ApiValueError
from sendx_python_sdk.exceptions import ApiKeyError
from sendx_python_sdk.exceptions import ApiAttributeError
from sendx_python_sdk.exceptions import ApiException

# import models into sdk package
from sendx_python_sdk.models.campaign import Campaign
from sendx_python_sdk.models.campaign_dashboard_data import CampaignDashboardData
from sendx_python_sdk.models.campaign_request import CampaignRequest
from sendx_python_sdk.models.contact import Contact
from sendx_python_sdk.models.contact_request import ContactRequest
from sendx_python_sdk.models.create_response import CreateResponse
from sendx_python_sdk.models.dashboard_stats import DashboardStats
from sendx_python_sdk.models.delete_campaign200_response import DeleteCampaign200Response
from sendx_python_sdk.models.delete_request import DeleteRequest
from sendx_python_sdk.models.delete_response import DeleteResponse
from sendx_python_sdk.models.last_sent_campaign_stat import LastSentCampaignStat
from sendx_python_sdk.models.list_model import ListModel
from sendx_python_sdk.models.list_request import ListRequest
from sendx_python_sdk.models.report_data import ReportData
from sendx_python_sdk.models.response import Response
from sendx_python_sdk.models.sender import Sender
from sendx_python_sdk.models.sender_request import SenderRequest
from sendx_python_sdk.models.sender_response import SenderResponse
from sendx_python_sdk.models.tag import Tag
from sendx_python_sdk.models.tag_request import TagRequest
