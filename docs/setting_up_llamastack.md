# Getting Started with Llama-Stack Server

## ✅ Setup and Run Ollama

- Verify models available:
  ```sh
  ollama list
  ```

- (Optional) Pull a specific model:
  ```sh
  ollama pull llama3.2:3b-instruct-fp16
  ```

- Run the model with keepalive:
  ```sh
  ollama run llama3.2:3b-instruct-fp16 --keepalive 60m
  ```

---

## ✅ Configure Environment Variables

```sh
export LLAMA_STACK_MODEL="meta-llama/Llama-3.2-3B-Instruct"
export LLAMA_STACK_PORT=8321
export LLAMA_STACK_SERVER=http://localhost:$LLAMA_STACK_PORT
export LLAMA_SERVER_CONTAINER_IMAGE="docker.io/llamastack/distribution-ollama:0.2.5"
export CONTAINER_NAME="llamastack-ollama"
export OLLAMA_PORT=11434
```

---

## ✅ Launch Llama-Stack Server

- Run the container:
  ```sh
  podman run -d \
    --name $CONTAINER_NAME \
    --network=host \
    $LLAMA_SERVER_CONTAINER_IMAGE \
    --port $LLAMA_STACK_PORT \
    --env INFERENCE_MODEL="$LLAMA_STACK_MODEL" \
    --env OLLAMA_URL=http://localhost:$OLLAMA_PORT
  ```

- Monitor the logs:
  ```sh
  podman logs -f $CONTAINER_NAME
  ```

---

## ✅ (Optional) CLI Client Usage

- Install CLI client:
  ```sh
  source ~/venv/bin/activate
  pip install --upgrade pip
  pip install llama-stack-client==0.2.5
  ```

- Configure CLI endpoint:
  ```sh
  llama-stack-client configure --endpoint $LLAMA_STACK_SERVER
  ```

- List available models:
  ```sh
  llama-stack-client models list
  ```

- Run a test prompt:
  ```sh
  llama-stack-client \
    inference chat-completion \
    --message "Write me a small poem why llamas are better than bees without knees"
  ```

---

## ✅ (Optional) API Requests with `curl`

- Chat completion via API:
  ```sh
  curl -sS $LLAMA_STACK_SERVER/v1/inference/chat-completion \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $API_KEY" \
    -d "{
      \"model_id\": \"$LLAMA_STACK_MODEL\",
      \"messages\": [{\"role\": \"user\", \"content\": \"Write me a small poem why llamas are better than bees without knees?\"}],
      \"temperature\": 0.0
    }" | jq -r '.completion_message | select(.role == "assistant") | .content'
  ```

- List model identifiers:
  ```sh
  curl -sS $LLAMA_STACK_SERVER/v1/models -H "Content-Type: application/json" | jq -r '.data[].identifier'
  ```

---

## 🎉 You're All Set

Llama-Stack Server is running locally and ready to use via CLI, API, or your own code.

