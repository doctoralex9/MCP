# server.py
from mcp.server.fastmcp import FastMCP
from textblob import TextBlob
from pathlib import Path
import shutil
from fastapi import FastAPI

# Create an MCP server
mcp = FastMCP("Personal_assistant")


app = FastAPI()
app.mount("/mcp", mcp )#Mount mcp object on the main app by using mount() method 

@app.get("/")
async def read_root():
    return {"message": "Welcome to MCP Personal Assistant Core! Access FastMCP at /mcp"}


@mcp.tool()
def analyze_your_mood(user_text: str)-> str:
    """
    Analyzes the user's mood from text and returns a supportive response.
    Example input: "I'm feeling really stressed about work today."
    """
    analysis = TextBlob(user_text)
    mood = analysis.sentiment.polarity

     # Mood classification + suggestions

    if mood < -0.5:
        return (
            "I hear you’re having a tough time. 💙\n"
            "Try taking a short walk or breathing deeply for 2 minutes.\n"
            "Remember: This feeling is temporary."
            )
    elif mood < 0:
        return (
            "It sounds like you’re feeling down. 🌧️\n"
            "How about listening to your favorite song or calling a friend?"
        )
    else:
        return (
            "Glad you’re doing okay! 🌞\n"
            "Keep up the positive energy—maybe celebrate with a small treat!"
        )

@mcp.tool()
def organize_downloads(
    base_path: str = "~/Downloads",  # Default path (supports ~)
    create_folders: bool = True,     # Auto-create category folders
    dry_run: bool = False            # Test without moving files
) -> str:
    """
    Organizes files in the Downloads folder by category (Images, Documents, etc.).
    Returns a summary of changes.
    """
    # Expand user path (~ -> /home/user)
    downloads_path = Path(base_path).expanduser()
    
    # File type categories
    categories = {
        "Images": [".jpg", ".png", ".gif", ".webp"],
        "Documents": [".pdf", ".docx", ".txt", ".md"],
        "Archives": [".zip", ".rar", ".tar.gz"],
        "Executables": [".exe", ".msi", ".deb"],
        "Videos": [".mp4", ".mov", ".avi"]
    }

    moved_files = {}
    ignored_files = []

    for item in downloads_path.iterdir():
        if item.is_file():
            file_ext = item.suffix.lower()
            moved = False

            # Find matching category
            for category, extensions in categories.items():
                if file_ext in extensions:
                    if create_folders:
                        (downloads_path / category).mkdir(exist_ok=True)
                    
                    dest = downloads_path / category / item.name
                    
                    if not dry_run:
                        shutil.move(str(item), str(dest))
                    
                    moved_files.setdefault(category, []).append(item.name)
                    moved = True
                    break

            if not moved:
                ignored_files.append(item.name)

    # Generate report
    report = [
        f"Organized {sum(len(v) for v in moved_files.values())} files:",
        *[f"- {cat}: {len(files)}" for cat, files in moved_files.items()],
        f"Ignored {len(ignored_files)} unsupported files" if ignored_files else ""
    ]
    
    return "\n".join(report)    
       

# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"