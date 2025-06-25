# server.py
from mcp.server.fastmcp import FastMCP
from textblob import TextBlob

# Create an MCP server
mcp = FastMCP("Demo")


# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.tool()
def analyze_your_mood(user_text: str)-> str:
    """
    Analyzes the user's mood from text and returns a supportive response.
    Example input: "I'm feeling really stressed about work today."
    """
    analysis = TextBlob(user_text)
    mood = analysis.sentiment.polarity

     # Mood classification + suggestions

    if mood < -0.25:
        return("Just chill a little bit")
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
    
       

# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"