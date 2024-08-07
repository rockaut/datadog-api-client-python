# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class SLODataSourceQueryDefinition(ModelComposed):
    def __init__(self, **kwargs):
        """
        A formula and function query.

        :param aggregator: The aggregation methods available for metrics queries.
        :type aggregator: FormulaAndFunctionMetricAggregation, optional

        :param cross_org_uuids: The source organization UUID for cross organization queries. Feature in Private Beta.
        :type cross_org_uuids: [str], optional

        :param data_source: Data source for metrics queries.
        :type data_source: FormulaAndFunctionMetricDataSource

        :param name: Name of the query for use in formulas.
        :type name: str

        :param query: Metrics query definition.
        :type query: str
        """
        super().__init__(kwargs)

    @cached_property
    def _composed_schemas(_):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        from datadog_api_client.v1.model.formula_and_function_metric_query_definition import (
            FormulaAndFunctionMetricQueryDefinition,
        )

        return {
            "oneOf": [
                FormulaAndFunctionMetricQueryDefinition,
            ],
        }
