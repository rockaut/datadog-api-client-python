# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v2.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v2.model.relationship_to_organization import RelationshipToOrganization
    from datadog_api_client.v2.model.relationship_to_organizations import RelationshipToOrganizations
    from datadog_api_client.v2.model.relationship_to_roles import RelationshipToRoles
    from datadog_api_client.v2.model.relationship_to_users import RelationshipToUsers

    globals()["RelationshipToOrganization"] = RelationshipToOrganization
    globals()["RelationshipToOrganizations"] = RelationshipToOrganizations
    globals()["RelationshipToRoles"] = RelationshipToRoles
    globals()["RelationshipToUsers"] = RelationshipToUsers


class UserResponseRelationships(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "org": (RelationshipToOrganization,),
            "other_orgs": (RelationshipToOrganizations,),
            "other_users": (RelationshipToUsers,),
            "roles": (RelationshipToRoles,),
        }

    attribute_map = {
        "org": "org",
        "other_orgs": "other_orgs",
        "other_users": "other_users",
        "roles": "roles",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """UserResponseRelationships - a model defined in OpenAPI


        :type org: RelationshipToOrganization, optional

        :type other_orgs: RelationshipToOrganizations, optional

        :type other_users: RelationshipToUsers, optional

        :type roles: RelationshipToRoles, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(UserResponseRelationships, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
