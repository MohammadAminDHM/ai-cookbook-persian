import asyncio
import nest_asyncio
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client

nest_asyncio.apply()  # Needed to run interactive python

"""
Make sure:
1. The server is running before running this script.
2. The server is configured to use streamable-http transport.
3. The server is listening on port 8050.

To run the server:
uv run server.py
"""


async def main():
    # Connect to the server using Streamable HTTP
    async with streamablehttp_client("http://localhost:8050/mcp") as (
        read_stream,
        write_stream,
        get_session_id,
    ):
        async with ClientSession(read_stream, write_stream) as session:
            # Initialize the connection
            await session.initialize()

            # List available tools
            tools_result = await session.list_tools()
            print("Available tools:")
            for tool in tools_result.tools:
                print(f"  - {tool.name}: {tool.description}")

            # Call our calculator tool
            result = await session.call_tool("add", arguments={"a": 2, "b": 3})
            print(f"2 + 3 = {result.content[0].text}")


if __name__ == "__main__":
    asyncio.run(main())
