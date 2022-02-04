# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.synthetics_private_location_secrets_authentication import (
        SyntheticsPrivateLocationSecretsAuthentication,
    )
    from datadog_api_client.v1.model.synthetics_private_location_secrets_config_decryption import (
        SyntheticsPrivateLocationSecretsConfigDecryption,
    )

    globals()["SyntheticsPrivateLocationSecretsAuthentication"] = SyntheticsPrivateLocationSecretsAuthentication
    globals()["SyntheticsPrivateLocationSecretsConfigDecryption"] = SyntheticsPrivateLocationSecretsConfigDecryption


class SyntheticsPrivateLocationSecrets(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "authentication": (SyntheticsPrivateLocationSecretsAuthentication,),
            "config_decryption": (SyntheticsPrivateLocationSecretsConfigDecryption,),
        }

    attribute_map = {
        "authentication": "authentication",
        "config_decryption": "config_decryption",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """SyntheticsPrivateLocationSecrets - a model defined in OpenAPI


        :type authentication: SyntheticsPrivateLocationSecretsAuthentication, optional

        :type config_decryption: SyntheticsPrivateLocationSecretsConfigDecryption, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SyntheticsPrivateLocationSecrets, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
