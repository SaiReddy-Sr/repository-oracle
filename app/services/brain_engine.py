import os
import json
import google.generativeai as genai
from app.models.schemas import AnalyzeResponse

def analyze_repo(codebase_text: str) -> AnalyzeResponse:
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])
    
    # We will use Gemini 1.5 Pro to process the potentially large codebase
    model = genai.GenerativeModel('gemini-1.5-pro')
    
    prompt = f"""
You are an expert AI Architect and technical marketer. Look at the following codebase text and generate three things:
1. An Instagram "Hype" Caption (emoji-heavy, exciting, summarizing what the project does).
2. A LinkedIn "Insight" Post (focus on the design patterns, architecture, and value proposition).
3. A DALL-E 3 prompt for "Abstract Technical Surrealism" that captures the essence of this project.

Return purely a JSON response containing exactly these keys: "instagram_caption", "linkedin_post", "dalle_prompt". Do not wrap the JSON in Markdown backticks.

Codebase Data:
{codebase_text[:100000]} # Limiting context slightly to avoid hitting massive token limits, but 1.5 Pro handles a lot.
"""
    
    # Use GenerationConfig for JSON format if supported, or just prompt for strict JSON.
    response = model.generate_content(
        prompt,
        generation_config={"response_mime_type": "application/json"}
    )
    
    try:
        data = json.loads(response.text)
        return AnalyzeResponse(**data)
    except Exception as e:
        raise ValueError(f"Failed to parse Gemini response: {e}. Raw Text: {response.text}")
