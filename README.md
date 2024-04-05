# GLIF client

Supports

- api
- async api
- status
- streaming

```python
from glif_api_wrapper.client import GlifAPI

api_token = "your_api_token_here"
glif_api = GlifAPI(api_token)

# option 1
simple_args = ["a happy horse", "living on a farm", "in France"]
response = glif_api.run_glif("clgh1vxtu0011mo081dplq3xs", simple_args)
print(response)

# option 2
named_args = {
    "subject": "a happy horse",
    "actionName": "living on a farm",
    "location": "in France"
  }
response = glif_api.run_glif("clgh1vxtu0011mo081dplq3xs", named_args)
print(response)
```