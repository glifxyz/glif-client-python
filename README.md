# GLIF client

A python client to interact with the [Glif](https://glif.app/glifs) API.

## Quickstart

```shell
pip install glif-client
```

Create a Glif account and create a new API token [here](https://glif.app/settings/api-tokens).

```python
from glif_client import GlifClient

glif_api_token = "your super secret token here"
# supply `api_token` or set it as an environment variable named GLIF_API_TOKEN
glif_api = GlifClient(api_token=glif_api_token, verbose=True)

# option 1, positional args
simple_args = ["a happy horse", "living on a farm", "in France"]
response = glif_api.run_simple("clgh1vxtu0011mo081dplq3xs", simple_args)
print(response)

# option 2, named args
named_args = {
    "subject": "a happy horse",
    "actionName": "living on a farm",
    "location": "in France"
  }
response = glif_api.run_simple("clgh1vxtu0011mo081dplq3xs", named_args)
print(response)
```

### Enable debugging

```python
import logging

logging.basicConfig(level=logging.DEBUG)
```

## Links

- More API docs: https://docs.glif.app/api/getting-started
