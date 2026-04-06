# 🧠 The Repository Oracle

> **An Agentic AI Content Engine that transforms raw source code into high-signal social media insights using Gemini 2.5 Flash.**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google%20Gemini-8E75B2?style=for-the-badge&logo=googlegemini&logoColor=white)

The Repository Oracle is a streamlined, agentic application that clones public codebases and distills their architecture, patterns, and logic into ready-to-post social media gold. 

## 🗺️ Visual Architecture

```mermaid
graph LR
    A[User URL Input] -->|POST /analyze| B(GitPython Clone & Filter)
    B -->|Filtered Code Context| C{Gemini 2.5 Flash Analysis}
    C -->|Extract Insights| D[Pydantic Validation]
    D -->|Strict JSON Model| E[Social Output Response]
    
    style A fill:#009688,stroke:#fff,stroke-width:2px,color:#fff
    style B fill:#F05032,stroke:#fff,stroke-width:2px,color:#fff
    style C fill:#8E75B2,stroke:#fff,stroke-width:2px,color:#fff
    style D fill:#3776AB,stroke:#fff,stroke-width:2px,color:#fff
    style E fill:#009688,stroke:#000,stroke-width:2px,color:#fff
```

## ✨ Core Features

- **⚡ Async Execution**: Powered by FastAPI background tasks to effortlessly handle repository lifecycle management and filesystem cleanup post-computation.
- **🔍 Intelligent Context Filtering**: Recursively clones the target repository and heavily filters out noise, keeping only high-impact application code (`.py`, `.js`, `.go`, `.md`).
- **📱 Multi-Platform Content**: Instantly generates:
  - 📸 High-hype Instagram Captions
  - 💼 Deep-dive LinkedIn Insights focused on Architecture
  - 🎨 DALL-E 3 Creative Prompts to visualize the codebase

## 🚀 Quick Start

Get up and running locally in under a minute.

1. **Clone the repository**
   ```bash
   git clone https://github.com/SaiReddy-Sr/repository-oracle.git
   cd repository-oracle
   ```

2. **Initialize your Environment**
   ```bash
   pip install -r requirements.txt
   cp .env.example .env
   # Open .env and add your GEMINI_API_KEY
   ```

3. **Ignite the Server**
   ```bash
   uvicorn main:app --reload
   ```
   Head over to `http://localhost:8000/docs` to test the API directly from the Swagger UI!
