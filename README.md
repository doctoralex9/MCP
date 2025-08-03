# MCP Personal Assistant – Claude Desktop Integration

This project provides a custom [MCP](https://github.com/microsoft/mcp) server for use with the Claude Desktop client.

## Features

- Sentiment analysis tool
- Downloads folder organizer
- Personalized greeting resource
- FastAPI + FastMCP integration

## Quick Start

1. **Clone this repository**  
   ```sh
   git clone https://github.com/yourusername/MCP-main.git
   cd MCP-main
   ```

2. **Install dependencies**  
   ```sh
   pip install -r requirements.txt
   ```

3. **Configure Claude Desktop**  
   Edit (or create)  
   `C:\Users\<YourUser>\AppData\Roaming\Claude\claude_desktop_config.json`  
   and add:
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
           "c:\\Users\\<YourUser>\\Desktop\\MCP-main\\src\\main.py"
         ],
         "url": "http://localhost:8000/mcp"
       }
     }
   }
   ```
   Replace `<YourUser>` with your Windows username.

4. **Start Claude Desktop**  
   Launch the Claude Desktop app.  
   The MCP server will start automatically and be available at `/mcp`.

## Usage

- Access the MCP tools and resources from within Claude Desktop.
- Customize or extend the server by editing `src/main.py`.

---
