# coding: utf-8

"""
    NetHSM
    All endpoints expect exactly the specified JSON. Additional properties will cause a Bad Request Error (400). All HTTP errors contain a JSON structure with an explanation of type string. All [base64](https://tools.ietf.org/html/rfc4648#section-4) encoded values are Big Endian.   # noqa: E501
    The version of the OpenAPI document: v1
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from pynitrokey.nethsm.client.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]



class LogLevelEnums:

    @schemas.classproperty
    def DEBUG(cls) -> typing.Literal["debug"]:
        return LogLevel.validate("debug")

    @schemas.classproperty
    def INFO(cls) -> typing.Literal["info"]:
        return LogLevel.validate("info")

    @schemas.classproperty
    def WARNING(cls) -> typing.Literal["warning"]:
        return LogLevel.validate("warning")

    @schemas.classproperty
    def ERROR(cls) -> typing.Literal["error"]:
        return LogLevel.validate("error")


@dataclasses.dataclass(frozen=True)
class LogLevel(
    schemas.Schema
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """
    types: typing.FrozenSet[typing.Type] = frozenset({
        str,
    })
    enum_value_to_name: typing.Mapping[typing.Union[int, float, str, schemas.Bool, None], str] = dataclasses.field(
        default_factory=lambda: {
            "debug": "DEBUG",
            "info": "INFO",
            "warning": "WARNING",
            "error": "ERROR",
        }
    )
    enums = LogLevelEnums

    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing.Literal["debug"],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Literal["debug"]: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing.Literal["info"],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Literal["info"]: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing.Literal["warning"],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Literal["warning"]: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing.Literal["error"],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Literal["error"]: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: str,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Literal["debug","info","warning","error",]: ...
    @classmethod
    def validate(
        cls,
        arg,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Literal[
        "debug",
        "info",
        "warning",
        "error",
    ]:
        validated_arg = super().validate_base(
            arg,
            configuration=configuration,
        )
        return typing.cast(typing.Literal[
                "debug",
                "info",
                "warning",
                "error",
            ],
            validated_arg
        )
