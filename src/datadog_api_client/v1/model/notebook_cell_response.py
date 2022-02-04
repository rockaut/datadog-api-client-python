# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.notebook_cell_resource_type import NotebookCellResourceType
    from datadog_api_client.v1.model.notebook_cell_response_attributes import NotebookCellResponseAttributes

    globals()["NotebookCellResourceType"] = NotebookCellResourceType
    globals()["NotebookCellResponseAttributes"] = NotebookCellResponseAttributes


class NotebookCellResponse(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "attributes": (NotebookCellResponseAttributes,),
            "id": (str,),
            "type": (NotebookCellResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    read_only_vars = {}

    def __init__(self, attributes, id, type, *args, **kwargs):
        """NotebookCellResponse - a model defined in OpenAPI


        :type attributes: NotebookCellResponseAttributes

        :param id: Notebook cell ID.
        :type id: str

        :type type: NotebookCellResourceType
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.attributes = attributes
        self.id = id
        self.type = type

    @classmethod
    def _from_openapi_data(cls, attributes, id, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(NotebookCellResponse, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.attributes = attributes
        self.id = id
        self.type = type
        return self
