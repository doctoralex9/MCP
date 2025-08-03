# MCP Personal Assistant – Claude Desktop Integration

This project provides a custom [MCP](https://github.com/microsoft/mcp) server for use with the Claude Desktop client.

## Features

- Sentiment analysis tool
- Downloads folder organizer

## Quick Start

1. **Clone this repository**  
   ```sh
   git clone https://github.com/yourusername/MCP.git
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
         ],
         "url": "http://localhost:8000/mcp"
       }
     }
   }
   ```
   Replace `<YourUser>` with your Windows username.

4. **Start Claude Desktop**  
   Launch the Claude Desktop app.  
   Click the Tools button to see your new tools available for use.
## Usage

Interact with your new tools directly within the Claude interface. For example, you can ask Claude to use the sentiment analyzer or the folder organizer.

---
