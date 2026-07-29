from collections.abc import Callable
from typing import Any
from phystensor.core.exceptions import DimensionalityError

class OpDispatcher:
    """
    Handles dimensional logic for binary and unary operations.
    Implements the 'Inference as a Service' rule: No invalid physics allowed.
    """

    @staticmethod
    def handle_additive(op_name: str, dim_a: Any, dim_b: Any) -> None:
        """Validates that dimensions match for addition/subtraction."""
        if dim_a != dim_b:
            raise DimensionalityError(
                f"Cannot perform {op_name} on mismatched units: {dim_a} and {dim_b}"
            )

    @staticmethod
    def handle_multiplicative(op_name: str, dim_a: Any, dim_b: Any, inverse: bool = False) -> Any:
        """Calculates the resulting dimension for multiplication/division."""
        if inverse:
            return dim_a - dim_b
        return dim_a + dim_b
