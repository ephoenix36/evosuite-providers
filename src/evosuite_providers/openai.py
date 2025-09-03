"""OpenAI provider implementation."""

import os
from typing import Any, Dict, Optional
from evosuite.plugins import Provider, PluginMetadata


class OpenAIProvider(Provider):
    """Provider for OpenAI LLM services."""
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        super().__init__(config)
        self.api_key = self.config.get("api_key") or os.getenv("OPENAI_API_KEY")
        self.model = self.config.get("model", "gpt-3.5-turbo")
        self.base_url = self.config.get("base_url", "https://api.openai.com/v1")
        self._client = None
    
    @property
    def metadata(self) -> PluginMetadata:
        return PluginMetadata(
            name="openai_provider",
            version="0.2.0",
            description="OpenAI LLM provider for text generation",
            author="EvoSuite Team", 
            provides=["provider.openai", "provider.llm"],
            requires_core=">=0.2,<0.3",
            config_schema={
                "type": "object",
                "properties": {
                    "api_key": {"type": "string", "description": "OpenAI API key"},
                    "model": {"type": "string", "default": "gpt-3.5-turbo"},
                    "base_url": {"type": "string", "default": "https://api.openai.com/v1"},
                    "max_tokens": {"type": "integer", "default": 1000},
                    "temperature": {"type": "number", "default": 0.7}
                },
                "required": ["api_key"]
            }
        )
    
    async def validate_config(self) -> bool:
        """Validate OpenAI configuration."""
        if not self.api_key:
            return False
        
        # Test basic API connectivity (mock for now)
        try:
            # In real implementation: make test API call
            return len(self.api_key) > 10  # Basic validation
        except Exception:
            return False
    
    async def generate(self, prompt: str, context: Dict[str, Any]) -> str:
        """Generate response using OpenAI API."""
        if not await self.validate_config():
            raise ValueError("Invalid OpenAI configuration")
        
        # Mock implementation - in real version, use openai client
        max_tokens = self.config.get("max_tokens", 1000)
        temperature = self.config.get("temperature", 0.7)
        
        # Simulate API call result
        return f"[OpenAI {self.model}] Generated response for prompt: {prompt[:50]}..."
    
    async def activate(self, context: Dict[str, Any]) -> None:
        """Initialize OpenAI client on activation."""
        try:
            # In real implementation:
            # import openai
            # self._client = openai.AsyncOpenAI(api_key=self.api_key, base_url=self.base_url)
            pass
        except ImportError:
            raise RuntimeError("OpenAI package not installed. Run: pip install openai")
    
    async def deactivate(self, context: Dict[str, Any]) -> None:
        """Clean up resources on deactivation."""
        if self._client:
            # Close client connections if needed
            self._client = None