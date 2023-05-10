# scarlet-shark-python
Scarlet Shark REST API Python client.

## Installation
```
pip install scarlet-shark-client
```

## Usage example

```python
from scarlet_shark_client.client import ClientFactory

client = ClientFactory.get_client('<your API key>', api_version='v0.4', print_json=True)
result = client.search_domain(domain='scarletshark.com')
```
prints
```json
{
  "age": 4043,
  "associated_urls": [],
  "classification": "security",
  "disclosure_email": "unknown",
  "domain": "scarletshark.com",
  "domain_description": "",
  "ip": "40.[redacted]",
  "reference_url": "",
  "registered": "2012-04-02",
  "service": {
    "service_email": "",
    "service_id": 0,
    "service_name": "unknown",
    "service_trust": "unknown",
    "service_type": "unknown",
    "service_url": ""
  },
  "tags": [
    "security"
  ],
  "threat_actor_aliases": [],
  "threat_actor_id": 0,
  "threat_classification": "safe",
  "threat_explanation": "The domain is considered to be safe and it hosts no known malicious content.",
  "tracking_domain": false
}
```

## Supported actions
### API version 0.4
* search_dns
* search_domain
* search_email
* search_hash
* search_ip
* search_network
* search_threat_actors
* search_threat_tools
* search_url