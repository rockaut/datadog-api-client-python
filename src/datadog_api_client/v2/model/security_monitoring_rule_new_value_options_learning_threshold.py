# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class SecurityMonitoringRuleNewValueOptionsLearningThreshold(ModelSimple):

    allowed_values = {
        "value": {
            "ZERO_OCCURRENCES": 0,
            "ONE_OCCURRENCE": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (int,),
        }

    def __init__(self, *args, **kwargs):
        """
        A number of occurrences after which signals will be generated for values that weren't learned.

        Note that value can be passed either in args or in kwargs, but not in both.

        :param value: If omitted defaults to 0. Must be one of [0, 1].
        :type value: int
        """
        super().__init__(kwargs)

        if "value" in kwargs:
            value = kwargs.pop("value")
        elif args:
            args = list(args)
            value = args.pop(0)
        else:
            value = 0

        self._check_pos_args(args)

        self.value = value

        self._check_kw_args(kwargs)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""
        return cls(*args, **kwargs)