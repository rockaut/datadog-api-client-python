"""
Get all log-based metrics returns "OK" response
"""

from datadog_api_client.v2 import ApiClient, Configuration
from datadog_api_client.v2.api.logs_metrics_api import LogsMetricsApi

with ApiClient(Configuration()) as api_client:
    api_instance = LogsMetricsApi(api_client)
    response = api_instance.list_logs_metrics()

    print(response)
