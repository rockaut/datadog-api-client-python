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
    from datadog_api_client.v2.model.list_apis_response_data import ListAPIsResponseData
    from datadog_api_client.v2.model.list_apis_response_meta import ListAPIsResponseMeta


class ListAPIsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.list_apis_response_data import ListAPIsResponseData
        from datadog_api_client.v2.model.list_apis_response_meta import ListAPIsResponseMeta

        return {
            "data": ([ListAPIsResponseData],),
            "meta": (ListAPIsResponseMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: Union[List[ListAPIsResponseData], UnsetType] = unset,
        meta: Union[ListAPIsResponseMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        Response for ``ListAPIs``.

        :param data: List of API items.
        :type data: [ListAPIsResponseData], optional

        :param meta: Metadata for ``ListAPIsResponse``.
        :type meta: ListAPIsResponseMeta, optional
        """
        if data is not unset:
            kwargs["data"] = data
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)
