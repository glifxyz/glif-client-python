import asyncio
import logging
import os
from typing import Optional
from urllib.parse import urljoin

import aiohttp
from pprint import pformat

logger = logging.getLogger(__name__)

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
        if api_token is not None:
            self.api_token = api_token
        else:
            self.api_token = os.getenv("GLIF_API_TOKEN")
        if not self.api_token:
            raise ValueError("api_token is not set")

    @property
    def headers(self) -> dict:
        return {"Authorization": f"Bearer {self.api_token}"}

    def run_simple(self, glif_id: str, inputs: Optional[list | dict] = None) -> str:
        return asyncio.run(self.arun_simple(glif_id, inputs))

    async def arun_simple(
        self, glif_id: str, inputs: Optional[list | dict] = None
    ) -> str:
        if inputs is None:
            inputs = {}
        logger.debug(f"Running {glif_id} with inputs: {pformat(inputs)}")
        async with aiohttp.ClientSession() as session:
            async with session.post(
                url=str(self.simple_api_url),
                json={"id": glif_id, "inputs": inputs},
                headers=self.headers,
            ) as response:
                return_data = await response.json()

        logger.debug(f"Output from arun_simple: {pformat(return_data)}")
        return return_data["output"]
