# MISSION: Build 'The Repository Oracle'
Role: Senior AI Architect & FastAPI Expert.

## Technical Stack
- Framework: FastAPI (Async)
- Engine: GitPython, Google Gemini 1.5 Pro
- Validation: Pydantic v2
- CI/CD: GitHub Actions (Linting + Testing)

## Workspace Structure
- /app/api/v1/          <-- Route definitions
- /app/services/        <-- Logic for Git cloning & Gemini calls
- /app/models/          <-- Pydantic schemas
- /tests/               <-- Pytest suite

## Agent Instructions
1. **Scaffold**: Create the directory structure above.
2. **Environment**: Install `fastapi`, `uvicorn`, `GitPython`, `google-generativeai`, and `pydantic`.
3. **The Git Engine**: In `services/git_engine.py`, implement a function to clone a repo to a `temp/` folder with `--depth 1`. Filter for `.py`, `.js`, `.go`, `.md`. 
4. **The Gemini Engine**: In `services/brain_engine.py`, create a prompt that generates:
   - Instagram "Hype" Caption (Emoji-heavy).
   - LinkedIn "Insight" Post (Focus on Design Patterns).
   - DALL-E 3 "Abstract Technical Surrealism" prompt.
5. **Safety**: Use FastAPI `BackgroundTasks` to delete the `temp/` directory after the JSON response is returned.
6. **Validation**: Run `uvicorn` and test the `/analyze` endpoint with a sample public GitHub URL. Show me the successful JSON response as an **Artifact**.