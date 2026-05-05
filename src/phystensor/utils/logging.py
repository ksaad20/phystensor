import logging
from datetime import datetime

class PhysicsLogger:
    """
    Utility for internal trace logging of physical operations.
    Designed for low-latency recording of tensor transformations.
    """
    _logger = logging.getLogger("phystensor.utils")

    @classmethod
    def trace_op(cls, op_name: str, dim_a: tuple, dim_b: tuple = None):
        """Logs a trace of a physical operation for debugging complex graph builds."""
        msg = f"OP: {op_name} | Vector A: {dim_a}"
        if dim_b:
            msg += f" | Vector B: {dim_b}"
        cls._logger.debug(f"[{datetime.now().isoformat()}] {msg}")

    @classmethod
    def warn_precision(cls, message: str):
        cls._logger.warning(f"Precision Warning: {message}")
