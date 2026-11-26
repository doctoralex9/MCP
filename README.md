# MCP Personal Assistant – Claude Desktop Integration

This project provides a custom [MCP](https://modelcontextprotocol.io) server for use with the Claude Desktop client.

## Features

- Downloads folder organizer: sorts files into Images, Documents, Archives, Executables and Videos folders, with a dry-run mode
- Mood analysis: an early experiment while I was learning MCP

## Quick Start

1. **Clone this repository**  
   ```sh
   git clone https://github.com/doctoralex9/MCP.git
   cd MCP
   ```

2. **Install dependencies**  
   ```sh
   pip install -r requirements.txt
   ```

3. **Configure Claude Desktop**  
   In the Claude Desktop app, click the menu icon (☰) in the top-left corner. Navigate to File > Settings, then select Edit Config to open the claude_desktop_config.json file. Add the following configuration:
   ```json
   {
     "mcpServers": {
       "Personal_assistant": {
         "command": "uv",
         "args": [
           "run",
           "--with",
           "mcp[cli]",
           "mcp",
           "run",
           "c:\\Users\\<YourUser>\\Desktop\\MCP\\src\\main.py"
         ]
       }
     }
   }
   ```
   Replace the path with the full path to `src\main.py` in the folder you cloned.

4. **Start Claude Desktop**  
   Launch the Claude Desktop app.  
   Click the Tools button to see your new tools available for use.

## Usage

Interact with your new tools directly within the Claude interface. For example, you can ask Claude to organize your Downloads folder (try a dry run first) or to analyze your mood.

## Docker (unfinished experiment)

The `Dockerfile` and the FastAPI wrapper in `src/main.py` were an attempt to run the server in a container over HTTP. I never finished it, so it doesn't work yet. Use the Quick Start above instead. Two things are still missing:

- **The container can't see your files.** The organizer needs your Downloads folder, so the folder would have to be mounted as a volume (for example `-v C:\Users\<YourUser>\Downloads:/data`) and its path passed in through an environment variable.
- **The HTTP wrapper isn't wired correctly.** `src/main.py` mounts the `FastMCP` object directly on FastAPI, but that object isn't a web app, so requests to `/mcp` fail. It would need to mount `mcp.streamable_http_app()` and start `mcp.session_manager` in FastAPI's lifespan.

Because the main tool works on files on your own computer, running it directly on your machine, as in the Quick Start, is the simpler setup.

---
