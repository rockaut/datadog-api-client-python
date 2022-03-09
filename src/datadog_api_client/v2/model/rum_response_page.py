# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v2.model_utils import (
    ModelNormal,
    cached_property,
)


class RUMResponsePage(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "after": (str,),
        }

    attribute_map = {
        "after": "after",
    }

    def __init__(self, *args, **kwargs):
        """
        Paging attributes.

        :param after: The cursor to use to get the next results, if any. To make the next request, use the same parameters with the addition of `page[cursor]`.
        :type after: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(RUMResponsePage, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self