from phystensor.io.logging import logger

def log_stability_warning(matrix_name: str, condition_number: float):
    """Logs a warning if a physical system is reaching numerical instability."""
    if condition_number > 1e12:
        logger.warning(
            f"Stability Warning: Matrix '{matrix_name}' is ill-conditioned. "
            f"Condition number: {condition_number:.2e}. Results may be unreliable."
        )

def log_decomposition(method: str, shape: tuple):
    """Trace log for expensive operations like SVD or Eigen."""
    logger.debug(f"Executing {method} on tensor of shape {shape}")
