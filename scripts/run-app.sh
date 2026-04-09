#!/bin/bash

set -e

echo "Stopping and removing old containers..."
docker compose down --remove-orphans

echo "Building and starting application..."
docker compose up --build