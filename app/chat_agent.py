import logging
import os
from dotenv import load_dotenv

logger = logging.getLogger(__name__)
load_dotenv()
# Get the LlamaStack server URL from environment variables
LLAMASTACK_SERVER_URL = os.getenv('LLAMASTACK_SERVER_URL')
LLAMA_STACK_MODEL = os.getenv('LLAMA_STACK_MODEL')

print(f"LlamaStack Server URL: {LLAMASTACK_SERVER_URL}")

# Global client variable
client = None

def define_client(base_url):
    """
    Defines a client for llamastack.
    
    Returns:
        Dictionary representing a placeholder client
    """
    logger.info(f"Creating client, {base_url}")
    from llama_stack_client import LlamaStackClient
    defined_client = LlamaStackClient(base_url=base_url,)    

    return defined_client

def basic_completion(payload):
    """
    Placeholder function for basic chat completion.
    
    Args:
        payload: Dictionary containing the request data
        
    Returns:
        Dictionary with the response
    """
    global client
    
    logger.info(f"Processing completion request: {payload}")
    
    # Test if client is not defined, call create_placeholder_client
    if client is None:
        logger.warning("Client is not defined, creating placeholder client")
        client = define_client(LLAMASTACK_SERVER_URL)
    
    response = client.inference.chat_completion(
    model_id=LLAMA_STACK_MODEL,
    messages=[
        {"role": "system", "content": "You're a helpful assistant."},
        {
            "role": "user",
            "content": payload["message"] ,
        },
    ],
)
    print(response.completion_message.content)

    # # Placeholder implementation
    # message = payload.get("message", "")
    # response = f"Echo: {message} (This is a placeholder response using {client['type']} client)"
    
    return {
        "response": response.completion_message.content,
        "status": "success",
        # "client_info": {
        #     "client_type": client.get("type", "unknown"),
        #     "server_url": client.get("server_url", "unknown")
        # }
    }