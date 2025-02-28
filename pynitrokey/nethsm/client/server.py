# coding: utf-8
"""
    NetHSM
    All endpoints expect exactly the specified JSON. Additional properties will cause a Bad Request Error (400). All HTTP errors contain a JSON structure with an explanation of type string. All [base64](https://tools.ietf.org/html/rfc4648#section-4) encoded values are Big Endian.   # noqa: E501
    The version of the OpenAPI document: v1
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
import abc
import dataclasses
import typing

from pynitrokey.nethsm.client.schemas import validation, schema


@dataclasses.dataclass
class ServerWithoutVariables(abc.ABC):
    url: str


@dataclasses.dataclass
class ServerWithVariables(abc.ABC):
    _url: str
    variables: validation.immutabledict[str, str]
    variables_schema: typing.Type[schema.Schema]
    url: str = dataclasses.field(init=False)

    def __post_init__(self):
        url = self._url
        assert isinstance (self.variables, self.variables_schema().type_to_output_cls[validation.immutabledict])
        for (key, value) in self.variables.items():
            url = url.replace("{" + key + "}", value)
        self.url = url
