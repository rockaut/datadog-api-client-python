# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SecurityMonitoringSignalRuleResponseQuery(ModelNormal):
    validations = {
        "correlated_query_index": {
            "inclusive_maximum": 9,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_rule_query_aggregation import (
            SecurityMonitoringRuleQueryAggregation,
        )

        return {
            "aggregation": (SecurityMonitoringRuleQueryAggregation,),
            "correlated_by_fields": ([str],),
            "correlated_query_index": (int,),
            "default_rule_id": (str,),
            "metrics": ([str],),
            "name": (str,),
            "rule_id": (str,),
        }

    attribute_map = {
        "aggregation": "aggregation",
        "correlated_by_fields": "correlatedByFields",
        "correlated_query_index": "correlatedQueryIndex",
        "default_rule_id": "defaultRuleId",
        "metrics": "metrics",
        "name": "name",
        "rule_id": "ruleId",
    }

    def __init__(self_, *args, **kwargs):
        """
        Query for matching rule on signals.

        :param aggregation: The aggregation type.
        :type aggregation: SecurityMonitoringRuleQueryAggregation, optional

        :param correlated_by_fields: Fields to group by.
        :type correlated_by_fields: [str], optional

        :param correlated_query_index: Index of the rule query used to retrieve the correlated field.
        :type correlated_query_index: int, optional

        :param default_rule_id: Default Rule ID to match on signals.
        :type default_rule_id: str, optional

        :param metrics: Group of target fields to aggregate over when using the new value aggregations.
        :type metrics: [str], optional

        :param name: Name of the query.
        :type name: str, optional

        :param rule_id: Rule ID to match on signals.
        :type rule_id: str, optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)