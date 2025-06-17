import os
from dotenv import load_dotenv 

load_dotenv()
def get_prompt(file):
    with open(f"prompts/{file}", encoding="utf-8") as f:
        return f.read()
    
openrouter_key = os.getenv("OPENROUTER_API_KEY")

if not openrouter_key:
    raise ValueError("OPENROUTER_API_KEY is not set")

# ✅ LiteLLM uses this internally
os.environ["OPENROUTER_API_KEY"] = openrouter_key