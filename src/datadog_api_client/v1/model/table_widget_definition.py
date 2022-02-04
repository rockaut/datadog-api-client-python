# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.table_widget_definition_type import TableWidgetDefinitionType
    from datadog_api_client.v1.model.table_widget_has_search_bar import TableWidgetHasSearchBar
    from datadog_api_client.v1.model.table_widget_request import TableWidgetRequest
    from datadog_api_client.v1.model.widget_custom_link import WidgetCustomLink
    from datadog_api_client.v1.model.widget_text_align import WidgetTextAlign
    from datadog_api_client.v1.model.widget_time import WidgetTime

    globals()["TableWidgetDefinitionType"] = TableWidgetDefinitionType
    globals()["TableWidgetHasSearchBar"] = TableWidgetHasSearchBar
    globals()["TableWidgetRequest"] = TableWidgetRequest
    globals()["WidgetCustomLink"] = WidgetCustomLink
    globals()["WidgetTextAlign"] = WidgetTextAlign
    globals()["WidgetTime"] = WidgetTime


class TableWidgetDefinition(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "custom_links": ([WidgetCustomLink],),
            "has_search_bar": (TableWidgetHasSearchBar,),
            "requests": ([TableWidgetRequest],),
            "time": (WidgetTime,),
            "title": (str,),
            "title_align": (WidgetTextAlign,),
            "title_size": (str,),
            "type": (TableWidgetDefinitionType,),
        }

    attribute_map = {
        "requests": "requests",
        "type": "type",
        "custom_links": "custom_links",
        "has_search_bar": "has_search_bar",
        "time": "time",
        "title": "title",
        "title_align": "title_align",
        "title_size": "title_size",
    }

    read_only_vars = {}

    def __init__(self, requests, type, *args, **kwargs):
        """TableWidgetDefinition - a model defined in OpenAPI


        :param requests: Widget definition.
        :type requests: [TableWidgetRequest]

        :type type: TableWidgetDefinitionType

        :param custom_links: List of custom links.
        :type custom_links: [WidgetCustomLink], optional

        :type has_search_bar: TableWidgetHasSearchBar, optional

        :type time: WidgetTime, optional

        :param title: Title of your widget.
        :type title: str, optional

        :type title_align: WidgetTextAlign, optional

        :param title_size: Size of the title.
        :type title_size: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.requests = requests
        self.type = type

    @classmethod
    def _from_openapi_data(cls, requests, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(TableWidgetDefinition, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.requests = requests
        self.type = type
        return self
