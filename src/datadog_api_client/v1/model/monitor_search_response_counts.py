# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.monitor_search_count import MonitorSearchCount

    globals()["MonitorSearchCount"] = MonitorSearchCount


class MonitorSearchResponseCounts(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "muted": (MonitorSearchCount,),
            "status": (MonitorSearchCount,),
            "tag": (MonitorSearchCount,),
            "type": (MonitorSearchCount,),
        }

    attribute_map = {
        "muted": "muted",
        "status": "status",
        "tag": "tag",
        "type": "type",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """MonitorSearchResponseCounts - a model defined in OpenAPI


        :type muted: MonitorSearchCount, optional

        :type status: MonitorSearchCount, optional

        :type tag: MonitorSearchCount, optional

        :type type: MonitorSearchCount, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(MonitorSearchResponseCounts, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
