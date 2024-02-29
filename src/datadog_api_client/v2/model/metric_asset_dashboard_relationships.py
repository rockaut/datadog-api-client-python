# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.metric_asset_dashboard_relationship import MetricAssetDashboardRelationship


class MetricAssetDashboardRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.metric_asset_dashboard_relationship import MetricAssetDashboardRelationship

        return {
            "data": ([MetricAssetDashboardRelationship],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[List[MetricAssetDashboardRelationship], UnsetType] = unset, **kwargs):
        """
        An object containing the list of dashboards that can be referenced in the ``included`` data.

        :param data: A list of dashboards that can be referenced in the ``included`` data.
        :type data: [MetricAssetDashboardRelationship], optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
