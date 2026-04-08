# Weather App

A learning project to understand how frontend, backend, API, Docker, Kubernetes, and Git work together.

## Overview

This project consists of two parts:

- **Backend**: Python API built with FastAPI
- **Frontend**: Simple HTML, CSS, and JavaScript application

The frontend communicates with the backend via HTTP requests (API).

---

## Project Structure

weather-app/
backend/
app/
main.py
requirements.txt
frontend/
index.html
script.js
styles.css
README.md

---

## Requirements

- Python 3.10+
- macOS (tested on MacBook Pro M3)
- Git

---

## How to Run the Backend

cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload

Backend will be available at:

http://127.0.0.1:8000

Test endpoints:

Health check: http://127.0.0.1:8000/health
API docs: http://127.0.0.1:8000/docs

How to run frontend:

cd frontend
python3 -m http.server 5500

Then open in browser:

http://127.0.0.1:5500
