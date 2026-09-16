FROM python:3.12-slim

# Install Node.js and npm
RUN apt-get update && \
    apt-get install -y nodejs npm && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Node dependencies
COPY backend/package.json backend/
WORKDIR /app/backend
RUN npm install

# Copy complete project
WORKDIR /app
COPY . .

# Make start script executable
RUN chmod +x start.sh

# Streamlit public port
EXPOSE 8501

CMD ["./start.sh"]
