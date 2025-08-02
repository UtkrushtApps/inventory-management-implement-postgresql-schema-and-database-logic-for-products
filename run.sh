#!/bin/bash
set -e

docker-compose down -v || true
docker-compose build
echo "Starting database container..."
docker-compose up -d db
sleep 8
echo "Initializing database schema..."
docker cp schema.sql $(docker-compose ps -q db):/docker-entrypoint-initdb.d/schema.sql
# schema.sql is picked up and run automatically by Postgres

echo "Starting FastAPI service..."
docker-compose up -d api
echo "API running at http://localhost:8000/docs"
