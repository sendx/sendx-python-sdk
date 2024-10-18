# coding: utf-8

"""
    SendX REST API

    # Introduction The SendX API is organized around REST. Our API has predictable resource-oriented URLs, accepts form-encoded request bodies, returns JSON-encoded responses, and uses standard HTTP response codes, authentication, and verbs. The SendX Rest API doesn’t support bulk updates. You can work on only one object per request. <br> 

    The version of the OpenAPI document: 1.0.0
    Contact: support@sendx.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ReportData(BaseModel):
    """
    Contains the report data for a given campaign
    """ # noqa: E501
    campaign_id: Optional[StrictStr] = Field(default=None, description="The ID of the campaign", alias="campaignId")
    link_stats: Optional[Dict[str, StrictInt]] = Field(default=None, description="Statistics about the links clicked within the campaign", alias="linkStats")
    clicked_contact_count: Optional[StrictInt] = Field(default=None, description="The total number of contacts that clicked on any link", alias="clickedContactCount")
    opened_contact_count: Optional[StrictInt] = Field(default=None, description="The total number of contacts that opened the campaign email", alias="openedContactCount")
    replied_contact_count: Optional[StrictInt] = Field(default=None, description="The total number of contacts that replied to the campaign email", alias="repliedContactCount")
    clicked_unique_contact_count: Optional[StrictInt] = Field(default=None, description="The unique number of contacts that clicked on any link", alias="clickedUniqueContactCount")
    opened_unique_contact_count: Optional[StrictInt] = Field(default=None, description="The unique number of contacts that opened the campaign email", alias="openedUniqueContactCount")
    replied_unique_contact_count: Optional[StrictInt] = Field(default=None, description="The unique number of contacts that replied to the campaign email", alias="repliedUniqueContactCount")
    sent_contact_count: Optional[StrictInt] = Field(default=None, description="The total number of contacts the campaign was sent to", alias="sentContactCount")
    unsubscribe_contact_count: Optional[StrictInt] = Field(default=None, description="The total number of contacts that unsubscribed", alias="unsubscribeContactCount")
    bounce_contact_count: Optional[StrictInt] = Field(default=None, description="The total number of bounced contacts", alias="bounceContactCount")
    spam_contact_count: Optional[StrictInt] = Field(default=None, description="The total number of contacts that marked the email as spam", alias="spamContactCount")
    email_revenue: Optional[StrictStr] = Field(default=None, description="The total revenue generated from the campaign email", alias="emailRevenue")
    revenue_per_recipient: Optional[StrictStr] = Field(default=None, description="The average revenue generated per recipient", alias="revenuePerRecipient")
    currency: Optional[StrictStr] = Field(default=None, description="The currency in which the revenue is measured")
    __properties: ClassVar[List[str]] = ["campaignId", "linkStats", "clickedContactCount", "openedContactCount", "repliedContactCount", "clickedUniqueContactCount", "openedUniqueContactCount", "repliedUniqueContactCount", "sentContactCount", "unsubscribeContactCount", "bounceContactCount", "spamContactCount", "emailRevenue", "revenuePerRecipient", "currency"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ReportData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ReportData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "campaignId": obj.get("campaignId"),
            "linkStats": obj.get("linkStats"),
            "clickedContactCount": obj.get("clickedContactCount"),
            "openedContactCount": obj.get("openedContactCount"),
            "repliedContactCount": obj.get("repliedContactCount"),
            "clickedUniqueContactCount": obj.get("clickedUniqueContactCount"),
            "openedUniqueContactCount": obj.get("openedUniqueContactCount"),
            "repliedUniqueContactCount": obj.get("repliedUniqueContactCount"),
            "sentContactCount": obj.get("sentContactCount"),
            "unsubscribeContactCount": obj.get("unsubscribeContactCount"),
            "bounceContactCount": obj.get("bounceContactCount"),
            "spamContactCount": obj.get("spamContactCount"),
            "emailRevenue": obj.get("emailRevenue"),
            "revenuePerRecipient": obj.get("revenuePerRecipient"),
            "currency": obj.get("currency")
        })
        return _obj


