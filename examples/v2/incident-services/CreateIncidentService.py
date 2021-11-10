"""
Create a new incident service returns "CREATED" response
"""

from datadog_api_client.v2 import ApiClient, Configuration
from datadog_api_client.v2.api.incident_services_api import IncidentServicesApi
from datadog_api_client.v2.model.incident_service_create_attributes import IncidentServiceCreateAttributes
from datadog_api_client.v2.model.incident_service_create_data import IncidentServiceCreateData
from datadog_api_client.v2.model.incident_service_create_request import IncidentServiceCreateRequest
from datadog_api_client.v2.model.incident_service_type import IncidentServiceType

body = IncidentServiceCreateRequest(
    data=IncidentServiceCreateData(
        type=IncidentServiceType("services"),
        attributes=IncidentServiceCreateAttributes(
            name="Example-Create_a_new_incident_service_returns_CREATED_response"
        ),
    )
)

with ApiClient(Configuration()) as api_client:
    api_instance = IncidentServicesApi(api_client)
    response = api_instance.create_incident_service(body=body)

    print(response)
