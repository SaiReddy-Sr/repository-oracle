import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch
from main import app
from app.models.schemas import AnalyzeResponse

client = TestClient(app)

@patch("app.api.v1.endpoints.analyze_repo")
@patch("app.api.v1.endpoints.clone_repo")
@patch("app.api.v1.endpoints.extract_code")
def test_analyze_endpoint(mock_extract, mock_clone, mock_analyze_repo):
    # Setup mocks
    mock_extract.return_value = "print('hello world')"
    mock_analyze_repo.return_value = AnalyzeResponse(
        instagram_caption="🔥 OMG check out this code!! #CodeHype",
        linkedin_post="In today's fast-paced tech world, proper abstractions are key. This repository demonstrates...",
        dalle_prompt="A glowing blue brain made of digital circuitry over a dark background."
    )
    
    # Send test request
    response = client.post("/api/v1/analyze", json={"repo_url": "https://github.com/tiangolo/fastapi"})
    
    # Assert
    assert response.status_code == 200
    data = response.json()
    assert "instagram_caption" in data
    assert "linkedin_post" in data
    assert "dalle_prompt" in data
    
    # Verify our mocks were called
    mock_clone.assert_called_once()
    mock_extract.assert_called_once()
    mock_analyze_repo.assert_called_once_with("print('hello world')")
