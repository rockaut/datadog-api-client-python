# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v2.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v2.model.organization_attributes import OrganizationAttributes
    from datadog_api_client.v2.model.organizations_type import OrganizationsType

    globals()["OrganizationAttributes"] = OrganizationAttributes
    globals()["OrganizationsType"] = OrganizationsType


class Organization(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "attributes": (OrganizationAttributes,),
            "id": (str,),
            "type": (OrganizationsType,),
        }

    attribute_map = {
        "type": "type",
        "attributes": "attributes",
        "id": "id",
    }

    read_only_vars = {}

    def __init__(self, type, *args, **kwargs):
        """Organization - a model defined in OpenAPI


        :type type: OrganizationsType

        :type attributes: OrganizationAttributes, optional

        :param id: ID of the organization.
        :type id: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.type = type

    @classmethod
    def _from_openapi_data(cls, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(Organization, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.type = type
        return self
