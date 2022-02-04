# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.logs_string_builder_processor_type import LogsStringBuilderProcessorType

    globals()["LogsStringBuilderProcessorType"] = LogsStringBuilderProcessorType


class LogsStringBuilderProcessor(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "is_enabled": (bool,),
            "is_replace_missing": (bool,),
            "name": (str,),
            "target": (str,),
            "template": (str,),
            "type": (LogsStringBuilderProcessorType,),
        }

    attribute_map = {
        "target": "target",
        "template": "template",
        "type": "type",
        "is_enabled": "is_enabled",
        "is_replace_missing": "is_replace_missing",
        "name": "name",
    }

    read_only_vars = {}

    def __init__(self, target, template, type, *args, **kwargs):
        """LogsStringBuilderProcessor - a model defined in OpenAPI


        :param target: The name of the attribute that contains the result of the template.
        :type target: str

        :param template: A formula with one or more attributes and raw text.
        :type template: str

        :type type: LogsStringBuilderProcessorType

        :param is_enabled: Whether or not the processor is enabled. If omitted the server will use the default value of False.
        :type is_enabled: bool, optional

        :param is_replace_missing: If true, it replaces all missing attributes of `template` by an empty string. If `false` (default), skips the operation for missing attributes. If omitted the server will use the default value of False.
        :type is_replace_missing: bool, optional

        :param name: Name of the processor.
        :type name: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.target = target
        self.template = template
        self.type = type

    @classmethod
    def _from_openapi_data(cls, target, template, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(LogsStringBuilderProcessor, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.target = target
        self.template = template
        self.type = type
        return self
