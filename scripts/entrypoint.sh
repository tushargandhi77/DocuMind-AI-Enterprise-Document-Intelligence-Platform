#!/bin/sh

echo "Starting Enterprise Document Intelligence System..."

if [ "$PRODUCTION" = "true" ]; then
    echo "Running in PRODUCTION mode"
    
    exec uvicorn app.main:app \
        --host 0.0.0.0 \
        --port 8000 \
        --workers 4 \
        --proxy-headers \
        --forwarded-allow-ips="*"

else
    echo "Running in DEVELOPMENT mode"

    exec uvicorn app.main:app \
        --host 0.0.0.0 \
        --port 8000 \
        --reload
fi
