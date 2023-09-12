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



from pydantic import BaseModel, Field, constr

class UserPassphrasePostData(BaseModel):
    """
    UserPassphrasePostData
    """
    passphrase: constr(strict=True, min_length=1) = Field(...)
    __properties = ["passphrase"]

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
    def from_json(cls, json_str: str) -> UserPassphrasePostData:
        """Create an instance of UserPassphrasePostData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UserPassphrasePostData:
        """Create an instance of UserPassphrasePostData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UserPassphrasePostData.parse_obj(obj)

        _obj = UserPassphrasePostData.parse_obj({
            "passphrase": obj.get("passphrase")
        })
        return _obj


