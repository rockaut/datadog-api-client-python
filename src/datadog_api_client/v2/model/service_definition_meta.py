# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ServiceDefinitionMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "github_html_url": (str,),
            "ingested_schema_version": (str,),
            "ingestion_source": (str,),
            "last_modified_time": (str,),
        }

    attribute_map = {
        "github_html_url": "github-html-url",
        "ingested_schema_version": "ingested-schema-version",
        "ingestion_source": "ingestion-source",
        "last_modified_time": "last-modified-time",
    }

    def __init__(self_, *args, **kwargs):
        """
        Metadata about a service definition.

        :param github_html_url: GitHub HTML URL.
        :type github_html_url: str, optional

        :param ingested_schema_version: Ingestion schema version.
        :type ingested_schema_version: str, optional

        :param ingestion_source: Ingestion source of the service definition.
        :type ingestion_source: str, optional

        :param last_modified_time: Last modified time of the service definition.
        :type last_modified_time: str, optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)