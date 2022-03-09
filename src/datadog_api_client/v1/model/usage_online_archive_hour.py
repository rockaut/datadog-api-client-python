# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


class UsageOnlineArchiveHour(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "hour": (datetime,),
            "online_archive_events_count": (int,),
            "org_name": (str,),
            "public_id": (str,),
        }

    attribute_map = {
        "hour": "hour",
        "online_archive_events_count": "online_archive_events_count",
        "org_name": "org_name",
        "public_id": "public_id",
    }

    def __init__(self, *args, **kwargs):
        """
        Online Archive usage in a given hour.

        :param hour: The hour for the usage.
        :type hour: datetime, optional

        :param online_archive_events_count: Total count of online archived events within the hour.
        :type online_archive_events_count: int, optional

        :param org_name: The organization name.
        :type org_name: str, optional

        :param public_id: The organization public ID.
        :type public_id: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(UsageOnlineArchiveHour, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self