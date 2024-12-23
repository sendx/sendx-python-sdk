# coding: utf-8

"""
    SendX REST API

    # Introduction SendX is an email marketing product. It helps you convert website visitors to customers, send them promotional emails, engage with them using drip sequences and craft custom journeys using powerful but simple automations. The SendX API is organized around REST. Our API has predictable resource-oriented URLs, accepts form-encoded request bodies, returns JSON-encoded responses, and uses standard HTTP response codes, authentication, and verbs. The SendX Rest API doesn’t support bulk updates. You can work on only one object per request. <br> 

    The version of the OpenAPI document: 1.0.0
    Contact: support@sendx.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class CampaignRequest(BaseModel):
    """
    CampaignRequest
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, description="The name of the campaign.")
    html_code: Optional[StrictStr] = Field(default=None, description="The HTML code of the campaign.", alias="htmlCode")
    subject: Optional[StrictStr] = Field(default=None, description="The subject of the campaign.")
    sender: Optional[StrictStr] = Field(default=None, description="Sender unique identifier.")
    preview_text: Optional[StrictStr] = Field(default=None, description="The preview text shown in email clients.", alias="previewText")
    schedule_type: Optional[StrictInt] = Field(default=None, description="The type of scheduling for the campaign <br> 0: Send Now <br> 1: Send Later ", alias="scheduleType")
    schedule_condition: Optional[StrictStr] = Field(default=None, description="The condition for scheduling the campaign.", alias="scheduleCondition")
    time_condition: Optional[StrictStr] = Field(default=None, description="The specific time to send the campaign.", alias="timeCondition")
    timezone: Optional[StrictStr] = Field(default=None, description="The timezone for the campaign scheduling.")
    preferred_timezone: Optional[StrictStr] = Field(default=None, description="Preferred timezone for scheduling.", alias="preferredTimezone")
    preferred_time_condition: Optional[StrictStr] = Field(default=None, description="Specific time preference for sending the campaign.", alias="preferredTimeCondition")
    send_in_contacts_timezone: Optional[StrictBool] = Field(default=None, description="Whether to send emails in each contact's timezone.", alias="sendInContactsTimezone")
    smart_send: Optional[StrictBool] = Field(default=None, description="Whether to enable smart send features (e.g., optimizing send time).", alias="smartSend")
    included_segments: Optional[List[StrictStr]] = Field(default=None, description="List of segment IDs to include.", alias="includedSegments")
    included_lists: Optional[List[StrictStr]] = Field(default=None, description="List of list IDs to include.", alias="includedLists")
    included_tags: Optional[List[StrictStr]] = Field(default=None, description="List of tag IDs to include.", alias="includedTags")
    excluded_segments: Optional[List[StrictStr]] = Field(default=None, description="List of segment IDs to exclude.", alias="excludedSegments")
    excluded_lists: Optional[List[StrictStr]] = Field(default=None, description="List of list IDs to exclude.", alias="excludedLists")
    excluded_tags: Optional[List[StrictStr]] = Field(default=None, description="List of tag IDs to exclude.", alias="excludedTags")
    __properties: ClassVar[List[str]] = ["name", "htmlCode", "subject", "sender", "previewText", "scheduleType", "scheduleCondition", "timeCondition", "timezone", "preferredTimezone", "preferredTimeCondition", "sendInContactsTimezone", "smartSend", "includedSegments", "includedLists", "includedTags", "excludedSegments", "excludedLists", "excludedTags"]

    @field_validator('schedule_type')
    def schedule_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set([0, 1]):
            raise ValueError("must be one of enum values (0, 1)")
        return value

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
        """Create an instance of CampaignRequest from a JSON string"""
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
        """Create an instance of CampaignRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "htmlCode": obj.get("htmlCode"),
            "subject": obj.get("subject"),
            "sender": obj.get("sender"),
            "previewText": obj.get("previewText"),
            "scheduleType": obj.get("scheduleType"),
            "scheduleCondition": obj.get("scheduleCondition"),
            "timeCondition": obj.get("timeCondition"),
            "timezone": obj.get("timezone"),
            "preferredTimezone": obj.get("preferredTimezone"),
            "preferredTimeCondition": obj.get("preferredTimeCondition"),
            "sendInContactsTimezone": obj.get("sendInContactsTimezone"),
            "smartSend": obj.get("smartSend"),
            "includedSegments": obj.get("includedSegments"),
            "includedLists": obj.get("includedLists"),
            "includedTags": obj.get("includedTags"),
            "excludedSegments": obj.get("excludedSegments"),
            "excludedLists": obj.get("excludedLists"),
            "excludedTags": obj.get("excludedTags")
        })
        return _obj


