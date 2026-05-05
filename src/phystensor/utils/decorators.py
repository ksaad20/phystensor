import functools
from phystensor.core.validation import DimensionalityManager

def dimensionless_required(func):
    """
    Decorator: Ensures the input PhysicalTensor is dimensionless 
    before executing the function (e.g., for sin, cos, exp).
    """
    @functools.wraps(func)
    def wrapper(tensor, *args, **kwargs):
        DimensionalityManager.validate_transcendental(tensor.dimensions, func.__name__)
        return func(tensor, *args, **kwargs)
    return wrapper

def preserve_dimensions(func):
    """
    Decorator: Ensures the output has the same dimensions as the input.
    Useful for filtering, sorting, or basic NumPy mappings.
    """
    @functools.wraps(func)
    def wrapper(tensor, *args, **kwargs):
        result_data = func(tensor.data, *args, **kwargs)
        return type(tensor)(result_data, tensor.dimensions)
    return wrapper
