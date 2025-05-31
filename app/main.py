from fastapi import FastAPI, Request
import logging
import os
from dotenv import load_dotenv
from app.chat_agent import basic_completion

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/")
async def root():
    logger.info("Root endpoint accessed")
    return {"message": "Gepeto AI API is running"}

@app.get("/health")
async def health_check():
    logger.info("Health check endpoint accessed")
    return {"message": "I'm healthy"}

@app.post("/basic_completion")
async def basic_completion_endpoint(request: Request):
    logger.info("Basic completion endpoint accessed")
    
    # Get the JSON payload from the request
    payload = await request.json()
    
    # Call the chat agent function
    result = basic_completion(payload)
    
    return result