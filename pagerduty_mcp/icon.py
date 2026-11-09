"""The MCP server's icon (serverInfo.icons): the PagerDuty mark.

pagerduty.svg is the PagerDuty mark from simple-icons 16.36.0 (icons/pagerduty.svg,
CC0 1.0, https://simpleicons.org), drawn white on a rounded square in the brand
colour #06AC38: the same SVG giantswarm/muster builds for PagerDuty in
internal/servericon/brands.go, so the connector shows the same icon whatever URL
it is reached on. The file ends in a newline, which the icon leaves out.
"""

import base64
from importlib.resources import files

from mcp.types import Icon

_SVG = files(__package__).joinpath("pagerduty.svg").read_bytes().rstrip(b"\n")

SERVER_ICON = Icon(
    src="data:image/svg+xml;base64," + base64.b64encode(_SVG).decode("ascii"),
    mime_type="image/svg+xml",
    sizes=["any"],
)
