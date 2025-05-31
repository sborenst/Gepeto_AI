# Gepeto AI Development Environment Setup

This document provides a step-by-step guide to setting up the development environment for the Gepeto AI project. Follow the instructions below to ensure a smooth setup process.

## Container Setup

1. **Install Podman/Docker**: Ensure Podman/Docker is installed on your local machine. Podman is used for containerization, allowing you to create and manage containers without requiring a daemon.

2. **Create a Podman Container**:
   - **Step 1**: Navigate to the project directory:
     ```bash
     cd /path/to/Gepeto_AI
     ```
   - **Step 2**: Build the container image using the `Containerfile`:
     ```bash
     podman build -t gepeto-ai .
     ```
   - **Step 3**: Run the container, mapping the necessary ports:
     ```bash
     podman run -d -p 8999:8999 --name gepeto-ai-container gepeto-ai
     # Or, for development mode:
     podman run -d -p 8999:8999 --name gepeto-ai-container -v $(pwd):/app gepeto-ai
     ```
   - **Step 4**: Verify the container is running:
     ```bash
     podman ps
     ```

3. **Configure Code Watching**: Use `watchmedo` or `uvicorn --reload` to automatically reload the application when code changes are detected. This enhances the development workflow by providing immediate feedback on code changes.

## Configuration Management

1. **Create a `.env` File**: Store environment-specific variables in a `.env` file. This file should contain all necessary configuration settings for the application.

2. **Install `python-dotenv`**: Use `python-dotenv` to load environment variables from the `.env` file into your application. This ensures that configuration settings are easily accessible within the code.

3. **Choose a Secrets Management Tool**: Research and select a tool for managing secrets, such as HashiCorp Vault or AWS Secrets Manager. This tool will securely store API keys and passwords.

## Security Enhancements

1. **API Key Authentication**: Implement API key authentication in FastAPI to secure the application. This involves creating middleware to check for valid API keys in incoming requests.

2. **Create a `.gitignore` File**: Add entries to a `.gitignore` file to prevent sensitive files and directories from being tracked by version control. This includes the `.env` file, cache directories, and compiled Python files.

## Testing and Documentation

1. **Write Unit Tests**: Use `pytest` to write unit tests for the application. This ensures that individual components function as expected.

2. **Write Integration Tests**: Develop integration tests for API endpoints to verify that different parts of the application work together correctly.

3. **Document the Architecture and Code**: Provide comprehensive documentation of the application's architecture and codebase. This includes user guides and API documentation.

## Iteration and Feedback

1. **Test and Iterate**: Continuously test each component and iterate based on the results. This involves gathering feedback and making necessary adjustments to improve the application.

2. **Gather Feedback**: Collect feedback from testing and documentation reviews to identify areas for improvement.

## Building and Running the Container

1. **Build the Container**: Use the following command to build the container:
   ```bash
   podman build -t gepeto-ai .
   ```

2. **Run the Container**: Use the following command to run the container:
   ```bash
   podman run -d -p 8999:8999 --name gepeto-ai-container gepeto-ai
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