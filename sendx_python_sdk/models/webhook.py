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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class Webhook(BaseModel):
    """
    Webhook
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="Webhook ID")
    enabled: Optional[StrictBool] = Field(default=None, description="Indicates whether the webhook is enabled.")
    url: Optional[StrictStr] = Field(default=None, description="The URL where webhook events will be sent.")
    unsubscribed: Optional[StrictBool] = Field(default=None, description="Indicates if the webhook unsubscribes users.")
    dropped: Optional[StrictBool] = Field(default=None, description="Indicates if the webhook processes dropped events.")
    bounced: Optional[StrictBool] = Field(default=None, description="Indicates if the webhook processes bounced events.")
    marked_spam: Optional[StrictBool] = Field(default=None, description="Indicates if the webhook processes marked-as-spam events.", alias="markedSpam")
    clicked: Optional[StrictBool] = Field(default=None, description="Indicates if the webhook processes click events.")
    opened: Optional[StrictBool] = Field(default=None, description="Indicates if the webhook processes open events.")
    created: Optional[StrictInt] = Field(default=None, description="Timestamp of when the webhook was created.")
    __properties: ClassVar[List[str]] = ["id", "enabled", "url", "unsubscribed", "dropped", "bounced", "markedSpam", "clicked", "opened", "created"]

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
        """Create an instance of Webhook from a JSON string"""
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
        """Create an instance of Webhook from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "enabled": obj.get("enabled"),
            "url": obj.get("url"),
            "unsubscribed": obj.get("unsubscribed"),
            "dropped": obj.get("dropped"),
            "bounced": obj.get("bounced"),
            "markedSpam": obj.get("markedSpam"),
            "clicked": obj.get("clicked"),
            "opened": obj.get("opened"),
            "created": obj.get("created")
        })
        return _obj


