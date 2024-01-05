# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SLOType(ModelSimple):
    """
    The type of the service level objective.

    :param value: Must be one of ["metric", "monitor", "time_slice"].
    :type value: str
    """

    allowed_values = {
        "metric",
        "monitor",
        "time_slice",
    }
    METRIC: ClassVar["SLOType"]
    MONITOR: ClassVar["SLOType"]
    TIME_SLICE: ClassVar["SLOType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SLOType.METRIC = SLOType("metric")
SLOType.MONITOR = SLOType("monitor")
SLOType.TIME_SLICE = SLOType("time_slice")
