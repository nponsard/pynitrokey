# coding: utf-8

"""
    NetHSM
    All endpoints expect exactly the specified JSON. Additional properties will cause a Bad Request Error (400). All HTTP errors contain a JSON structure with an explanation of type string. All [base64](https://tools.ietf.org/html/rfc4648#section-4) encoded values are Big Endian.   # noqa: E501
    The version of the OpenAPI document: v1
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""


from pynitrokey.nethsm.client.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]
from pynitrokey.nethsm.client.components.schema import info_data
Schema: typing_extensions.TypeAlias = info_data.InfoData
