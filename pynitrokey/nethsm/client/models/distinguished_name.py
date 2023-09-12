# coding: utf-8

"""
    NetHSM

    All endpoints expect exactly the specified JSON. Additional properties will cause a Bad Request Error (400). All HTTP errors contain a JSON structure with an explanation of type string. All [base64](https://tools.ietf.org/html/rfc4648#section-4) encoded values are Big Endian. 

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr

class DistinguishedName(BaseModel):
    """
    DistinguishedName
    """
    country_name: Optional[StrictStr] = Field(None, alias="countryName")
    state_or_province_name: Optional[StrictStr] = Field(None, alias="stateOrProvinceName")
    locality_name: Optional[StrictStr] = Field(None, alias="localityName")
    organization_name: Optional[StrictStr] = Field(None, alias="organizationName")
    organizational_unit_name: Optional[StrictStr] = Field(None, alias="organizationalUnitName")
    common_name: StrictStr = Field(..., alias="commonName")
    email_address: Optional[StrictStr] = Field(None, alias="emailAddress")
    __properties = ["countryName", "stateOrProvinceName", "localityName", "organizationName", "organizationalUnitName", "commonName", "emailAddress"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> DistinguishedName:
        """Create an instance of DistinguishedName from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DistinguishedName:
        """Create an instance of DistinguishedName from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DistinguishedName.parse_obj(obj)

        _obj = DistinguishedName.parse_obj({
            "country_name": obj.get("countryName"),
            "state_or_province_name": obj.get("stateOrProvinceName"),
            "locality_name": obj.get("localityName"),
            "organization_name": obj.get("organizationName"),
            "organizational_unit_name": obj.get("organizationalUnitName"),
            "common_name": obj.get("commonName"),
            "email_address": obj.get("emailAddress")
        })
        return _obj


