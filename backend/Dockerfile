# Base image med Python
FROM python:3.11-slim

# Sett arbeidsmappe inne i containeren
WORKDIR /app

# Kopier requirements først (for caching)
COPY requirements.txt .

# Installer Python-avhengigheter
RUN pip install --no-cache-dir -r requirements.txt

# Kopier resten av koden
COPY app ./app

# Eksponer porten backend kjører på
EXPOSE 8000

# Kommando som starter backend
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]