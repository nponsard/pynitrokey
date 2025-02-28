# coding: utf-8

"""
    NetHSM
    All endpoints expect exactly the specified JSON. Additional properties will cause a Bad Request Error (400). All HTTP errors contain a JSON structure with an explanation of type string. All [base64](https://tools.ietf.org/html/rfc4648#section-4) encoded values are Big Endian.   # noqa: E501
    The version of the OpenAPI document: v1
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from pynitrokey.nethsm.client.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]

CountryName: typing_extensions.TypeAlias = schemas.StrSchema
StateOrProvinceName: typing_extensions.TypeAlias = schemas.StrSchema
LocalityName: typing_extensions.TypeAlias = schemas.StrSchema
OrganizationName: typing_extensions.TypeAlias = schemas.StrSchema
OrganizationalUnitName: typing_extensions.TypeAlias = schemas.StrSchema
CommonName: typing_extensions.TypeAlias = schemas.StrSchema
EmailAddress: typing_extensions.TypeAlias = schemas.StrSchema
Properties = typing.TypedDict(
    'Properties',
    {
        "countryName": typing.Type[CountryName],
        "stateOrProvinceName": typing.Type[StateOrProvinceName],
        "localityName": typing.Type[LocalityName],
        "organizationName": typing.Type[OrganizationName],
        "organizationalUnitName": typing.Type[OrganizationalUnitName],
        "commonName": typing.Type[CommonName],
        "emailAddress": typing.Type[EmailAddress],
    }
)


class DistinguishedNameDict(schemas.immutabledict[str, str]):

    __required_keys__: typing.FrozenSet[str] = frozenset({
        "commonName",
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
        "countryName",
        "stateOrProvinceName",
        "localityName",
        "organizationName",
        "organizationalUnitName",
        "emailAddress",
    })
    
    def __new__(
        cls,
        *,
        commonName: str,
        countryName: typing.Union[
            str,
            schemas.Unset
        ] = schemas.unset,
        stateOrProvinceName: typing.Union[
            str,
            schemas.Unset
        ] = schemas.unset,
        localityName: typing.Union[
            str,
            schemas.Unset
        ] = schemas.unset,
        organizationName: typing.Union[
            str,
            schemas.Unset
        ] = schemas.unset,
        organizationalUnitName: typing.Union[
            str,
            schemas.Unset
        ] = schemas.unset,
        emailAddress: typing.Union[
            str,
            schemas.Unset
        ] = schemas.unset,
        configuration_: typing.Optional[schema_configuration.SchemaConfiguration] = None,
        **kwargs: schemas.INPUT_TYPES_ALL,
    ):
        arg_: typing.Dict[str, typing.Any] = {
            "commonName": commonName,
        }
        for key, val in (
            ("countryName", countryName),
            ("stateOrProvinceName", stateOrProvinceName),
            ("localityName", localityName),
            ("organizationName", organizationName),
            ("organizationalUnitName", organizationalUnitName),
            ("emailAddress", emailAddress),
        ):
            if isinstance(val, schemas.Unset):
                continue
            arg_[key] = val
        arg_.update(kwargs)
        used_arg_ = typing.cast(DistinguishedNameDictInput, arg_)
        return DistinguishedName.validate(used_arg_, configuration=configuration_)
    
    @staticmethod
    def from_dict_(
        arg: typing.Union[
            DistinguishedNameDictInput,
            DistinguishedNameDict
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> DistinguishedNameDict:
        return DistinguishedName.validate(arg, configuration=configuration)
    
    @property
    def commonName(self) -> str:
        return typing.cast(
            str,
            self.__getitem__("commonName")
        )
    
    @property
    def countryName(self) -> typing.Union[str, schemas.Unset]:
        val = self.get("countryName", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            str,
            val
        )
    
    @property
    def stateOrProvinceName(self) -> typing.Union[str, schemas.Unset]:
        val = self.get("stateOrProvinceName", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            str,
            val
        )
    
    @property
    def localityName(self) -> typing.Union[str, schemas.Unset]:
        val = self.get("localityName", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            str,
            val
        )
    
    @property
    def organizationName(self) -> typing.Union[str, schemas.Unset]:
        val = self.get("organizationName", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            str,
            val
        )
    
    @property
    def organizationalUnitName(self) -> typing.Union[str, schemas.Unset]:
        val = self.get("organizationalUnitName", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            str,
            val
        )
    
    @property
    def emailAddress(self) -> typing.Union[str, schemas.Unset]:
        val = self.get("emailAddress", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            str,
            val
        )
    
    def get_additional_property_(self, name: str) -> typing.Union[schemas.OUTPUT_BASE_TYPES, schemas.Unset]:
        schemas.raise_if_key_known(name, self.__required_keys__, self.__optional_keys__)
        return self.get(name, schemas.unset)
DistinguishedNameDictInput = typing.Mapping[str, schemas.INPUT_TYPES_ALL]


@dataclasses.dataclass(frozen=True)
class DistinguishedName(
    schemas.Schema[DistinguishedNameDict, tuple]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """
    types: typing.FrozenSet[typing.Type] = frozenset({schemas.immutabledict})
    required: typing.FrozenSet[str] = frozenset({
        "commonName",
    })
    properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: DistinguishedNameDict
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            DistinguishedNameDictInput,
            DistinguishedNameDict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> DistinguishedNameDict:
        return super().validate_base(
            arg,
            configuration=configuration,
        )

