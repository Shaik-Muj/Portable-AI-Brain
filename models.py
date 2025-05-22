from llm_clients.openai_client import OpenAIClient
from llm_clients.ollama_client import OllamaClient
from llm_clients.gemma_client import GemmaClient
from llm_clients.llama_client import LLaMaClient

MODEL_CLIENTS = {
    "openai": OpenAIClient(),
    "ollama": OllamaClient(),
    "gemma": GemmaClient(),
    "llama": LLaMaClient(),
}