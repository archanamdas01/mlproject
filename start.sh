#!/bin/bash

echo "Starting Node.js backend..."

cd /app/backend
node server.js &

echo "Starting Streamlit frontend..."

cd /app
streamlit run frontend/app.py \
    --server.address=0.0.0.0 \
    --server.port=8501
