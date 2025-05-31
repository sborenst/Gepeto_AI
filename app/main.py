from fastapi import FastAPI
import logging

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