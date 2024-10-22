# coding: utf-8

"""
    SendX REST API

    # Introduction SendX is an email marketing product. It helps you convert website visitors to customers, send them promotional emails, engage with them using drip sequences and craft custom journeys using powerful but simple automations. The SendX API is organized around REST. Our API has predictable resource-oriented URLs, accepts form-encoded request bodies, returns JSON-encoded responses, and uses standard HTTP response codes, authentication, and verbs. The SendX Rest API doesn’t support bulk updates. You can work on only one object per request. <br> 

    The version of the OpenAPI document: 1.0.1
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
from sendx_python_sdk.models.last_sent_campaign_stat import LastSentCampaignStat
from typing import Optional, Set
from typing_extensions import Self

class DashboardStats(BaseModel):
    """
    DashboardStats
    """ # noqa: E501
    last_email_campaign_stat: Optional[LastSentCampaignStat] = Field(default=None, alias="lastEmailCampaignStat")
    newsletter_count: Optional[StrictInt] = Field(default=None, description="Number of newsletters sent.", alias="newsletterCount")
    automation_count: Optional[StrictInt] = Field(default=None, description="Number of automations set up.", alias="automationCount")
    __properties: ClassVar[List[str]] = ["lastEmailCampaignStat", "newsletterCount", "automationCount"]

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
        """Create an instance of DashboardStats from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of last_email_campaign_stat
        if self.last_email_campaign_stat:
            _dict['lastEmailCampaignStat'] = self.last_email_campaign_stat.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DashboardStats from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "lastEmailCampaignStat": LastSentCampaignStat.from_dict(obj["lastEmailCampaignStat"]) if obj.get("lastEmailCampaignStat") is not None else None,
            "newsletterCount": obj.get("newsletterCount"),
            "automationCount": obj.get("automationCount")
        })
        return _obj


