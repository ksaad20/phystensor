
import logging
import json
import sys
from datetime import datetime
from typing import Any, Dict

class IndustrialFormatter(logging.Formatter):
    """
    Formats logs into JSON for easy ingestion by ELK stacks, 
    Datadog, or cloud-native logging services.
    """
    def format(self, record: logging.LogRecord) -> str:
        log_entry: Dict[str, Any] = {
            "timestamp": datetime.fromtimestamp(record.created).isoformat(),
            "level": record.levelname,
            "module": record.module,
            "message": record.getMessage(),
        }
        
        # Capture dimensional metadata if provided in the 'extra' kwarg
        if hasattr(record, "dimensions"):
            log_entry["dimensions"] = record.dimensions
        
        if record.exc_info:
            log_entry["exception"] = self.formatException(record.exc_info)
            
        return json.dumps(log_entry)

def setup_logger(name: str = "phystensor", level: int = logging.INFO) -> logging.Logger:
    """
    Initializes a logger that outputs structured JSON to stdout.
    This follows 'Twelve-Factor App' principles for cloud scalability.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    # Avoid duplicate handlers if setup is called multiple times
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(IndustrialFormatter())
        logger.addHandler(handler)
        
    return logger

# Global singleton for the library
logger = setup_logger()

def log_dimension_error(error: Exception, dim_a: Any = None, dim_b: Any = None):
    """
    A specialized helper to log physical contradictions with 
    their full vector context.
    """
    extra = {
        "dimensions": {
            "input_a": str(dim_a) if dim_a else "N/A",
            "input_b": str(dim_b) if dim_b else "N/A"
        }
    }
    logger.error(f"Physics Validation Failed: {str(error)}", extra=extra)
