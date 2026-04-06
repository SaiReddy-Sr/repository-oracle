import os
import uuid
from fastapi import APIRouter, BackgroundTasks, HTTPException
from app.models.schemas import AnalyzeRequest, AnalyzeResponse
from app.services.git_engine import clone_repo, extract_code, delete_temp_dir
from app.services.brain_engine import analyze_repo

router = APIRouter()

@router.post("/analyze", response_model=AnalyzeResponse)
async def analyze_repository(request: AnalyzeRequest, background_tasks: BackgroundTasks):
    repo_url = str(request.repo_url)
    
    # Generate a unique temp directory for this request
    temp_dir = os.path.join(os.getcwd(), "temp", str(uuid.uuid4()))
    
    try:
        # Clone the repo
        clone_repo(repo_url, temp_dir)
        
        # Extract the code
        codebase_text = extract_code(temp_dir)
        
        if not codebase_text.strip():
            raise HTTPException(status_code=400, detail="No source code found in repository (.py, .js, .go, .md)")
            
        # Analyze with Gemini
        response = analyze_repo(codebase_text)
        
        return response
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        # Schedule the temp directory for deletion after response is sent
        background_tasks.add_task(delete_temp_dir, temp_dir)
