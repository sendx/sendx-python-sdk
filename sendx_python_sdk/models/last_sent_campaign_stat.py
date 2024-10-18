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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from sendx_python_sdk.models.campaign_dashboard_data import CampaignDashboardData
from typing import Optional, Set
from typing_extensions import Self

class LastSentCampaignStat(BaseModel):
    """
    LastSentCampaignStat
    """ # noqa: E501
    campaign: Optional[CampaignDashboardData] = None
    sent: Optional[StrictInt] = Field(default=None, description="Number of emails sent.")
    delivered: Optional[StrictInt] = Field(default=None, description="Number of emails delivered.")
    subscribed: Optional[StrictInt] = Field(default=None, description="Number of new subscriptions.")
    unsubscribed: Optional[StrictInt] = Field(default=None, description="Number of unsubscribes.")
    open: Optional[StrictInt] = Field(default=None, description="Number of emails opened.")
    link_clicked: Optional[StrictInt] = Field(default=None, description="Number of link clicks.", alias="linkClicked")
    replied: Optional[StrictInt] = Field(default=None, description="Number of replies received.")
    __properties: ClassVar[List[str]] = ["campaign", "sent", "delivered", "subscribed", "unsubscribed", "open", "linkClicked", "replied"]

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
        """Create an instance of LastSentCampaignStat from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of campaign
        if self.campaign:
            _dict['campaign'] = self.campaign.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of LastSentCampaignStat from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "campaign": CampaignDashboardData.from_dict(obj["campaign"]) if obj.get("campaign") is not None else None,
            "sent": obj.get("sent"),
            "delivered": obj.get("delivered"),
            "subscribed": obj.get("subscribed"),
            "unsubscribed": obj.get("unsubscribed"),
            "open": obj.get("open"),
            "linkClicked": obj.get("linkClicked"),
            "replied": obj.get("replied")
        })
        return _obj


