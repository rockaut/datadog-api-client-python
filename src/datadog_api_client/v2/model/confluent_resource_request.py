# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ConfluentResourceRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.confluent_resource_request_data import ConfluentResourceRequestData

        return {
            "data": (ConfluentResourceRequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data, *args, **kwargs):
        """
        The JSON:API request for updating a Confluent resource.

        :param data: JSON:API request for updating a Confluent resource.
        :type data: ConfluentResourceRequestData
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)

        self_.data = data