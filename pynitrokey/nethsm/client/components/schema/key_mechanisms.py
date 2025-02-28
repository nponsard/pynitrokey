# coding: utf-8

"""
    NetHSM
    All endpoints expect exactly the specified JSON. Additional properties will cause a Bad Request Error (400). All HTTP errors contain a JSON structure with an explanation of type string. All [base64](https://tools.ietf.org/html/rfc4648#section-4) encoded values are Big Endian.   # noqa: E501
    The version of the OpenAPI document: v1
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from pynitrokey.nethsm.client.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]


from pynitrokey.nethsm.client.components.schema import key_mechanism


class KeyMechanismsTuple(
    typing.Tuple[
        typing.Literal["RSA_Decryption_RAW", "RSA_Decryption_PKCS1", "RSA_Decryption_OAEP_MD5", "RSA_Decryption_OAEP_SHA1", "RSA_Decryption_OAEP_SHA224", "RSA_Decryption_OAEP_SHA256", "RSA_Decryption_OAEP_SHA384", "RSA_Decryption_OAEP_SHA512", "RSA_Signature_PKCS1", "RSA_Signature_PSS_MD5", "RSA_Signature_PSS_SHA1", "RSA_Signature_PSS_SHA224", "RSA_Signature_PSS_SHA256", "RSA_Signature_PSS_SHA384", "RSA_Signature_PSS_SHA512", "EdDSA_Signature", "ECDSA_Signature", "AES_Encryption_CBC", "AES_Decryption_CBC"],
        ...
    ]
):

    def __new__(cls, arg: typing.Union[KeyMechanismsTupleInput, KeyMechanismsTuple], configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None):
        return KeyMechanisms.validate(arg, configuration=configuration)
KeyMechanismsTupleInput = typing.Union[
    typing.List[
        typing.Literal[
            "RSA_Decryption_RAW",
            "RSA_Decryption_PKCS1",
            "RSA_Decryption_OAEP_MD5",
            "RSA_Decryption_OAEP_SHA1",
            "RSA_Decryption_OAEP_SHA224",
            "RSA_Decryption_OAEP_SHA256",
            "RSA_Decryption_OAEP_SHA384",
            "RSA_Decryption_OAEP_SHA512",
            "RSA_Signature_PKCS1",
            "RSA_Signature_PSS_MD5",
            "RSA_Signature_PSS_SHA1",
            "RSA_Signature_PSS_SHA224",
            "RSA_Signature_PSS_SHA256",
            "RSA_Signature_PSS_SHA384",
            "RSA_Signature_PSS_SHA512",
            "EdDSA_Signature",
            "ECDSA_Signature",
            "AES_Encryption_CBC",
            "AES_Decryption_CBC"
        ],
    ],
    typing.Tuple[
        typing.Literal[
            "RSA_Decryption_RAW",
            "RSA_Decryption_PKCS1",
            "RSA_Decryption_OAEP_MD5",
            "RSA_Decryption_OAEP_SHA1",
            "RSA_Decryption_OAEP_SHA224",
            "RSA_Decryption_OAEP_SHA256",
            "RSA_Decryption_OAEP_SHA384",
            "RSA_Decryption_OAEP_SHA512",
            "RSA_Signature_PKCS1",
            "RSA_Signature_PSS_MD5",
            "RSA_Signature_PSS_SHA1",
            "RSA_Signature_PSS_SHA224",
            "RSA_Signature_PSS_SHA256",
            "RSA_Signature_PSS_SHA384",
            "RSA_Signature_PSS_SHA512",
            "EdDSA_Signature",
            "ECDSA_Signature",
            "AES_Encryption_CBC",
            "AES_Decryption_CBC"
        ],
        ...
    ]
]


@dataclasses.dataclass(frozen=True)
class KeyMechanisms(
    schemas.Schema[schemas.immutabledict, KeyMechanismsTuple]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """
    types: typing.FrozenSet[typing.Type] = frozenset({tuple})
    items: typing.Type[key_mechanism.KeyMechanism] = dataclasses.field(default_factory=lambda: key_mechanism.KeyMechanism) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            tuple: KeyMechanismsTuple
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            KeyMechanismsTupleInput,
            KeyMechanismsTuple,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> KeyMechanismsTuple:
        return super().validate_base(
            arg,
            configuration=configuration,
        )
