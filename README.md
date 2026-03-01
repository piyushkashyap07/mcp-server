# MCP Server Calculator

## Setup Instructions

These are the commands run to set up this project initially:

```bash
uv init mcp-server-calculator
cd mcp-server-calculator
uv venv
uv add "mcp[cli]"
# Created main.py file
uv run main.py
```

## Step-by-Step Guide

### Start your MCP server
Unlike the stdio transport, where the inspector launches the server process, for streamable-http, the server must be running independently. Open a terminal and run your Python script:

```bash
python main.py
```

You will see output indicating the server is running on a specific address and port, generally `http://127.0.0.1:8000` with the MCP endpoint at `http://127.0.0.1:8000/mcp`.

### Launch the MCP Inspector
Open a separate terminal window and launch the MCP Inspector using npx:

```bash
npx @modelcontextprotocol/inspector
```

This command will typically open the Inspector UI in your web browser, often at `http://localhost:6274`.

### Configure the Inspector UI
In the MCP Inspector's web interface:
1. Set the Transport Type to **Streamable HTTP**.
2. Enter your server's URL (e.g., `http://localhost:8000/mcp`) in the designated field.

### Connect and Test
1. Click the "Connect" button to establish the connection. The status should change to Connected.
2. Once connected, you can interact with your server by clicking the "Tools" button and selecting "List tools" to see the available functions. You can then select a specific tool, fill in the required parameters, and run it to test the output.
