from __future__ import annotations

from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from tools.acedata_client import AceDataSerpClient


class SerpGoogleTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        result = AceDataSerpClient(self.runtime.credentials.get("acedata_bearer_token", "")).invoke(
            "serp_google", tool_parameters
        )
        yield self.create_json_message(result)
        for name, value in result.items():
            yield self.create_variable_message(name, value)
        for url in result["media_urls"]:
            if (
                "search" == "image"
                or "search" == "mixed"
                and any(
                    suffix in url.lower().split("?")[0]
                    for suffix in [".png", ".jpg", ".jpeg", ".webp"]
                )
            ):
                yield self.create_image_message(url)
            else:
                yield self.create_link_message(url)
