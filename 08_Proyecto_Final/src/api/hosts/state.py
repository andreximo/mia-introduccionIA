
from dataclasses import dataclass, field
from typing import Any
 
from mcp import ClientSession
 
 
@dataclass
class AppState:
    mcp_sessions: dict[str, ClientSession] = field(default_factory=dict)
    tool_to_session: dict[str, ClientSession] = field(default_factory=dict)
    tools_catalog: list[dict[str, Any]] = field(default_factory=list)
 