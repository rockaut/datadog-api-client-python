# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


class WebhooksIntegrationCustomVariable(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        return {
            "is_secret": (bool,),
            "name": (str,),
            "value": (str,),
        }

    attribute_map = {
        "is_secret": "is_secret",
        "name": "name",
        "value": "value",
    }

    read_only_vars = {}

    def __init__(self, is_secret, name, value, *args, **kwargs):
        """WebhooksIntegrationCustomVariable - a model defined in OpenAPI


        :param is_secret: Make custom variable is secret or not. If the custom variable is secret, the value is not returned in the response payload.
        :type is_secret: bool

        :param name: The name of the variable. It corresponds with `<CUSTOM_VARIABLE_NAME>`.
        :type name: str

        :param value: Value of the custom variable.
        :type value: str
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.is_secret = is_secret
        self.name = name
        self.value = value

    @classmethod
    def _from_openapi_data(cls, is_secret, name, value, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(WebhooksIntegrationCustomVariable, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.is_secret = is_secret
        self.name = name
        self.value = value
        return self
