# coding: utf-8

"""
    NetHSM
    All endpoints expect exactly the specified JSON. Additional properties will cause a Bad Request Error (400). All HTTP errors contain a JSON structure with an explanation of type string. All [base64](https://tools.ietf.org/html/rfc4648#section-4) encoded values are Big Endian.   # noqa: E501
    The version of the OpenAPI document: v1
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from pynitrokey.nethsm.client.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]


from pynitrokey.nethsm.client.components.schema import id


class TagListTuple(
    typing.Tuple[
        str,
        ...
    ]
):

    def __new__(cls, arg: typing.Union[TagListTupleInput, TagListTuple], configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None):
        return TagList.validate(arg, configuration=configuration)
TagListTupleInput = typing.Union[
    typing.List[
        str,
    ],
    typing.Tuple[
        str,
        ...
    ]
]


@dataclasses.dataclass(frozen=True)
class TagList(
    schemas.Schema[schemas.immutabledict, TagListTuple]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """
    types: typing.FrozenSet[typing.Type] = frozenset({tuple})
    items: typing.Type[id.ID] = dataclasses.field(default_factory=lambda: id.ID) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            tuple: TagListTuple
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            TagListTupleInput,
            TagListTuple,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> TagListTuple:
        return super().validate_base(
            arg,
            configuration=configuration,
        )
