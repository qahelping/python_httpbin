from urllib.parse import urljoin

from aiohttp import ClientSession

from dataclasses import dataclass, field


ACCEPT = "text/plain"
CONFIG = "https://httpbin.org/"


@dataclass
class HttpBin:
    session: ClientSession = field(init=True, default_factory=ClientSession)

    async def get_status(self, status: str):
        endpoint = f"/status/{status}"
        url = urljoin(CONFIG, endpoint)
        headers = {"accept": ACCEPT}
        response = await self.session.get(url, headers=headers)
        return response

    async def post_response_headers(self, freeform: str):
        endpoint = f"/response-headers"
        url = urljoin(CONFIG, endpoint)
        params = {"freeform": freeform}
        headers = {"accept": ACCEPT}
        response = await self.session.post(url, headers=headers, params=params)
        return response

    async def redirect(self, n: str):
        endpoint = f"/redirect/{n}"
        url = urljoin(CONFIG, endpoint)
        headers = {"accept": ACCEPT}
        response = await self.session.get(url, headers=headers)
        content = await response.json(content_type=None)
        redirect_url = content["url"]
        return response, redirect_url

    async def close(self) -> None:
        await self.session.close()
