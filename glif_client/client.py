import os
from dotenv import load_dotenv
import requests
import aiohttp
import json

load_dotenv()

class GlifClient:
    GLIF_API_TOKEN = os.getenv("GLIF_API_TOKEN")

    def __init__(
        self,
        verbose : bool = False,
    ):
        self.simple_api_url = "https://simple-api.glif.app"
        self.api_url = "https://alpha.glif.xyz/api/graph-run"

        if not self.GLIF_API_TOKEN:
            raise ValueError("GLIF_API_TOKEN is not set")
        self.verbose = verbose

    def get_headers(self) -> dict:
        return {"Authorization": f"Bearer {self.GLIF_API_TOKEN}"}
    
    def run_simple(self, glif_id: str, inputs: dict) -> dict:
        if self.verbose:
            print(f"Running {glif_id} with inputs: {inputs}")
        response = requests.post(
            self.simple_api_url,
            json={"id": glif_id, "inputs": inputs},
            headers=self.get_headers(),
        )
        return_data = json.loads(response.content)
        if self.verbose:
            print(return_data)
        return return_data["output"]

    async def arun_simple(self, glif_id: str, inputs: dict) -> dict:
        if self.verbose:
            print(f"Running {glif_id} with inputs: {inputs}")
        async with aiohttp.ClientSession() as session:
            async with session.post(
                url=f"{self.simple_api_url}/{glif_id}",
                json=inputs,
                headers=self.get_headers(),
            ) as response:
                return_data = await response.json()
                if self.verbose:
                    print(return_data)
                return return_data["output"]

    async def arun(self, glif_id: str, inputs: dict) -> dict:
        async with aiohttp.ClientSession() as session:
            async with session.post(
                "https://glif.app/api",
                json={"id": glif_id, "inputs": inputs},
                headers=self.get_headers(),
            ) as response:
                print(response)
                async for data in response.content.iter_any():
                    # Decode each chunk and split by newline to get individual JSON strings
                    for line in data.decode("utf-8").split("\n"):
                        if line:  # Check if the line is not empty
                            try:
                                json_data = json.loads(line)
                                if self.verbose:
                                    print(json_data)
                                if json_data["type"] == "result":
                                    return json_data["result"]["output"]["value"]
                            except json.JSONDecodeError:
                                # print(f"Error decoding JSON: {e} - raw: {line}")
                                pass  # streaming error?