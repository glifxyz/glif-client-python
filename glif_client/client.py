import json
import os
from typing import Optional, Union
from urllib.parse import urljoin

import aiohttp
import requests
from dotenv import load_dotenv

import logging

class URLPath:
    """
    Example usage
    ```
    base_url = URLPath('https://api.example.com')
    endpoint = base_url / 'data' / 'users'
    print(endpoint)
    ```
    """

    def __init__(self, base_url: str) -> None:
        self.base_url = base_url

    def __truediv__(self, other: str) -> "URLPath":
        return URLPath(urljoin(self.base_url + "/", other))

    def __str__(self) -> str:
        return self.base_url


class GlifClient:
    simple_api_url = URLPath("https://simple-api.glif.app")
    api_url = URLPath("https://glif.app/api")

    def __init__(
        self,
        api_token: Optional[str] = None,
    ):
        if api_token:
            self.api_token = api_token
        else:
            load_dotenv()
            self.api_token = os.getenv("GLIF_API_TOKEN")
        if not self.api_token:
            raise ValueError("api_token is not set")

    @property
    def headers(self) -> dict:
        return {"Authorization": f"Bearer {self.api_token}"}
    

    def run_simple(self, glif_id: str, inputs: Optional[dict] = None) -> dict:
        if inputs is None:
            inputs = {}
        logging.debug(f"Running {glif_id} with inputs: {inputs}")
        response = requests.post(
            self.simple_api_url,
            json={"id": glif_id, "inputs": inputs},
            headers=self.headers,
        )
        return_data = json.loads(response.content)

        logging.debug(f"Output from run_simple: {return_data=}")
        return return_data["output"]

    async def arun_simple(self, glif_id: str, inputs: Optional[dict] = None) -> dict:
        if inputs is None:
            inputs = {}
        logging.debug(f"Running {glif_id} with inputs: {inputs}")
        async with aiohttp.ClientSession() as session:
            async with session.post(
                url=str(self.simple_api_url),
                json={"id": glif_id, "inputs": inputs},
                headers=self.headers,
            ) as response:
                return_data = await response.json()

        logging.debug(f"Output from arun_simple: {return_data=}")
        return return_data["output"]

    async def arun(self, glif_id: str, inputs: Optional[dict] = None) -> dict:
        if inputs is None:
            inputs = {}
        logging.debug(f"Running {glif_id} with inputs: {inputs}")
        async with aiohttp.ClientSession() as session:
            async with session.post(
                url=str(self.api_url),
                json={"id": glif_id, "inputs": inputs},
                headers=self.headers,
            ) as response:
                async for data in response.content.iter_any():
                    # Decode each chunk and split by newline to get individual JSON strings
                    for line in data.decode("utf-8").split("\n"):
                        if line:  # Check if the line is not empty
                            try:
                                json_data = json.loads(line)
                                logging.debug(f"Output from arun: {json_data=}")
                                if json_data["type"] == "result":
                                    return json_data["result"]["output"]["value"]
                            except json.JSONDecodeError:
                                # print(f"Error decoding JSON: {e} - raw: {line}")
                                pass  # streaming error?
