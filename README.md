# Simple FastAPI demo

This repository contains a minimal FastAPI application with GET and POST endpoints and a few tests.

How to run locally

1. Create a virtual environment and install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Start the server with uvicorn:

```bash
uvicorn main:app --reload
```

3. Run tests:

```bash
pytest -q
```

API endpoints

- GET / -> health
- GET /items/{item_id} -> returns a demo item (404 if id <= 0)
- POST /items -> creates an item and returns it with a generated id

