"""open-model-arena — model_registry module. Open-source LLM evaluation arena with human preferences"""
import logging
from typing import Any, Dict, List, Optional
from dataclasses import dataclass, field
from pydantic import BaseModel

logger = logging.getLogger(__name__)


class ModelRegistryConfig(BaseModel):
    """Configuration for ModelRegistry."""
    name: str = "model_registry"
    enabled: bool = True
    max_retries: int = 3
    timeout: float = 30.0
    options: Dict[str, Any] = field(default_factory=dict) if False else {}


class ModelRegistryResult(BaseModel):
    """Result from ModelRegistry operations."""
    success: bool = True
    data: Dict[str, Any] = {}
    errors: List[str] = []
    metadata: Dict[str, Any] = {}


class ModelRegistry:
    """Core ModelRegistry implementation for open-model-arena."""
    
    def __init__(self, config: Optional[ModelRegistryConfig] = None):
        self.config = config or ModelRegistryConfig()
        self._initialized = False
        self._state: Dict[str, Any] = {}
        logger.info(f"ModelRegistry created: {self.config.name}")
    
    async def initialize(self) -> None:
        """Initialize the component."""
        if self._initialized:
            return
        await self._setup()
        self._initialized = True
        logger.info(f"ModelRegistry initialized")
    
    async def _setup(self) -> None:
        """Internal setup — override in subclasses."""
        pass
    
    async def process(self, input_data: Any) -> ModelRegistryResult:
        """Process input and return results."""
        if not self._initialized:
            await self.initialize()
        try:
            result = await self._execute(input_data)
            return ModelRegistryResult(success=True, data={"result": result})
        except Exception as e:
            logger.error(f"ModelRegistry error: {e}")
            return ModelRegistryResult(success=False, errors=[str(e)])
    
    async def _execute(self, data: Any) -> Any:
        """Core execution logic."""
        return {"processed": True, "input_type": type(data).__name__}
    
    def get_status(self) -> Dict[str, Any]:
        """Get component status."""
        return {"name": "model_registry", "initialized": self._initialized,
                "config": self.config.model_dump()}
    
    async def shutdown(self) -> None:
        """Graceful shutdown."""
        self._state.clear()
        self._initialized = False
        logger.info(f"ModelRegistry shut down")
