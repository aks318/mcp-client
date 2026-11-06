
import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
import os


async def main():
    client = MultiServerMCPClient({
        "demo": {
            "transport": "stdio",
            "command": "/home/aakash/Projects/mcp-servers/fastmcp-demo-server/.venv/bin/python",
            "args": [
                "/home/aakash/Projects/mcp-servers/fastmcp-demo-server/maths.py"
            ],
        },
        "expense": {
            "transport": "http",
            "url": "https://involved-silver-firefly.fastmcp.app/mcp",
            "headers": {
                "Authorization": f"Bearer {os.environ['EXPENSE_MCP_TOKEN']}"
            }
        }
    })

    tools = await client.get_tools()

    print("\nAvailable MCP tools:")

    for tool in tools:
        print(f"- {tool.name}: {tool.description}")

    # Test the calculator's add tool
    add_tool = next((t for t in tools if t.name == "add"), None)

    if add_tool:
        result = await add_tool.ainvoke({"a": 10, "b": 20})
        print("\nAddition result:", result)


if __name__ == "__main__":
    asyncio.run(main())
