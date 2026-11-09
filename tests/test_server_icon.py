"""The server declares the PagerDuty mark as its icon in the initialize result."""

import base64

import anyio
from mcp.client import Client
from mcp.server.mcpserver import MCPServer
from mcp.types import Icon

from pagerduty_mcp import server

# The SVG giantswarm/muster draws for PagerDuty (internal/servericon/brands.go):
# the simple-icons 16.36.0 mark, white on a rounded square in #06AC38.
MUSTER_PAGERDUTY_SVG = (
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">'
    "<title>PagerDuty</title>"
    '<rect width="24" height="24" rx="5" fill="#06AC38"/>'
    '<path transform="translate(5 5) scale(0.5833)" fill="#FFFFFF" d="'
    "M16.965 1.18C15.085.164 13.769 0 10.683 0H3.73v14.55h6.926c2.743 0 4.8-.164 6.61-1.37 1.975-1.303 "
    "3.004-3.484 3.004-6.007 0-2.716-1.262-4.896-3.305-5.994zm-5.5 10.326h-4.21V3.113l3.977-.027c3.62-.028 "
    "5.43 1.234 5.43 4.128 0 3.113-2.248 4.292-5.197 4.292zM3.73 17.61h3.525V24H3.73Z"
    '"/>'
    "</svg>"
)


def test_initialize_declares_pagerduty_icon(monkeypatch):
    """`run` builds the server with the icon, and initialize returns it in serverInfo.icons."""
    built = []
    monkeypatch.setattr(server, "ApplicationContextStrategy", lambda: None)
    monkeypatch.setattr(server.ContextResolver, "set_strategy", lambda _strategy: None)
    monkeypatch.setattr(MCPServer, "run", lambda self, **_kwargs: built.append(self))
    server.run()

    async def initialize():
        async with Client(built[0], mode="legacy") as client:
            return client.server_info

    server_info = anyio.run(initialize)

    assert server_info.icons == [
        Icon(
            src="data:image/svg+xml;base64," + base64.b64encode(MUSTER_PAGERDUTY_SVG.encode()).decode("ascii"),
            mime_type="image/svg+xml",
            sizes=["any"],
        )
    ]
