from pydantic import BaseModel, HttpUrl

class AnalyzeRequest(BaseModel):
    repo_url: HttpUrl

class AnalyzeResponse(BaseModel):
    instagram_caption: str
    linkedin_post: str
    dalle_prompt: str
