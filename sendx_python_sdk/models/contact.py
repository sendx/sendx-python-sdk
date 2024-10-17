# coding: utf-8

"""
    SendX REST API

    # Introduction The SendX API is organized around REST. Our API has predictable resource-oriented URLs, accepts form-encoded request bodies, returns JSON-encoded responses, and uses standard HTTP response codes, authentication, and verbs. The SendX Rest API doesn’t support bulk updates. You can work on only one object per request. <br> 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class Contact(BaseModel):
    """
    Contact
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="Identifier for the contact.")
    first_name: Optional[StrictStr] = Field(default=None, description="The first name of the contact.", alias="firstName")
    last_name: Optional[StrictStr] = Field(default=None, description="The last name of the contact.", alias="lastName")
    email: Optional[StrictStr] = Field(default=None, description="The email address of the contact.")
    company: Optional[StrictStr] = Field(default=None, description="The company of the contact.")
    custom_fields: Optional[Dict[str, StrictStr]] = Field(default=None, description="Custom fields and their values", alias="customFields")
    unsubscribed: Optional[StrictBool] = Field(default=None, description="Indicates if the contact has unsubscribed from emails.")
    bounced: Optional[StrictBool] = Field(default=None, description="Indicates if the contact's email has bounced.")
    spam: Optional[StrictBool] = Field(default=None, description="Indicates if the contact marked the email as spam.")
    created: Optional[datetime] = Field(default=None, description="The date and time when the contact was created.")
    updated: Optional[datetime] = Field(default=None, description="The date and time when the contact was last updated.")
    blocked: Optional[StrictBool] = Field(default=None, description="Indicates if the contact is blocked from receiving emails.")
    dropped: Optional[StrictBool] = Field(default=None, description="Indicates if emails to this contact were dropped.")
    ltv: Optional[StrictInt] = Field(default=None, description="Lifetime value (LTV) of the contact in currency units.", alias="LTV")
    contact_source: Optional[StrictInt] = Field(default=None, description="The source from which the contact was added. Possible values: ", alias="contactSource")
    last_tracked_ip: Optional[StrictStr] = Field(default=None, description="The last known IP address tracked for the contact.", alias="lastTrackedIp")
    __properties: ClassVar[List[str]] = ["id", "firstName", "lastName", "email", "company", "customFields", "unsubscribed", "bounced", "spam", "created", "updated", "blocked", "dropped", "LTV", "contactSource", "lastTrackedIp"]

    @field_validator('contact_source')
    def contact_source_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]):
            raise ValueError("must be one of enum values (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19)")
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
        """Create an instance of Contact from a JSON string"""
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
        """Create an instance of Contact from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "firstName": obj.get("firstName"),
            "lastName": obj.get("lastName"),
            "email": obj.get("email"),
            "company": obj.get("company"),
            "customFields": obj.get("customFields"),
            "unsubscribed": obj.get("unsubscribed"),
            "bounced": obj.get("bounced"),
            "spam": obj.get("spam"),
            "created": obj.get("created"),
            "updated": obj.get("updated"),
            "blocked": obj.get("blocked"),
            "dropped": obj.get("dropped"),
            "LTV": obj.get("LTV"),
            "contactSource": obj.get("contactSource"),
            "lastTrackedIp": obj.get("lastTrackedIp")
        })
        return _obj

