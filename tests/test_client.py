import logging

from glif_client import GlifClient


def test_client_simple():
    glif_api = GlifClient()

    simple_args = ["a happy horse", "foobar"]
    response = glif_api.run_simple("cm023wc6m0009k7ur9ta0g14f", simple_args)
    logging.info(f"Response: {response}")
    assert isinstance(response, str)


def test_client_arged():
    glif_api = GlifClient()

    named_args = {
        "prompt": "a happy horse",
        "other_parameter": "foobar",
    }
    response = glif_api.run_simple("cm023wc6m0009k7ur9ta0g14f", named_args)
    logging.info(f"Response: {response}")
    assert isinstance(response, str)
