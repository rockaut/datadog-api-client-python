# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.time_series_formula_and_function_event_query_definition_sort import (
    TimeSeriesFormulaAndFunctionEventQueryDefinitionSort,
)

globals()["TimeSeriesFormulaAndFunctionEventQueryDefinitionSort"] = TimeSeriesFormulaAndFunctionEventQueryDefinitionSort
from datadog_api_client.v1.model.time_series_formula_and_function_event_query_definition_group_by import (
    TimeSeriesFormulaAndFunctionEventQueryDefinitionGroupBy,
)


class TestTimeSeriesFormulaAndFunctionEventQueryDefinitionGroupBy(unittest.TestCase):
    """TimeSeriesFormulaAndFunctionEventQueryDefinitionGroupBy unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTimeSeriesFormulaAndFunctionEventQueryDefinitionGroupBy(self):
        """Test TimeSeriesFormulaAndFunctionEventQueryDefinitionGroupBy"""
        # FIXME: construct object with mandatory attributes with example values
        # model = TimeSeriesFormulaAndFunctionEventQueryDefinitionGroupBy()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()