# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ServiceDefinitionV2Doc(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "name": (str,),
            "provider": (str,),
            "url": (str,),
        }

    attribute_map = {
        "name": "name",
        "provider": "provider",
        "url": "url",
    }

    def __init__(self_, name, url, *args, **kwargs):
        """
        Service documents.

        :param name: Document name.
        :type name: str

        :param provider: Document provider.
        :type provider: str, optional

        :param url: Document URL.
        :type url: str
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)

        self_.name = name
        self_.url = url