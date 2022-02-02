# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.synthetics_api_test_result_failure import SyntheticsApiTestResultFailure
    from datadog_api_client.v1.model.synthetics_ssl_certificate import SyntheticsSSLCertificate
    from datadog_api_client.v1.model.synthetics_test_process_status import SyntheticsTestProcessStatus
    from datadog_api_client.v1.model.synthetics_timing import SyntheticsTiming

    globals()["SyntheticsApiTestResultFailure"] = SyntheticsApiTestResultFailure
    globals()["SyntheticsSSLCertificate"] = SyntheticsSSLCertificate
    globals()["SyntheticsTestProcessStatus"] = SyntheticsTestProcessStatus
    globals()["SyntheticsTiming"] = SyntheticsTiming


class SyntheticsAPITestResultData(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "cert": (SyntheticsSSLCertificate,),
            "event_type": (SyntheticsTestProcessStatus,),
            "failure": (SyntheticsApiTestResultFailure,),
            "http_status_code": (int,),
            "request_headers": ({str: (dict,)},),
            "response_body": (str,),
            "response_headers": ({str: (dict,)},),
            "response_size": (int,),
            "timings": (SyntheticsTiming,),
        }

    attribute_map = {
        "cert": "cert",
        "event_type": "eventType",
        "failure": "failure",
        "http_status_code": "httpStatusCode",
        "request_headers": "requestHeaders",
        "response_body": "responseBody",
        "response_headers": "responseHeaders",
        "response_size": "responseSize",
        "timings": "timings",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """SyntheticsAPITestResultData - a model defined in OpenAPI

        Keyword Args:
            cert (SyntheticsSSLCertificate): [optional]
            event_type (SyntheticsTestProcessStatus): [optional]
            failure (SyntheticsApiTestResultFailure): [optional]
            http_status_code (int): [optional] The API test HTTP status code.
            request_headers ({str: (dict,)}): [optional] Request header object used for the API test.
            response_body (str): [optional] Response body returned for the API test.
            response_headers ({str: (dict,)}): [optional] Response headers returned for the API test.
            response_size (int): [optional] Global size in byte of the API test response.
            timings (SyntheticsTiming): [optional]
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SyntheticsAPITestResultData, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
