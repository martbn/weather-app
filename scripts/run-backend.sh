#!/bin/bash

echo "Building Docker image..."
docker build -t weather-backend ./backend

echo "Stopping existing container (if any)..."
docker stop weather-backend-container 2>/dev/null
docker rm weather-backend-container 2>/dev/null

echo "Starting backend container..."
docker run -p 8000:8000 --name weather-backend-container weather-backend