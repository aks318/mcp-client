import asyncio
from fastmcp import Client
from fastmcp.client.auth import OAuth


async def main():
    oauth = OAuth(
        additional_client_metadata={
            "token_endpoint_auth_method": "none"
        }
    )

    async with Client(
        "https://involved-silver-firefly.fastmcp.app/mcp",
        auth=oauth
    ) as client:

        tools = await client.list_tools()

        print("\nConnected successfully!")

        for tool in tools:
            print(f"- {tool.name}: {tool.description}")


if __name__ == "__main__":
    asyncio.run(main())