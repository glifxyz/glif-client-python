# GLIF client

A python client to interact with the [Glif](https://glif.app/glifs) API.

## Quickstart

```shell
pip install glif-client
```

Create a Glif account and create a new API token [here](https://glif.app/settings/api-tokens).

```shell
export GLIF_API_TOKEN="your-token"
```

Example:

```python
from glif_client import GlifClient

# supply `api_token` or set it as an environment variable named GLIF_API_TOKEN
glif_api = GlifClient(api_token="your-token")

# option 1, positional args
simple_args = ["a happy horse", "foobar"]
response = glif_api.run_simple("cm023wc6m0009k7ur9ta0g14f", simple_args)
print(response)

# option 2, named args
named_args = {
    "prompt": "a happy horse",
    "other_parameter": "foobar",
}
response = glif_api.run_simple("cm023wc6m0009k7ur9ta0g14f", named_args)
print(response)
```

### Enable debugging

```python
import logging

logging.basicConfig(level=logging.DEBUG)
```

### Dev (unix)

Install dev deps:

```shell
pip install -r requirements.dev.txt
```

There's a makefile with two handy commands:

```shell
make test # run the little test suite
make style # run formatting
```

## Links

- More API docs: https://docs.glif.app/api/getting-started
