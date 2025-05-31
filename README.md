# Gepeto AI Development Environment Setup

This document provides a step-by-step guide to setting up the development environment for the Gepeto AI project. Follow the instructions below to ensure a smooth setup process.

## Building and Running the Container

1. **Build the Container**: Use the following command to build the container:
   ```bash
   podman build -t gepeto-ai .
   ```

2. **Run the Container**: Use the following command to run the container:
   ```bash
   podman run -d -p 8999:8999 --name gepeto-ai-container gepeto-ai
   # Or for development: 
    podman run -d --replace -p 8999:8999 --name gepeto-ai-container -v $(pwd):/app gepeto-ai

   ```

3. **Check Container Status**: Verify the container is running:
   ```bash
   podman ps
   ```

4. **View Container Logs**: Check the application logs:
   ```bash
   podman logs gepeto-ai-container
   ```

5. **Test the API Endpoints**: Use the following `curl` commands to test the endpoints:
   
   **Root endpoint:**
   ```bash
   curl http://127.0.0.1:8999/
   ```
   Expected response: `{"message": "Gepeto AI API is running"}`
   
   **Health endpoint:**
   ```bash
   curl http://127.0.0.1:8999/health
   ```
   Expected response: `{"message": "I'm healthy"}`

6. **Stop and Remove Container** (when needed):
   ```bash
   podman stop gepeto-ai-container
   podman rm gepeto-ai-container
   ```

## Troubleshooting

- **If `localhost` doesn't work**: Use `127.0.0.1` instead due to IPv6/IPv4 resolution issues
- **Force IPv4 with curl**: `curl -4 http://localhost:8999/health`
- **Check port mapping**: `podman port gepeto-ai-container`

This guide will be updated as the development process progresses.

## after you setup you llamastack server 

curl -X POST http://127.0.0.1:8999/basic_completion   -H "Content-Type: application/json"   -d '{"message": "Hello, how are you?"}'